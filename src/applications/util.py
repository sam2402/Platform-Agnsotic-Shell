from typing import List, Optional

from .application import ArgumentError


def read_lines(file_name: str) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines(keepends=True)


def parse_opt_boolean_flag(args: List[str], flag: str) \
        -> (bool, Optional[str]):
    if not args:
        return False, None
    if len(args) == 1:
        if args[0] == flag:
            return True, None
        return False, args[0]
    if len(args) == 2 and args[0] == flag:
        return True, args[1]

    raise ArgumentError()


def parse_opt_int_flag(args: List[str], flag: str, default: int) \
        -> (int, Optional[str]):
    if not args:
        return default, None
    if len(args) == 1:
        if args[0] == flag:
            raise ArgumentError()
        return default, args[0]
    if len(args) == 2 or len(args) == 3 and args[0] == flag:
        try:
            return int(args[1]), args[2] if len(args) == 3 else None
        except ValueError:
            raise ValueError(f"expected an integer, got '{args[1]}'")

    raise ArgumentError()
