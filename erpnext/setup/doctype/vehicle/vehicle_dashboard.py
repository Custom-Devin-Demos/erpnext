# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

from __future__ import annotations


def get_data() -> dict:
	return {
		"fieldname": "license_plate",
		"non_standard_fieldnames": {"Delivery Trip": "vehicle"},
		"transactions": [{"items": ["Vehicle Log"]}, {"items": ["Delivery Trip"]}],
	}
