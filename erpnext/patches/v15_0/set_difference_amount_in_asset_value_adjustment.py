from __future__ import annotations

import frappe


def execute() -> None:
	AssetValueAdjustment = frappe.qb.DocType("Asset Value Adjustment")

	frappe.qb.update(AssetValueAdjustment).set(
		AssetValueAdjustment.difference_amount,
		AssetValueAdjustment.new_asset_value - AssetValueAdjustment.current_asset_value,
	).where(AssetValueAdjustment.docstatus != 2).run()
