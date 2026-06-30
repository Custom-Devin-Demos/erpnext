from __future__ import annotations

import frappe


def execute() -> None:
	bom = frappe.qb.DocType("BOM")

	(
		frappe.qb.update(bom).set(bom.transfer_material_against, "Work Order").where(bom.with_operations == 0)
	).run()
