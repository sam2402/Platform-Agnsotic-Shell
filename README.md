# COMP0010 Shell

# Features

- All applications from the coursework brief are implemented.
- Extra flags have been added to the existing applications to make them more like their UNIX equivalents.
  - Extra flags have added to the following applications (documentation can be found in each application file):
    - `cat`: `-n`
    - `echo`: `-n`
    - `grep` `-v/--invert`, `-c/--colour`
    - `head`: `-v/--verbose`
    - `ls`: `-a`, `-r/--reverse`, `-s/--size`
    - `pwd`: `-P`
    - `sort`: `-R`, `-f`
    - `tail`: `-v/--invert`
- Extra UNIX applications have been added (`mkdir`, `rm`, `wc`) also with several flags.
- A help flag (`-h/--help`) has been added to every application which displays a usage message to the user.

## Design

- Class hierarchies are used to represent applications (`src/applications/application.py`) and commands
(`src/command.py`) to provide a polymorphic interface for interacting with them.  
- ANTLR is used for defining the command grammar (`src/antlr/Command.g4`) and parsing user input into a parse tree
(`src/parser.py`) which is then parsed into a `Command` object.
- A custom flag parsing system (`src/flagging.py`) was written to allow new flags to be added to applications with ease
by abstracting away boilerplate flag parsing code.
- Design patterns such as singleton (`src/application_factory.py`), adaptor (`UnsafeApplication` in
`src/applications/applications.py`, and factory (`src/application_factory.py`) have been utilised.
- Common utility methods have been extracted to `src/util.py`.

## Code Quality

- Applications each have their own files, as do and each part of the shell evaluation process to ensure each source file
and class has a single responsibility.
- [PEP8, the Python style guidelines](https://peps.python.org/pep-0008/) and all flake8 linting rules are followed
throughout.
- Type hints are used throughout the codebase, allowing IDEs to perform type checking so type errors can be caught
earlier in the development process.
- Documentation is provided for important public class methods.
- Unit tests are written in a consistent manner using a custom system to allow easy testing of applications with desired
flag combinations.

## Error Handling

- Custom error types (`ApplicationError`, `ArgumentError`, `ParsingError`) have been introduced.
- Error logic has been changed so that the shell does not crash when it is misused (e.g. if a user enters a command that does
not follow the grammar or if they provide invalid arguments to an application) but instead an informative error message
is provided based on the error type that was raised, enhancing the user's experience. 
