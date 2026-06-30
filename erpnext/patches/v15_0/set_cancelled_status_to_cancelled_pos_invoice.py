from __future__ import annotations

import frappe
from frappe.query_builder import DocType


def execute() -> None:
	POSInvoice = DocType("POS Invoice")

	frappe.qb.update(POSInvoice).set(POSInvoice.status, "Cancelled").where(POSInvoice.docstatus == 2).run()
