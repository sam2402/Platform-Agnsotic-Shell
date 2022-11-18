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
        4,0,11,51,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,25,8,0,11,0,12,0,
        26,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,4,10,48,8,10,11,10,12,10,49,0,0,11,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,2,8,0,33,33,35,38,40,58,
        61,61,63,91,93,95,97,123,125,126,2,0,9,9,32,32,52,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,24,
        1,0,0,0,3,28,1,0,0,0,5,30,1,0,0,0,7,32,1,0,0,0,9,34,1,0,0,0,11,36,
        1,0,0,0,13,38,1,0,0,0,15,40,1,0,0,0,17,42,1,0,0,0,19,44,1,0,0,0,
        21,47,1,0,0,0,23,25,7,0,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,
        0,0,0,26,27,1,0,0,0,27,2,1,0,0,0,28,29,5,124,0,0,29,4,1,0,0,0,30,
        31,5,59,0,0,31,6,1,0,0,0,32,33,5,10,0,0,33,8,1,0,0,0,34,35,5,39,
        0,0,35,10,1,0,0,0,36,37,5,34,0,0,37,12,1,0,0,0,38,39,5,96,0,0,39,
        14,1,0,0,0,40,41,5,95,0,0,41,16,1,0,0,0,42,43,5,62,0,0,43,18,1,0,
        0,0,44,45,5,60,0,0,45,20,1,0,0,0,46,48,7,1,0,0,47,46,1,0,0,0,48,
        49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,22,1,0,0,0,3,0,26,49,0
    ]

class CommandLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UNQUOTED = 1
    PIPE = 2
    SEMI = 3
    NEWLINE = 4
    SINGLE_QUOTE = 5
    DOUBLE_QUOTE = 6
    BACKTICK = 7
    UNDERSCORE = 8
    GT = 9
    LT = 10
    WHITESPACE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "';'", "'\\n'", "'''", "'\"'", "'`'", "'_'", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "UNQUOTED", "PIPE", "SEMI", "NEWLINE", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
            "BACKTICK", "UNDERSCORE", "GT", "LT", "WHITESPACE" ]

    ruleNames = [ "UNQUOTED", "PIPE", "SEMI", "NEWLINE", "SINGLE_QUOTE", 
                  "DOUBLE_QUOTE", "BACKTICK", "UNDERSCORE", "GT", "LT", 
                  "WHITESPACE" ]

    grammarFileName = "Command.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


