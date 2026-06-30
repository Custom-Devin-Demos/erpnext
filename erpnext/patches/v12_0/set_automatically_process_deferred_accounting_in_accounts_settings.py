from __future__ import annotations

import frappe


def execute() -> None:
	frappe.reload_doc("accounts", "doctype", "accounts_settings")

	frappe.db.set_single_value("Accounts Settings", "automatically_process_deferred_accounting_entry", 1)
