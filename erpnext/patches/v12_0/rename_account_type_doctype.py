from __future__ import annotations

import frappe


def execute() -> None:
	frappe.rename_doc("DocType", "Account Type", "Bank Account Type", force=True)
	frappe.rename_doc("DocType", "Account Subtype", "Bank Account Subtype", force=True)
	frappe.reload_doc("accounts", "doctype", "bank_account")
