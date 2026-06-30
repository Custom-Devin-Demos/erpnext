from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		"""
		UPDATE `tabStock Ledger Entry`
			SET posting_datetime = timestamp(posting_date, posting_time)
	"""
	)
