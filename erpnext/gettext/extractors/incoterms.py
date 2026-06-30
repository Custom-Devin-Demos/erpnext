from __future__ import annotations

from csv import DictReader
from io import StringIO
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from collections.abc import Iterator


def extract(fileobj, *args, **kwargs) -> Iterator[tuple]:
	"""Extract incoterm titles from a CSV file."""
	file = StringIO(fileobj.read().decode())  # CSV reader expects a text file
	reader = DictReader(file)
	for i, row in enumerate(reader):
		yield i + 2, "_", row["title"], ["Title of an incoterm"]
