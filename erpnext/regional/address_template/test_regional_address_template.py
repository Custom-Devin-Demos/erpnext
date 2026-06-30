from __future__ import annotations

from typing import TYPE_CHECKING

import frappe

from erpnext.regional.address_template.setup import get_address_templates, update_address_template
from erpnext.tests.utils import ERPNextTestSuite

if TYPE_CHECKING:
	from frappe.model.document import Document


def ensure_country(country: str) -> Document:
	if frappe.db.exists("Country", country):
		return frappe.get_doc("Country", country)
	else:
		c = frappe.get_doc({"doctype": "Country", "country_name": country})
		c.insert()
		return c


class TestRegionalAddressTemplate(ERPNextTestSuite):
	def test_get_address_templates(self) -> None:
		"""Get the countries and paths from the templates directory."""
		templates = get_address_templates()
		self.assertIsInstance(templates, list)
		self.assertIsInstance(templates[0], tuple)

	def test_create_address_template(self) -> None:
		"""Create a new Address Template."""
		country = ensure_country("Germany")
		update_address_template(country.name, "TEST")
		doc = frappe.get_doc("Address Template", country.name)
		self.assertEqual(doc.template, "TEST")

	def test_update_address_template(self) -> None:
		"""Update an existing Address Template."""
		country = ensure_country("Germany")
		if not frappe.db.exists("Address Template", country.name):
			frappe.get_doc(
				{"doctype": "Address Template", "country": country.name, "template": "EXISTING"}
			).insert()

		update_address_template(country.name, "NEW")
		doc = frappe.get_doc("Address Template", country.name)
		self.assertEqual(doc.template, "NEW")
