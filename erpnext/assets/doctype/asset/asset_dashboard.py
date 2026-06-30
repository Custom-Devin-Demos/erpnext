from __future__ import annotations

from frappe import _


def get_data() -> dict:
	return {
		"non_standard_fieldnames": {"Asset Movement": "asset"},
		"transactions": [{"label": _("Movement"), "items": ["Asset Movement"]}],
	}
