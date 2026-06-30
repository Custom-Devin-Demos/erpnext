from __future__ import annotations

import frappe

import erpnext
from erpnext.tests.utils import ERPNextTestSuite


@erpnext.allow_regional
def test_method() -> str:
	return "original"


class TestInit(ERPNextTestSuite):
	def test_regional_overrides(self) -> None:
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
