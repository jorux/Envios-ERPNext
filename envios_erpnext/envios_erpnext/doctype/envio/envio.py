# Copyright (c) 2022, Jorux and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

import frappe
from frappe import _

class Envio(Document):
  pass
@frappe.whitelist()
def make_envios(customer,sales_invoice):
    eee = frappe.new_doc("Envio")
    eee.customer = customer
    eee.sales_invoice = sales_invoice
    eee.instrucciones_especiales = "prueba"
    eee.insert(ignore_permissions=True)
    return eee.name
