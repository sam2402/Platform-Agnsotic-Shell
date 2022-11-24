from dataclasses import dataclass
from typing import Dict, List, Type, Union

ApplicationFlagDict = Dict[str, Union[str, int, bool]]
FlagType = Union[Type[str], Type[int], Type[bool]]


@dataclass
class Flag:
    name: str
    type: FlagType
    long_name: str = None
    argument_count: int = 0
    is_optional: bool = False
    default_value: Union[FlagType, List[FlagType]] = None

    def __str__(self) -> str:
        return self.name


class FlagConfiguration:

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
