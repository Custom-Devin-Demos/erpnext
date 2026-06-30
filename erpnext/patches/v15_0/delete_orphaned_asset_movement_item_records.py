from __future__ import annotations

import frappe


def execute() -> None:
	# nosemgrep
	frappe.db.sql(
		"""
		DELETE FROM `tabAsset Movement Item`
		WHERE parent NOT IN (SELECT name FROM `tabAsset Movement`)
		"""
	)
