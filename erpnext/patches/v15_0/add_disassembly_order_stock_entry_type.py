from __future__ import annotations

import frappe


def execute() -> None:
	if not frappe.db.exists("Stock Entry Type", "Disassemble"):
		frappe.get_doc(
			{
				"doctype": "Stock Entry Type",
				"name": "Disassemble",
				"purpose": "Disassemble",
				"is_standard": 1,
			}
		).insert(ignore_permissions=True)
