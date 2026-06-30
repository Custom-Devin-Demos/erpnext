from __future__ import annotations

import frappe
from frappe.query_builder import DocType


def execute() -> None:
	if not frappe.db.has_column("Payment Entry", "apply_tax_withholding_amount"):
		return

	pe = DocType("Payment Entry")
	(frappe.qb.update(pe).set(pe.apply_tds, pe.apply_tax_withholding_amount)).run()
