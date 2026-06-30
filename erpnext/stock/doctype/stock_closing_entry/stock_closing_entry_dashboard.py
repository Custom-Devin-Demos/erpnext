from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "stock_closing_entry",
		"transactions": [
			{
				"label": _("Stock Closing Log"),
				"items": ["Stock Closing Balance"],
			},
		],
	}
