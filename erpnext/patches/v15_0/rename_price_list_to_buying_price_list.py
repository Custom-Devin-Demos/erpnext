from __future__ import annotations

import frappe
from frappe.model.utils.rename_field import rename_field


def execute() -> None:
	if frappe.db.has_column("Material Request", "price_list"):
		rename_field(
			"Material Request",
			"price_list",
			"buying_price_list",
		)
