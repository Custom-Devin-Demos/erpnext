from __future__ import annotations

import frappe
from frappe.query_builder import DocType


def execute() -> None:
	Asset = DocType("Asset")

	query = (
		frappe.qb.update(Asset)
		.set(Asset.status, "Draft")
		.where((Asset.docstatus == 0) & ((Asset.status.isnull()) | (Asset.status == "")))
	)
	query.run()
