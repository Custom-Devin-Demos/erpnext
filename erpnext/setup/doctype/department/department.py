# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import annotations

import json

import frappe
from frappe.utils.nestedset import NestedSet, get_root_of

from erpnext.utilities.transaction_base import delete_events


class Department(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company: DF.Link
		department_name: DF.Data
		disabled: DF.Check
		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Data | None
		parent_department: DF.Link | None
		rgt: DF.Int
	# end: auto-generated types

	nsm_parent_field = "parent_department"

	def autoname(self) -> None:
		if self.company:
			self.name = get_abbreviated_name(self.department_name, self.company)
		else:
			self.name = self.department_name

	def validate(self) -> None:
		if not self.parent_department:
			root = get_root_of("Department")
			if root:
				self.parent_department = root

	def before_rename(self, old: str, new: str, merge: bool = False) -> str:
		# renaming consistency with abbreviation
		if frappe.get_cached_value("Company", self.company, "abbr") not in new:
			new = get_abbreviated_name(new, self.company)

		return new

	def on_update(self) -> None:
		if not (frappe.local.flags.ignore_update_nsm or frappe.flags.in_setup_wizard):
			super().on_update()

	def on_trash(self) -> None:
		super().on_trash()
		delete_events(self.doctype, self.name)


def on_doctype_update() -> None:
	frappe.db.add_index("Department", ["lft", "rgt"])


def get_abbreviated_name(name: str, company: str) -> str:
	abbr = frappe.get_cached_value("Company", company, "abbr")
	new_name = f"{name} - {abbr}"
	return new_name


@frappe.whitelist()
def get_children(
	doctype: str,
	parent: str | None = None,
	company: str | None = None,
	is_root: bool = False,
	include_disabled: str | dict | None = None,
) -> list:
	include_disabled = frappe.parse_json(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = {}

	if company == parent:
		filters["name"] = get_root_of("Department")
	elif company:
		filters["parent_department"] = parent
		filters["company"] = company
	else:
		filters["parent_department"] = parent

	if frappe.db.has_column(doctype, "disabled") and not include_disabled:
		filters["disabled"] = False

	return frappe.get_all("Department", fields=fields, filters=filters, order_by="name")


@frappe.whitelist()
def add_node() -> None:
	from frappe.desk.treeview import make_tree_args

	args = frappe.form_dict
	args = make_tree_args(**args)

	if args.parent_department == args.company:
		args.parent_department = None

	frappe.get_doc(args).insert()
