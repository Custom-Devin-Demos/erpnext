# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	frappe.delete_doc("Page", "modules_setup")
