from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("setup", "doctype", "currency_exchange")
	frappe.db.sql("""update `tabCurrency Exchange` set for_buying = 1, for_selling = 1""")
