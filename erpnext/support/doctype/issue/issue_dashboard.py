from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {"fieldname": "issue", "transactions": [{"label": _("Activity"), "items": ["Task"]}]}
