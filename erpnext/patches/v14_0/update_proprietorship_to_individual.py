from __future__ import annotations

import frappe


def execute() -> None:
	for doctype in ["Customer", "Supplier"]:
		field = doctype.lower() + "_type"
		frappe.db.set_value(doctype, {field: "Proprietorship"}, field, "Individual")
