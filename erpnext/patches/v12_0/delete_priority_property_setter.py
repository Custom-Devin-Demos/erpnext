from __future__ import annotations

import frappe


def execute() -> None:
	frappe.db.sql(
		"""
		DELETE FROM `tabProperty Setter`
		WHERE `tabProperty Setter`.doc_type='Issue'
			AND `tabProperty Setter`.field_name='priority'
			AND `tabProperty Setter`.property='options'
	"""
	)
