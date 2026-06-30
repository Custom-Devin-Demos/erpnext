# Copyright (c) 2018, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import annotations

import frappe
from frappe import _

from erpnext import get_region


def check_deletion_permission(doc, method: str) -> None:
	region = get_region(doc.company)
	if region in ["Nepal"] and doc.docstatus != 0:
		frappe.throw(_("Deletion is not permitted for country {0}").format(region))
