from __future__ import annotations

import click
import frappe


def execute() -> None:
	if "taxjar_integration" in frappe.get_installed_apps():
		return

	doctypes = ["TaxJar Settings", "TaxJar Nexus", "Product Tax Category"]
	for doctype in doctypes:
		frappe.delete_doc("DocType", doctype, ignore_missing=True)

	click.secho(
		"Taxjar Integration is moved to a separate app"
		"Please install the app to continue using the module: https://github.com/frappe/taxjar_integration",
		fg="yellow",
	)
