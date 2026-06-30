from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "time_sheet",
		"transactions": [{"label": _("References"), "items": ["Sales Invoice"]}],
	}
