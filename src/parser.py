import glob
import re
from typing import List, Tuple

from application import Application, UnsafeApplication
from application_cat import CatApplication
from application_cd import CdApplication
from application_cut import CutApplication
from application_echo import EchoApplication
from application_find import FindApplication
from application_grep import GrepApplication
from application_head_tail import HeadApplication, TailApplication
from application_ls import LsApplication
from application_pwd import PwdApplication
from application_sort import SortApplication
from application_uniq import UniqApplication


# At the moment this just handles semicolons, does
# glob expansion and returns [(application, args)]
def parse_raw_input(raw_line: str) -> List[Tuple[Application, List[str]]]:
    raw_commands = extract_raw_commands(raw_line)
    commands = []

    for raw_command in raw_commands:
        tokens = perform_glob_expansion(raw_command)
        app = app_from_name(tokens[0])
        args = tokens[1:]
        commands.append((app, args))

    return commands


APPLICATIONS = {
    "cat": CatApplication,
    "cd": CdApplication,
    "cut": CutApplication,
    "echo": EchoApplication,
    "find": FindApplication,
    "grep": GrepApplication,
    "head": HeadApplication,
    "ls": LsApplication,
    "pwd": PwdApplication,
    "sort": SortApplication,
    "tail": TailApplication,
    "uniq": UniqApplication,
}


def app_from_name(app_name: str, try_unsafe=True) -> Application:
    if try_unsafe and app_name.startswith("_"):
        app = app_from_name(app_name[1:], False)
        return UnsafeApplication(app)

    if app_name in APPLICATIONS:
        return APPLICATIONS[app_name]()

    raise ValueError(f"unknown application '{app_name}'")


def extract_raw_commands(raw_line: str) -> List[str]:
    raw_commands = []

    for match in re.finditer("([^\"';]+|\"[^\"]*\"|'[^']*')", raw_line):
        if match.group(0):
            raw_commands.append(match.group(0))

    return raw_commands


def perform_glob_expansion(raw_command: str) -> List[str]:
    tokens = []

    for match in re.finditer("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", raw_command):
        if match.group(1) or match.group(2):
            quoted = match.group(0)
            tokens.append(quoted[1:-1])
        else:
            globbing = glob.glob(match.group(0))
            if globbing:
                tokens.extend(globbing)
            else:
                tokens.append(match.group(0))

    return tokens
