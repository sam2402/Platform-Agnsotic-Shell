# Generated from Command.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,23,8,0,11,0,12,0,24,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,4,
        9,44,8,9,11,9,12,9,45,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,1,0,2,8,0,9,10,32,32,34,34,39,39,59,60,62,62,96,96,124,
        124,2,0,9,9,32,32,48,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,1,22,1,0,0,0,3,26,1,0,0,0,5,28,1,0,0,0,7,30,1,0,
        0,0,9,32,1,0,0,0,11,34,1,0,0,0,13,36,1,0,0,0,15,38,1,0,0,0,17,40,
        1,0,0,0,19,43,1,0,0,0,21,23,8,0,0,0,22,21,1,0,0,0,23,24,1,0,0,0,
        24,22,1,0,0,0,24,25,1,0,0,0,25,2,1,0,0,0,26,27,5,10,0,0,27,4,1,0,
        0,0,28,29,5,34,0,0,29,6,1,0,0,0,30,31,5,39,0,0,31,8,1,0,0,0,32,33,
        5,59,0,0,33,10,1,0,0,0,34,35,5,60,0,0,35,12,1,0,0,0,36,37,5,62,0,
        0,37,14,1,0,0,0,38,39,5,96,0,0,39,16,1,0,0,0,40,41,5,124,0,0,41,
        18,1,0,0,0,42,44,7,1,0,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,
        0,45,46,1,0,0,0,46,20,1,0,0,0,3,0,24,45,0
    ]

class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UNQUOTED = 1
    NEWLINE = 2
    DOUBLE_QUOTE = 3
    SINGLE_QUOTE = 4
    SEMI = 5
    LT = 6
    GT = 7
    BACKTICK = 8
    PIPE = 9
    WHITESPACE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'", "'\"'", "'''", "';'", "'<'", "'>'", "'`'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED", "NEWLINE", "DOUBLE_QUOTE", "SINGLE_QUOTE", "SEMI", 
            "LT", "GT", "BACKTICK", "PIPE", "WHITESPACE" ]

    ruleNames = [ "UNQUOTED", "NEWLINE", "DOUBLE_QUOTE", "SINGLE_QUOTE", 
                  "SEMI", "LT", "GT", "BACKTICK", "PIPE", "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


