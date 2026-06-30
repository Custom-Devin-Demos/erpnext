from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("manufacturing", "doctype", "workstation")

	frappe.db.sql(
		""" UPDATE `tabWorkstation`
        SET production_capacity = 1 """
	)
