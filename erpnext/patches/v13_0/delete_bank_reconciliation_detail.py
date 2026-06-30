# Copyright (c) 2019, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.exists("DocType", "Bank Reconciliation Detail") and frappe.db.exists(
		"DocType", "Bank Clearance Detail"
	):
		frappe.delete_doc("DocType", "Bank Reconciliation Detail", force=1)
