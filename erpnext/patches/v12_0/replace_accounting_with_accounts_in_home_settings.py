from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		"""UPDATE `tabUser` SET `home_settings` = REPLACE(`home_settings`, 'Accounting', 'Accounts')"""
	)
	frappe.cache().delete_key("home_settings")
