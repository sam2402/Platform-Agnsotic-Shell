from dataclasses import dataclass
from typing import List, Type, Union


@dataclass
class Flag:
    name: str
    type: Union[Type[str], Type[int], Type[bool]]
    long_name: str = None
    argument_count: int = 0
    is_optional: bool = False

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
        raise KeyError("No such flag ")

    def __str__(self) -> str:
        return str([str(flag) for flag in self.flags])
