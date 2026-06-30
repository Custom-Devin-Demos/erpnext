from __future__ import annotations

from frappe.model.utils.rename_field import rename_field


def execute() -> None:
	rename_field("Asset", "gross_purchase_amount", "net_purchase_amount")
	rename_field("Asset Depreciation Schedule", "gross_purchase_amount", "net_purchase_amount")
