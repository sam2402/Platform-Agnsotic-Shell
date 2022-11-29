"""Store of common utility functions used in the COMP0010 shell"""

from applications.application import ApplicationError


def read_lines(file_name: str) -> list[str]:
    try:
        with open(file_name) as file:
            return file.read().splitlines(keepends=True)
    except FileNotFoundError:
        raise ApplicationError(f"file '{file_name}' does not exist")


def write_lines(file_name: str, lines: list[str]):
    with open(file_name, "w") as file:
        file.writelines(lines)
