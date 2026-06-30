# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import annotations

from typing import TYPE_CHECKING

import frappe
from frappe import _
from frappe.utils.nestedset import NestedSet

if TYPE_CHECKING:
	from frappe.model.document import Document


class QualityProcedure(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from erpnext.quality_management.doctype.quality_procedure_process.quality_procedure_process import (
			QualityProcedureProcess,
		)

		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Data | None
		parent_quality_procedure: DF.Link | None
		process_owner: DF.Link | None
		process_owner_full_name: DF.Data | None
		processes: DF.Table[QualityProcedureProcess]
		quality_procedure_name: DF.Data
		rgt: DF.Int
	# end: auto-generated types

	nsm_parent_field = "parent_quality_procedure"

	def before_save(self) -> None:
		self.check_for_incorrect_child()

	def on_update(self) -> None:
		NestedSet.on_update(self)
		self.set_parent()
		self.remove_parent_from_old_child()
		self.add_child_to_parent()
		self.remove_child_from_old_parent()

	def after_insert(self) -> None:
		self.set_parent()
		self.add_child_to_parent()

	def on_trash(self) -> None:
		# clear from child table (sub procedures)
		qpp = frappe.qb.DocType("Quality Procedure Process")
		frappe.qb.update(qpp).set(qpp["procedure"], "").where(qpp["procedure"] == self.name).run()
		NestedSet.on_trash(self, allow_root_deletion=True)

	def check_for_incorrect_child(self) -> None:
		for process in self.processes:
			if process.procedure:
				self.is_group = 1
				# Check if any child process belongs to another parent.
				parent_quality_procedure = frappe.db.get_value(
					"Quality Procedure", process.procedure, "parent_quality_procedure"
				)
				if parent_quality_procedure and parent_quality_procedure != self.name:
					frappe.throw(
						_("{0} already has a Parent Procedure {1}.").format(
							frappe.bold(process.procedure), frappe.bold(parent_quality_procedure)
						),
						title=_("Invalid Child Procedure"),
					)

	def set_parent(self) -> None:
		"""Set `Parent Procedure` in `Child Procedures`"""

		for process in self.processes:
			if process.procedure:
				if not frappe.db.get_value(
					"Quality Procedure", process.procedure, "parent_quality_procedure"
				):
					frappe.db.set_value(
						"Quality Procedure", process.procedure, "parent_quality_procedure", self.name
					)

	def remove_parent_from_old_child(self) -> None:
		"""Remove `Parent Procedure` from `Old Child Procedures`"""

		if old_doc := self.get_doc_before_save():
			if old_child_procedures := set([d.procedure for d in old_doc.processes if d.procedure]):
				current_child_procedures = set([d.procedure for d in self.processes if d.procedure])

				if removed_child_procedures := list(
					old_child_procedures.difference(current_child_procedures)
				):
					for child_procedure in removed_child_procedures:
						frappe.db.set_value(
							"Quality Procedure", child_procedure, "parent_quality_procedure", None
						)

	def add_child_to_parent(self) -> None:
		"""Add `Child Procedure` to `Parent Procedure`"""

		if self.parent_quality_procedure:
			parent = frappe.get_doc("Quality Procedure", self.parent_quality_procedure)
			if not [d for d in parent.processes if d.procedure == self.name]:
				parent.append("processes", {"procedure": self.name, "process_description": self.name})
				parent.save()

	def remove_child_from_old_parent(self) -> None:
		"""Remove `Child Procedure` from `Old Parent Procedure`"""

		if old_doc := self.get_doc_before_save():
			if old_parent := old_doc.parent_quality_procedure:
				if self.parent_quality_procedure != old_parent:
					parent = frappe.get_doc("Quality Procedure", old_parent)
					for process in parent.processes:
						if process.procedure == self.name:
							parent.remove(process)
					parent.save()


@frappe.whitelist()
def get_children(
	doctype: str,
	parent: str | None = None,
	parent_quality_procedure: str | None = None,
	is_root: bool = False,
) -> list:
	if parent is None or parent == "All Quality Procedures":
		parent = ""

	if parent:
		parent_procedure = frappe.get_doc("Quality Procedure", parent)
		# return the list in order
		return [
			dict(
				value=d.procedure,
				expandable=frappe.db.get_value("Quality Procedure", d.procedure, "is_group"),
			)
			for d in parent_procedure.processes
			if d.procedure
		]
	else:
		return frappe.get_all(
			"Quality Procedure",
			fields=["name as value", "is_group as expandable"],
			filters=dict(parent_quality_procedure=parent),
			order_by="name asc",
		)


@frappe.whitelist()
def add_node() -> Document:
	from frappe.desk.treeview import make_tree_args

	args = frappe.form_dict
	args = make_tree_args(**args)

	if args.parent_quality_procedure == "All Quality Procedures":
		args.parent_quality_procedure = None

	return frappe.get_doc(args).insert()
