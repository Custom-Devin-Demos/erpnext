from __future__ import annotations

import frappe


def execute() -> None:
	for ws in ["Receivables", "Payables"]:
		frappe.delete_doc_if_exists("Workspace Sidebar", ws)
		frappe.delete_doc_if_exists("Workspace", ws)
