from __future__ import annotations

import frappe


def execute() -> None:
	Asset = frappe.qb.DocType("Asset")
	query = (
		frappe.qb.update(Asset)
		.set(Asset.status, "Work In Progress")
		.where((Asset.docstatus == 0) & (Asset.is_composite_asset == 1))
	)
	query.run()
