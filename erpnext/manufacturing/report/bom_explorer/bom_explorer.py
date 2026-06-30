# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from __future__ import annotations

import frappe
from frappe import _


def execute(filters: dict | None = None) -> tuple:
	data = []
	columns = get_columns()
	get_data(filters, data)
	return columns, data


def get_data(filters: dict, data: list) -> None:
	get_exploded_items(filters.bom, data)


def get_exploded_items(bom: str, data: list, indent: int = 0, qty: float = 1) -> None:
	exploded_items = frappe.get_all(
		"BOM Item",
		filters={"parent": bom},
		fields=[
			"qty",
			"bom_no",
			"qty",
			"item_code",
			"item_name",
			"description",
			"uom",
			"idx",
			"is_phantom_item",
		],
		order_by="idx ASC",
	)

	for item in exploded_items:
		item["indent"] = indent
		data.append(
			{
				"item_code": item.item_code,
				"item_name": item.item_name,
				"indent": indent,
				"bom_level": indent,
				"bom": item.bom_no,
				"qty": item.qty * qty,
				"uom": item.uom,
				"description": item.description,
				"is_phantom_item": item.is_phantom_item,
			}
		)
		if item.bom_no:
			get_exploded_items(item.bom_no, data, indent=indent + 1, qty=item.qty)


def get_columns() -> list:
	return [
		{
			"label": _("Item Code"),
			"fieldtype": "Link",
			"fieldname": "item_code",
			"width": 300,
			"options": "Item",
		},
		{"label": _("Item Name"), "fieldtype": "data", "fieldname": "item_name", "width": 100},
		{"label": _("BOM"), "fieldtype": "Link", "fieldname": "bom", "width": 150, "options": "BOM"},
		{"label": _("Is Phantom Item"), "fieldtype": "Check", "fieldname": "is_phantom_item"},
		{"label": _("Qty"), "fieldtype": "data", "fieldname": "qty", "width": 100},
		{"label": _("UOM"), "fieldtype": "data", "fieldname": "uom", "width": 100},
		{"label": _("BOM Level"), "fieldtype": "Int", "fieldname": "bom_level", "width": 100},
		{
			"label": _("Standard Description"),
			"fieldtype": "data",
			"fieldname": "description",
			"width": 150,
		},
	]
