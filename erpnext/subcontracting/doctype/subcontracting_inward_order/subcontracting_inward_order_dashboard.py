from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "subcontracting_inward_order",
		"transactions": [
			{
				"label": _("Transactions"),
				"items": ["Stock Entry"],
			},
			{
				"label": _("Manufacturing"),
				"items": ["Work Order"],
			},
		],
	}
