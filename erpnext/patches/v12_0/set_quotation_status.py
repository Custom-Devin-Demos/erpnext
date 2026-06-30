from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		""" UPDATE `tabQuotation` set status = 'Open'
		where docstatus = 1 and status = 'Submitted' """
	)
