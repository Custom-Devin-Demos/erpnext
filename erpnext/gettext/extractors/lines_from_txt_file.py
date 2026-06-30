from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from collections.abc import Iterator


def extract(fileobj, *args, **kwargs) -> Iterator[tuple]:
	"""Split file into lines and yield one translation unit per line."""
	for line_no, line in enumerate(fileobj.readlines()):
		yield line_no + 1, "_", line.decode().strip(), []
