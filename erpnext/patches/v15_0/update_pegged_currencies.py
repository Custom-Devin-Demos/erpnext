from __future__ import annotations

from erpnext.setup.install import update_pegged_currencies


def execute() -> None:
	update_pegged_currencies()
