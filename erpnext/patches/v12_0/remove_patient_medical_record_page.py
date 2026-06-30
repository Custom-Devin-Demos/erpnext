# Copyright (c) 2019


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.delete_doc("Page", "medical_record")
