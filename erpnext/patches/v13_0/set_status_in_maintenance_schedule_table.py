from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("maintenance", "doctype", "Maintenance Schedule Detail")
	frappe.db.sql(
		"""
		UPDATE `tabMaintenance Schedule Detail`
		SET completion_status = 'Pending'
		WHERE docstatus < 2
	"""
	)
