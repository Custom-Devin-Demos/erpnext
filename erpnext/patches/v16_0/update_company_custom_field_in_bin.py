from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("stock", "doctype", "bin")

	frappe.db.sql(
		"""
        UPDATE `tabBin` b
        INNER JOIN `tabWarehouse` w ON b.warehouse = w.name
        SET b.company = w.company
        WHERE b.company IS NULL OR b.company = ''
    """
	)
