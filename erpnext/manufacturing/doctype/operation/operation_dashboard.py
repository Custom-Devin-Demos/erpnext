from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"fieldname": "operation",
		"transactions": [{"label": _("Manufacture"), "items": ["BOM", "Work Order", "Job Card"]}],
	}
