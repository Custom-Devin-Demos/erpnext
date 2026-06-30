from __future__ import annotations

from contextlib import contextmanager

import frappe


@contextmanager
def temporary_flag(flag_name: str, value) -> None:
	flags = frappe.local.flags
	flags[flag_name] = value
	try:
		yield
	finally:
		flags.pop(flag_name, None)
