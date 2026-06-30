from __future__ import annotations

from erpnext.setup.install import create_custom_company_links


def execute() -> None:
	"""Add link fields to Company in Email Account and Communication."""
	create_custom_company_links()
