from __future__ import annotations

import frappe


def execute() -> None:
	for ws in ["Retail", "Utilities"]:
		frappe.delete_doc_if_exists("Workspace", ws)

	for ws in ["Integrations", "Settings"]:
		frappe.db.set_value("Workspace", ws, "public", 0)
