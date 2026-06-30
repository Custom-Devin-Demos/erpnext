from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doctype("System Settings")
	settings = frappe.get_doc("System Settings")
	settings.db_set("app_name", "ERPNext", commit=True)
