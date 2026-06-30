from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("projects", "doctype", "project")

	frappe.db.sql(
		"""UPDATE `tabProject`
		SET
			naming_series = 'PROJ-.####'
		WHERE
			naming_series is NULL"""
	)
