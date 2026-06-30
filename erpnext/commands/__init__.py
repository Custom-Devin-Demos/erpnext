# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# GPL v3 License. See license.txt

from __future__ import annotations

import click


def call_command(cmd: click.Command, context: dict):
	return click.Context(cmd, obj=context).forward(cmd)


commands = []
