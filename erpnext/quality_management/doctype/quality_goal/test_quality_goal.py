# Copyright (c) 2018, Frappe and Contributors
# See license.txt

from __future__ import annotations

from typing import TYPE_CHECKING

import frappe

from erpnext.tests.utils import ERPNextTestSuite

if TYPE_CHECKING:
	from frappe.model.document import Document


class TestQualityGoal(ERPNextTestSuite):
	def test_quality_goal(self) -> None:
		# no code, just a basic sanity check
		goal = get_quality_goal()
		self.assertTrue(goal)
		goal.delete()


def get_quality_goal() -> Document:
	return frappe.get_doc(
		doctype="Quality Goal",
		goal="Test Quality Module",
		frequency="Daily",
		objectives=[dict(objective="Check test cases", target="100", uom="Percent")],
	).insert()
