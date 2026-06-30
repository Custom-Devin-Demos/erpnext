from __future__ import annotations

import frappe


def get_context(context) -> None:
	context.no_cache = 1

	timelog = frappe.get_doc("Time Log", frappe.form_dict.timelog)

	context.doc = timelog
