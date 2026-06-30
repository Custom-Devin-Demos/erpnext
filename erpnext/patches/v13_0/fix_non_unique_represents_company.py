from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		"""
		update tabCustomer
		set represents_company = NULL
		where represents_company = ''
	"""
	)
