from __future__ import annotations

import frappe


def execute() -> None:
	pr_table = frappe.qb.DocType("Pricing Rule")
	(
		frappe.qb.update(pr_table)
		.set(pr_table.has_priority, 1)
		.where((pr_table.priority.isnotnull()) & (pr_table.priority != ""))
	).run()
