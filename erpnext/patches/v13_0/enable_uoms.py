from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("setup", "doctype", "uom")

	uom = frappe.qb.DocType("UOM")

	(
		frappe.qb.update(uom)
		.set(uom.enabled, 1)
		.where(uom.creation >= "2021-10-18")  # date when this field was released
	).run()
