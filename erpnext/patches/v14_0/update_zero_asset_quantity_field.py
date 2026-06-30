from __future__ import annotations

import frappe


def execute() -> None:
	asset = frappe.qb.DocType("Asset")
	frappe.qb.update(asset).set(asset.asset_quantity, 1).where(asset.asset_quantity == 0).run()
