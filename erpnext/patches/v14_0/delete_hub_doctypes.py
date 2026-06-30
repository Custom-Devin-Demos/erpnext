from __future__ import annotations

import frappe


def execute() -> None:
	doctypes = frappe.get_all("DocType", {"module": "Hub Node", "custom": 0}, pluck="name")
	for doctype in doctypes:
		frappe.delete_doc("DocType", doctype, ignore_missing=True)

	frappe.delete_doc("Module Def", "Hub Node", ignore_missing=True, force=True)
