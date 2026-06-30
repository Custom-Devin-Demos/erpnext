# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe


def execute() -> None:
	for report in ["Delayed Order Item Summary", "Delayed Order Summary"]:
		if frappe.db.exists("Report", report):
			frappe.delete_doc("Report", report)
