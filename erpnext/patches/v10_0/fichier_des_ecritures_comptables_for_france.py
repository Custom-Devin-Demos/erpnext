# Copyright (c) 2018, Frappe and Contributors
# License: GNU General Public License v3. See license.txt


from __future__ import annotations

import frappe

from erpnext.setup.doctype.company.company import install_country_fixtures


def execute() -> None:
	frappe.reload_doc("regional", "report", "fichier_des_ecritures_comptables_[fec]")
	for d in frappe.get_all("Company", filters={"country": "France"}):
		install_country_fixtures(d.name)
