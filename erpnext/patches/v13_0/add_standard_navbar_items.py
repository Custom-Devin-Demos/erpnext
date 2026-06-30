# import frappe
from __future__ import annotations

from erpnext.setup.install import add_standard_navbar_items


def execute() -> None:
	# Add standard navbar items for ERPNext in Navbar Settings
	add_standard_navbar_items()
