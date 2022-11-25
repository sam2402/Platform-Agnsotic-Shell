from typing import List, Type

from applications.application import (
    Application,
    ArgumentError,
    UnsafeApplication,
    ApplicationError,
)
from applications.cat import Cat
from applications.cd import Cd
from applications.cut import Cut
from applications.echo import Echo
from applications.find import Find
from applications.grep import Grep
from applications.head_tail import Head, Tail
from applications.ls import Ls
from applications.mkdir import Mkdir
from applications.pwd import Pwd
from applications.rm import Rm
from applications.sort import Sort
from applications.uniq import Uniq
from flagging import ApplicationFlagDict, FlagConfiguration

APPLICATIONS = {
    "cat": Cat,
    "cd": Cd,
    "cut": Cut,
    "echo": Echo,
    "find": Find,
    "grep": Grep,
    "head": Head,
    "ls": Ls,
    "mkdir": Mkdir,
    "pwd": Pwd,
    "rm": Rm,
    "sort": Sort,
    "tail": Tail,
    "uniq": Uniq,
}


class ApplicationFactory:
    """
    Singleton Application Factory
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ApplicationFactory, cls).__new__(cls)
        return cls._instance

    def get_application(self, args: List[str]) -> Application:
        app_name = args[0]
        if app_name.startswith("_"):
            return UnsafeApplication(self._get_safe_application(
                app_name[1:], args[1:]
            ))
        return self._get_safe_application(app_name, args[1:])

    def _get_safe_application(
            self, app_name: str, application_args: List[str]
    ) -> Application:
        application_type = self._get_app_type(app_name)
        flags = self._parse_flags(
            application_type.flag_configuration,
            application_args
        )
        return application_type(flags)

    def _get_app_type(self, app_name: str) -> Type[Application]:
        if app_name in APPLICATIONS:
            return APPLICATIONS[app_name]
        raise ApplicationError(f"unknown application '{app_name}'")

    def _parse_flags(
            self, flag_configuration: FlagConfiguration, args: List[str]
    ) -> ApplicationFlagDict:
        flags = {}
        for i in range(len(args)):
            arg = args[i]
            if arg in flag_configuration:
                flag = flag_configuration[arg]
                try:
                    flag_values = list(
                        map(
                            lambda x: flag.type(x),
                            args[i + 1: i + flag.argument_count + 1],
                        )
                    )
                except ValueError:
                    raise ArgumentError("invalid flags argument types")
                if len(flag_values) != flag.argument_count:
                    raise ArgumentError("invalid flags argument")
                if len(flag_values) == 0:
                    flag_value = True
                elif len(flag_values) == 1:
                    flag_value = flag_values[0]
                else:
                    flag_value = flag_values
                flags[flag.name] = flag_value
                i += flag_configuration[arg].argument_count
            else:
                return self._clean_flags(flag_configuration, flags)
        return self._clean_flags(flag_configuration, flags)

    def _clean_flags(
        self,
        flag_configuration: FlagConfiguration,
        flags: ApplicationFlagDict,
    ):
        cleaned_flags = flags
        for flag in flag_configuration.required_flags():
            if flag.type is bool and flag.name not in flags:
                cleaned_flags[flag.name] = False
            if flag.name not in flags:
                raise ArgumentError(f"expected flag {flag.name}")

        for flag in flag_configuration.optional_flags():
            if flag.name not in cleaned_flags:
                if flag.default_value is not None:
                    cleaned_flags[flag.name] = flag.default_value
                elif flag.type is bool:
                    cleaned_flags[flag.name] = False
        return cleaned_flags
