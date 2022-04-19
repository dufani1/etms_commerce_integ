from ast import arg
from functools import wraps
import frappe
from frappe.core.doctype.user.user import generate_keys
from frappe.core.doctype.user.user import User
from pandas import read_html


def eci_verify_request(func):

    def wrapper(*args, **kwargs):
        headers = frappe.request.headers
        eci_settings = frappe.get_single("ECI Commerce Settings")
        if eci_settings.enabled == 0:
            return {"message": "services_disabled"}
        try:
            API_KEY = headers["Consumer-Key"]
            API_SECRET = headers["Consumer-Secret"]

            if API_KEY != eci_settings.api_key or API_SECRET != eci_settings.get_password(
                    "api_secret"):
                    return {"message": "not_authorized"}
            del kwargs['cmd']
            return func(*args, **kwargs)

        except Exception as e:
            raise e
            return {"message": "not_authorized"}

    return wrapper


@frappe.whitelist(allow_guest=False, methods=["GET"])
@eci_verify_request
def user_info():
    user = frappe.get_doc("User", frappe.session.user)

    address_line1 = frappe.db.get_value(
        "Address",
        filters={"name": f"{user.name}-Shipping"},
        fieldname="address_line1")
    city = frappe.db.get_value("Address",
                               filters={"name": f"{user.name}-Shipping"},
                               fieldname="city")
    info = {
        "id": user.name,
        "name": user.name,
        "displayname": user.full_name,
        "username": user.username,
        "email": user.email,
        "firstname": user.first_name,
        "lastname": user.last_name,
        "nicename": user.first_name,
        "avatar": user.user_image,
        "url": "",
        "roles": [],
        "address_line1": address_line1,
        "city": city
    }

    return info


@frappe.whitelist(allow_guest=True, methods=["POST"])
@eci_verify_request
def login(usr, pwd, seconds):

    if usr and pwd:
        _user = User.find_by_credentials(usr, pwd)
        user = frappe.get_doc("User", _user.name)
        if user and _user["is_authenticated"]:
            return {
                "user": user.name,
                "api_key": user.api_key,
                "api_secret": user.get_password("api_secret"),
            }

    return "faild to login"


@frappe.whitelist(allow_guest=True, methods=["POST"])
def sign_up(username, new_password, first_name, last_name, phone_number):
    frappe.set_user("administrator")
    if frappe.get_value("ECI Commerce Settings", fieldname="allow_new_users_registrations") == 0:
        return {"message": "new_registrations_disabled"}

    user_exist = frappe.db.get("User", username)

    if user_exist:
        return {"message": "user_already_exist"}

    if frappe.db.get_creation_count('User', 60) > 300:
        return {
            "message":
            "Too many users signed up recently, so the registration is disabled. Please try back in an hour"
        }

    user = frappe.get_doc({
        "doctype": "User",
        "email": username,
        "first_name": first_name,
        "enabled": 1,
        "new_password": new_password,
        "last_name": last_name,
        "user_type": "Website User"
    })
    user.flags.ignore_permissions = True
    user.flags.ignore_password_policy = True

    # Generate api keys
    api_secret = frappe.generate_hash(length=15)
    api_key = frappe.generate_hash(length=15)

    user.api_key = api_key
    user.api_secret = api_secret

    user.insert()
    # user.add_roles("Customer")

    customer = frappe.get_doc({
        "doctype": "Customer",
        "account_manager": user.name,
        "customer_name": user.email,
        "customer_group": "Commercial",
        "territory": "All Territories",
        "customer_type": frappe._("Individual"),
        "mobile_no": phone_number
    })

    customer.flags.ignore_mandatory = True
    customer.flags.ignore_permissions = True
    customer.insert()

    return {"user": user.name, "api_key": api_key, "api_secret": api_secret}
