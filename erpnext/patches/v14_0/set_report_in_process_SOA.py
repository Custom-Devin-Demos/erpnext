# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE

from __future__ import annotations

import frappe


def execute() -> None:
	process_soa = frappe.qb.DocType("Process Statement Of Accounts")
	q = frappe.qb.update(process_soa).set(process_soa.report, "General Ledger")
	q.run()
