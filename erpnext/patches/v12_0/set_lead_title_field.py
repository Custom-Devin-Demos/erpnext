from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("crm", "doctype", "lead")
	frappe.db.sql(
		"""
		UPDATE
			`tabLead`
		SET
			title = IF(organization_lead = 1, company_name, lead_name)
	"""
	)
