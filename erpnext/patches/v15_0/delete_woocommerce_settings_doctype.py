from __future__ import annotations

import frappe


def execute() -> None:
	frappe.delete_doc("DocType", "Woocommerce Settings", ignore_missing=True)
