from __future__ import annotations

from frappe import _


def get_data():
	return {
		"fieldname": "bank",
		"transactions": [{"label": _("Bank Details"), "items": ["Bank Account", "Bank Guarantee"]}],
	}
