from __future__ import annotations

import frappe
from frappe.model.utils.rename_field import rename_field


def execute() -> None:
	if frappe.db.has_column("Purchase Order Item", "subcontracted_quantity"):
		rename_field("Purchase Order Item", "subcontracted_quantity", "subcontracted_qty")
