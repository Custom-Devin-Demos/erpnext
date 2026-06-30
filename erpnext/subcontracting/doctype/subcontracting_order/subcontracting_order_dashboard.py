from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "subcontracting_order",
		"non_standard_fieldnames": {"Stock Reservation Entry": "voucher_no"},
		"transactions": [
			{
				"label": _("Reference"),
				"items": ["Subcontracting Receipt", "Stock Entry"],
			},
			{
				"label": _("Stock Reservation"),
				"items": ["Stock Reservation Entry"],
			},
		],
	}
