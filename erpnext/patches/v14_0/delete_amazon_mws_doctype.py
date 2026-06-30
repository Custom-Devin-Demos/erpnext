from __future__ import annotations

import frappe


def execute() -> None:
	frappe.delete_doc("DocType", "Amazon MWS Settings", ignore_missing=True)
