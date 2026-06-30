# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("assets", "doctype", "Location")
	for dt in (
		"Account",
		"Cost Center",
		"File",
		"Employee",
		"Location",
		"Task",
		"Customer Group",
		"Sales Person",
		"Territory",
	):
		frappe.reload_doctype(dt)
		frappe.get_doc("DocType", dt).run_module_method("on_doctype_update")
