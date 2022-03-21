# Copyright (c) 2022, Jorux and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

import frappe
from frappe import _

class Envio(Document):
  pass
@frappe.whitelist()
def make_envios(customer):
    eee = frappe.new_doc("Envio")
    eee.customer = customer
    eee.instrucciones_especiales = "prueba"
    eee.insert(ignore_permissions=True)
    return eee.name
