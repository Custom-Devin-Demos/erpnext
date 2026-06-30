from __future__ import annotations

import frappe
from frappe.query_builder import DocType


def execute() -> None:
	if frappe.db.has_column("Asset Repair", "stock_entry"):
		AssetRepair = DocType("Asset Repair")
		StockEntry = DocType("Stock Entry")

		(
			frappe.qb.update(StockEntry)
			.join(AssetRepair)
			.on(StockEntry.name == AssetRepair.stock_entry)
			.set(StockEntry.asset_repair, AssetRepair.name)
		).run()
