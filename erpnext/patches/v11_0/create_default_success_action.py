from __future__ import annotations

import frappe

from erpnext.setup.install import create_default_success_action


def execute() -> None:
	frappe.reload_doc("core", "doctype", "success_action")
	create_default_success_action()
