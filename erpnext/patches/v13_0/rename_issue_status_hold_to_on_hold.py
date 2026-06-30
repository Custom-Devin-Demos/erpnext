# Copyright (c) 2020, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	if frappe.db.exists("DocType", "Issue"):
		frappe.reload_doc("support", "doctype", "issue")
		rename_status()


def rename_status() -> None:
	frappe.db.sql(
		"""
		UPDATE
			`tabIssue`
		SET
			status = 'On Hold'
		WHERE
			status = 'Hold'
	"""
	)
