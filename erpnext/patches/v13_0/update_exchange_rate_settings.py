from __future__ import annotations

import frappe

from erpnext.setup.install import setup_currency_exchange


def execute() -> None:
	frappe.reload_doc("accounts", "doctype", "currency_exchange_settings")
	setup_currency_exchange()
