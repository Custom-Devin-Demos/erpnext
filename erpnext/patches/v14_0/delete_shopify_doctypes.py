from __future__ import annotations

import frappe


def execute() -> None:
	frappe.delete_doc("DocType", "Shopify Settings", ignore_missing=True)
	frappe.delete_doc("DocType", "Shopify Log", ignore_missing=True)
