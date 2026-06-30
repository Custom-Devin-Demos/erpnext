# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# License: MIT. See LICENSE


from __future__ import annotations

import frappe


def execute() -> None:
	# nosemgrep
	frappe.db.sql(
		"""
		UPDATE `tabPeriod Closing Voucher`
		SET
			period_start_date = (select year_start_date from `tabFiscal Year` where name = fiscal_year),
			period_end_date = posting_date
	"""
	)
