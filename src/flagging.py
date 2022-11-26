"""Module for handling user flags"""

from dataclasses import dataclass
from typing import get_args, Dict, List, Type, Union

ApplicationFlagDict = Dict[str, Union[str, int, bool]]
FlagType = Union[Type[str], Type[int], Type[bool]]


@dataclass
class Flag:
    """The data about a flag an application accepts"""
    name: str
    type: FlagType
    long_name: str = None
    argument_count: int = 0
    is_optional: bool = False
    default_value: Union[get_args(FlagType)[0],
                         List[get_args(FlagType)[0]]] = None

    def __str__(self) -> str:
        return self.name


class FlagConfiguration:
    """A store of flags an application accepts and methods for handling them

    Externally appears like a read only dictionary with flag names as keys and
    flags as values.
    See this typical use case:

    fc = FlagConfiguration([
        Flag("-r", bool, "--recursive"),
        Flag("-v", bool, "--verbose"),
        Flag("-f", bool, "--force")
    ])
    fc["-r"] # returns Flag("-r", bool, "--recursive")
    fc["-fake-flag"] # raises KeyError
    "-f" in fc # True
    """

    def __init__(self, flags: List[Flag] = None):
        self.flags = [Flag("-h", bool, "--help")] \
            + (flags if flags is not None else [])

    def optional_flags(self):
        return list(filter(lambda flag: flag.is_optional, self.flags))

    def required_flags(self):
        return list(filter(lambda flag: not flag.is_optional, self.flags))

    def __contains__(self, elem):
        return bool(list(filter(
            lambda flag: elem in [flag.name, flag.long_name],
            self.flags
        )))

    def __getitem__(self, item):
        for flag in self.flags:
            if item in [flag.name, flag.long_name]:
                return flag
        raise KeyError(f"No such flag '{item}'")

    def __str__(self) -> str:
        return str([str(flag) for flag in self.flags])
