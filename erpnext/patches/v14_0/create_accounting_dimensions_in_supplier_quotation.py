from __future__ import annotations

from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import (
	create_accounting_dimensions_for_doctype,
)


def execute() -> None:
	create_accounting_dimensions_for_doctype(doctype="Supplier Quotation")
	create_accounting_dimensions_for_doctype(doctype="Supplier Quotation Item")
