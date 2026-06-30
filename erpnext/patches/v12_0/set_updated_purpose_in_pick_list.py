# Copyright (c) 2019, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("stock", "doctype", "pick_list")
	frappe.db.sql(
		"""UPDATE `tabPick List` set purpose = 'Delivery'
        WHERE docstatus = 1  and purpose = 'Delivery against Sales Order' """
	)
