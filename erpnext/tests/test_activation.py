from __future__ import annotations

from erpnext.tests.utils import ERPNextTestSuite
from erpnext.utilities.activation import get_level


class TestActivation(ERPNextTestSuite):
	def test_activation(self) -> None:
		site_info = {"activation": {"activation_level": 0, "sales_data": []}}
		levels = get_level(site_info)
		self.assertTrue(levels)
