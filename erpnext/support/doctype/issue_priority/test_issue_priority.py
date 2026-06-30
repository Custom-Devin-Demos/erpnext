# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

from __future__ import annotations

import frappe

from erpnext.tests.utils import ERPNextTestSuite


class TestIssuePriority(ERPNextTestSuite):
	def test_priorities(self) -> None:
		make_priorities()
		priorities = frappe.get_list("Issue Priority")

		for priority in priorities:
			self.assertIn(priority.name, ["Low", "Medium", "High"])


def make_priorities() -> None:
	insert_priority("Low")
	insert_priority("Medium")
	insert_priority("High")


def insert_priority(name: str) -> None:
	if not frappe.db.exists("Issue Priority", name):
		frappe.get_doc({"doctype": "Issue Priority", "name": name}).insert(ignore_permissions=True)
