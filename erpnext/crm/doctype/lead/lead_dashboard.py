from __future__ import annotations


def get_data() -> dict:
	return {
		"fieldname": "lead",
		"non_standard_fieldnames": {"Quotation": "party_name", "Opportunity": "party_name"},
		"dynamic_links": {"party_name": ["Lead", "quotation_to"]},
		"transactions": [
			{"items": ["Opportunity", "Quotation", "Prospect"]},
		],
	}
