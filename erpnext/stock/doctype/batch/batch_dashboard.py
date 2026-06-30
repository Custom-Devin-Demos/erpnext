from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "batch_no",
		"transactions": [
			{"label": _("Buy"), "items": ["Purchase Invoice", "Purchase Receipt"]},
			{"label": _("Sell"), "items": ["Sales Invoice", "Delivery Note"]},
			{"label": _("Move"), "items": ["Stock Entry", "Serial and Batch Bundle"]},
			{"label": _("Quality"), "items": ["Quality Inspection"]},
		],
	}
