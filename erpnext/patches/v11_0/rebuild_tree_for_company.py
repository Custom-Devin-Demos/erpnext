from __future__ import annotations

import frappe
from frappe.utils.nestedset import rebuild_tree


def execute() -> None:
	frappe.reload_doc("setup", "doctype", "company")
	rebuild_tree("Company")
