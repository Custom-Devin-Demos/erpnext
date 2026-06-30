# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import annotations

from erpnext.accounts.report.sales_register.sales_register import _execute


def execute(filters: dict | None = None) -> tuple:
	return _execute(filters)
