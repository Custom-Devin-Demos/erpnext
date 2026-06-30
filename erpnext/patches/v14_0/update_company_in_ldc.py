# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


from __future__ import annotations

import frappe

from erpnext import get_default_company


def execute() -> None:
	company = get_default_company()
	if company:
		for d in frappe.get_all("Lower Deduction Certificate", pluck="name"):
			frappe.db.set_value("Lower Deduction Certificate", d, "company", company, update_modified=False)
