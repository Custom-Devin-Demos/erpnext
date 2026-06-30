from __future__ import annotations

from frappe.model.utils.rename_field import rename_field


def execute() -> None:
	rename_field(
		"Buying Settings",
		"over_order_allowance",
		"blanket_order_allowance",
	)

	rename_field(
		"Selling Settings",
		"over_order_allowance",
		"blanket_order_allowance",
	)
