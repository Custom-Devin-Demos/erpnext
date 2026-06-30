from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("manufacturing", "doctype", "work_order")

	frappe.db.sql(
		"""
		UPDATE
			`tabWork Order` wo
				JOIN `tabItem` item ON wo.production_item = item.item_code
		SET
			wo.item_name = item.item_name
	"""
	)
	frappe.db.commit()
