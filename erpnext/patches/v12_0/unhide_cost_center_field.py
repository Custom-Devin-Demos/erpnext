# Copyright (c) 2017, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		"""
		DELETE FROM `tabProperty Setter`
		WHERE doc_type in ('Sales Invoice', 'Purchase Invoice', 'Payment Entry')
		AND field_name = 'cost_center'
		AND property = 'hidden'
	"""
	)
