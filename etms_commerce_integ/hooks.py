from . import __version__ as app_version

app_name = "etms_commerce_integ"
app_title = "Etms Commerce Integ"
app_publisher = "ebkar Technologies"
app_description = "Integration For ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@ebkar.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/etms_commerce_integ/css/etms_commerce_integ.css"
# app_include_js = "/assets/etms_commerce_integ/js/etms_commerce_integ.js"

# include js, css files in header of web template
# web_include_css = "/assets/etms_commerce_integ/css/etms_commerce_integ.css"
# web_include_js = "/assets/etms_commerce_integ/js/etms_commerce_integ.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "etms_commerce_integ/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Item" : "public/js/item.js",
    "ECI Advertisements": "public/js/eci_advertisements.js",
    "ECI Customer Vehicles" : "public/js/eci_customer_vehicles.js",
    "ECI Vehicle Make": "public/js/eci_vehicle_make.js",
    "ECI Vehicle Model": "public/js/eci_vehicle_model.js",
    # "ECI Parts Request": "public/js/eci_parts_request.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "etms_commerce_integ.install.before_install"
# after_install = "etms_commerce_integ.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "etms_commerce_integ.uninstall.before_uninstall"
# after_uninstall = "etms_commerce_integ.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "etms_commerce_integ.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"on_update": "etms_commerce_integ.events.item.on_update"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"etms_commerce_integ.tasks.all"
# 	],
# 	"daily": [
# 		"etms_commerce_integ.tasks.daily"
# 	],
# 	"hourly": [
# 		"etms_commerce_integ.tasks.hourly"
# 	],
# 	"weekly": [
# 		"etms_commerce_integ.tasks.weekly"
# 	]
# 	"monthly": [
# 		"etms_commerce_integ.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "etms_commerce_integ.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "etms_commerce_integ.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "etms_commerce_integ.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# User Data Protection
# --------------------

user_data_fields = [{
    "doctype": "{doctype_1}",
    "filter_by": "{filter_by}",
    "redact_fields": ["{field_1}", "{field_2}"],
    "partial": 1,
}, {
    "doctype": "{doctype_2}",
    "filter_by": "{filter_by}",
    "partial": 1,
}, {
    "doctype": "{doctype_3}",
    "strict": False,
}, {
    "doctype": "{doctype_4}"
}]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"etms_commerce_integ.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []

fixtures = [
    {
		"dt":"Role", 
		"filters": [["name", "in", (
            "ECI System Manager",
            "ECI System User",
            "ECI Product Manager"
        )]]
	},
    {
    "doctype":
    "Custom Field",
    "filters": [[
        "fieldname", "in",
        (
        # Item
        "eci_product_section",
        "eci_product",
        "eci_mfr_part_number",
        "publish_to_commerce_app",
        "eci_product_condition",
        "is_inspected",
        "inspection_note",
        "has_warranty",
        "warranty_note",
        "warehouses_to_check_item_availability",
        "eci_check_availability_in_suppliers_warehouse",
        "eci_supplier_warehouse_table",
        "eci_categories",
        "eci_product_tags_multiselect",
        "eci_product_images",
        "has_specific_compatibility",
        "eci_vehicle_compatibility",
        "mode_of_payment",
        "eci_expected_delivery_date",
        "eci_section",
        "expected_territory_delivery_time",
        # Sales Order
        "eci_order_section",
        "is_eci_order",
        "eci_shipping_territory",
        "eci_shipping_address",
        # Customer
        "eci_customer_section",
        "eci_is_customer_email_verified",
        "eci_email_confirmation_key",
        "eci_mobile_no_2",)
    ]]
}]
