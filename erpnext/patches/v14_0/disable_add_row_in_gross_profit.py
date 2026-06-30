from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.set_value("Report", "Gross Profit", "add_total_row", 0)
