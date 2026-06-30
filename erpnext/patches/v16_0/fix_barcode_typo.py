from __future__ import annotations

import frappe


def execute() -> None:
	frappe.qb.update("Item Barcode").set("barcode_type", "EAN-13").where(
		frappe.qb.Field("barcode_type") == "EAN-12"
	).run()
