from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("accounts", "doctype", "pos_closing_entry")

	frappe.db.sql("update `tabPOS Closing Entry` set `status` = 'Failed' where `status` = 'Queued'")
