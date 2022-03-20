from . import __version__ as app_version

app_name = "envios_erpnext"
app_title = "Envios Erpnext"
app_publisher = "Jorux"
app_description = "Simple app to create a doctype linked to sales invoice in ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "rodrishishi@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/envios_erpnext/css/envios_erpnext.css"
# app_include_js = "/assets/envios_erpnext/js/envios_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/envios_erpnext/css/envios_erpnext.css"
# web_include_js = "/assets/envios_erpnext/js/envios_erpnext.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "envios_erpnext/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "envios_erpnext.utils.jinja_methods",
# 	"filters": "envios_erpnext.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "envios_erpnext.install.before_install"
# after_install = "envios_erpnext.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "envios_erpnext.uninstall.before_uninstall"
# after_uninstall = "envios_erpnext.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "envios_erpnext.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"envios_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"envios_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"envios_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"envios_erpnext.tasks.weekly"
# 	],
# 	"monthly": [
# 		"envios_erpnext.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "envios_erpnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "envios_erpnext.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "envios_erpnext.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"envios_erpnext.auth.validate"
# ]

