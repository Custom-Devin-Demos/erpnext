# Copyright (c) 2017, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.exists("Company", {"country": "India"}):
		return

	frappe.reload_doc("core", "doctype", "has_role")
	frappe.db.sql(
		"""
		delete from
			`tabHas Role`
		where
			parenttype = 'Report' and parent in('GST Sales Register',
				'GST Purchase Register', 'GST Itemised Sales Register',
				'GST Itemised Purchase Register', 'Eway Bill')
		"""
	)
