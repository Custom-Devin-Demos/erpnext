from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("core", "doctype", "scheduled_job_type")
	if frappe.db.exists("Scheduled Job Type", "repost_item_valuation.repost_entries"):
		frappe.db.set_value("Scheduled Job Type", "repost_item_valuation.repost_entries", "stopped", 0)
