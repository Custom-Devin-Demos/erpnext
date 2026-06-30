# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.table_exists("Asset Adjustment") and not frappe.db.table_exists("Asset Value Adjustment"):
		frappe.rename_doc("DocType", "Asset Adjustment", "Asset Value Adjustment", force=True)
		frappe.reload_doc("assets", "doctype", "asset_value_adjustment")
