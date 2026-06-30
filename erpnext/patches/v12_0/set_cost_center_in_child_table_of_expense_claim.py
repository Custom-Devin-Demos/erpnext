from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("hr", "doctype", "expense_claim_detail")
	frappe.db.sql(
		"""
		UPDATE `tabExpense Claim Detail` child, `tabExpense Claim` par
		SET child.cost_center = par.cost_center
		WHERE child.parent = par.name
	"""
	)
