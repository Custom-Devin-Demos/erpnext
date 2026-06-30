from __future__ import annotations


def get_data():
	return {
		"fieldname": "payment_gateway_account",
		"non_standard_fieldnames": {"Subscription Plan": "payment_gateway"},
		"transactions": [{"items": ["Payment Request"]}, {"items": ["Subscription Plan"]}],
	}
