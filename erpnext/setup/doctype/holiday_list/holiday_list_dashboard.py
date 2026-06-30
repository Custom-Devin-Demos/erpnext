from __future__ import annotations


def get_data() -> dict:
	return {
		"fieldname": "holiday_list",
		"non_standard_fieldnames": {
			"Company": "default_holiday_list",
		},
		"transactions": [
			{
				"items": ["Company", "Employee", "Workstation"],
			},
			{"items": ["Service Level Agreement"]},
		],
	}
