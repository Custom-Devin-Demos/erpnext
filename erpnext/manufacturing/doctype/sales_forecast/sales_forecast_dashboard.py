from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "sales_forecast",
		"transactions": [
			{
				"label": _("MPS"),
				"items": ["Master Production Schedule"],
			},
		],
	}
