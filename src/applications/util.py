from typing import List

from .application import ApplicationError


def read_lines(file_name: str) -> List[str]:
    try:
        with open(file_name) as file:
            return file.read().splitlines(keepends=True)
    except FileNotFoundError:
        raise ApplicationError(f"file '{file_name}' does not exist")
