from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doctype("Payment Entry")
	frappe.db.sql(
		"""update `tabPayment Entry` set status = CASE
		WHEN docstatus = 1 THEN 'Submitted'
		WHEN docstatus = 2 THEN 'Cancelled'
		ELSE 'Draft'
		END;"""
	)
