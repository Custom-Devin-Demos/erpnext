from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.get_all("Company", filters={"country": "India"}, limit=1):
		frappe.db.set_single_value("Stock Settings", "allow_existing_serial_no", 1)
