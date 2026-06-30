from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "supplier",
		"non_standard_fieldnames": {"Payment Entry": "party", "Bank Account": "party"},
		"dynamic_links": {"party": ["Supplier", "party_type"]},
		"transactions": [
			{"label": _("Procurement"), "items": ["Request for Quotation", "Supplier Quotation"]},
			{"label": _("Orders"), "items": ["Purchase Order", "Purchase Receipt", "Purchase Invoice"]},
			{"label": _("Payments"), "items": ["Payment Entry", "Bank Account"]},
			{"label": _("Pricing"), "items": ["Pricing Rule"]},
		],
	}
