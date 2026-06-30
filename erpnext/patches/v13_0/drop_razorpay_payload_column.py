from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.exists("DocType", "Membership"):
		if "webhook_payload" in frappe.db.get_table_columns("Membership"):
			frappe.db.sql("alter table `tabMembership` drop column webhook_payload")
