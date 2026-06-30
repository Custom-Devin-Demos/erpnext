# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("accounts", "doctype", "Payment Schedule")
	if frappe.db.count("Payment Schedule"):
		frappe.db.sql(
			"""
			UPDATE
				`tabPayment Schedule` ps
			SET
				ps.outstanding = (ps.payment_amount - ps.paid_amount)
		"""
		)
