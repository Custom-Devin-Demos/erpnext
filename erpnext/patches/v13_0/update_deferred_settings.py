# Copyright (c) 2019, Frappe and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import annotations

import frappe


def execute() -> None:
	accounts_settings = frappe.get_doc("Accounts Settings", "Accounts Settings")
	accounts_settings.book_deferred_entries_based_on = "Days"
	accounts_settings.book_deferred_entries_via_journal_entry = 0
	accounts_settings.submit_journal_entries = 0
	accounts_settings.save()
