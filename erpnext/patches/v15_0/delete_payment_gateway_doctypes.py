from __future__ import annotations

import frappe


def execute() -> None:
	for dt in ("GoCardless Settings", "GoCardless Mandate", "Mpesa Settings"):
		frappe.delete_doc("DocType", dt, ignore_missing=True)
