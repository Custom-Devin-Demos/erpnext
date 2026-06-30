from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("buying", "doctype", "supplier_quotation")
	frappe.db.sql(
		"""UPDATE `tabSupplier Quotation`
		SET valid_till = DATE_ADD(transaction_date , INTERVAL 1 MONTH)
		WHERE docstatus < 2"""
	)
