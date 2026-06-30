from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.exists("Page", "point-of-sale"):
		frappe.rename_doc("Page", "pos", "point-of-sale", 1, 1)
