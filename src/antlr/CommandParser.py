# Generated from Command.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,3,0,30,8,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,44,8,2,1,3,3,3,47,8,3,1,3,1,3,3,3,51,8,3,5,3,53,8,3,10,3,
        12,3,56,9,3,1,3,1,3,3,3,60,8,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,
        3,3,3,69,8,3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,3,3,78,8,3,1,4,
        1,4,3,4,82,8,4,1,5,1,5,3,5,86,8,5,1,5,1,5,1,6,1,6,1,6,3,6,93,8,6,
        1,7,1,7,5,7,97,8,7,10,7,12,7,100,9,7,1,7,1,7,1,8,1,8,1,8,5,8,107,
        8,8,10,8,12,8,110,9,8,1,8,1,8,1,9,1,9,5,9,116,8,9,10,9,12,9,119,
        9,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,6,7,2,0,
        2,2,4,4,2,0,2,2,8,8,132,0,20,1,0,0,0,2,33,1,0,0,0,4,43,1,0,0,0,6,
        46,1,0,0,0,8,81,1,0,0,0,10,83,1,0,0,0,12,92,1,0,0,0,14,94,1,0,0,
        0,16,103,1,0,0,0,18,113,1,0,0,0,20,25,3,2,1,0,21,22,5,5,0,0,22,24,
        3,2,1,0,23,21,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,29,1,0,0,0,27,25,1,0,0,0,28,30,5,5,0,0,29,28,1,0,0,0,29,30,1,
        0,0,0,30,1,1,0,0,0,31,34,3,4,2,0,32,34,3,6,3,0,33,31,1,0,0,0,33,
        32,1,0,0,0,34,3,1,0,0,0,35,36,3,6,3,0,36,37,5,9,0,0,37,38,3,4,2,
        0,38,44,1,0,0,0,39,40,3,6,3,0,40,41,5,9,0,0,41,42,3,6,3,0,42,44,
        1,0,0,0,43,35,1,0,0,0,43,39,1,0,0,0,44,5,1,0,0,0,45,47,5,10,0,0,
        46,45,1,0,0,0,46,47,1,0,0,0,47,54,1,0,0,0,48,50,3,10,5,0,49,51,5,
        10,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,0,52,48,1,0,0,0,53,
        56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,
        0,57,64,3,8,4,0,58,60,5,10,0,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,
        1,0,0,0,61,63,3,8,4,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,
        64,65,1,0,0,0,65,73,1,0,0,0,66,64,1,0,0,0,67,69,5,10,0,0,68,67,1,
        0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,72,3,10,5,0,71,68,1,0,0,0,72,
        75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,
        0,76,78,5,10,0,0,77,76,1,0,0,0,77,78,1,0,0,0,78,7,1,0,0,0,79,82,
        3,12,6,0,80,82,5,1,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,9,1,0,0,0,
        83,85,7,0,0,0,84,86,5,10,0,0,85,84,1,0,0,0,85,86,1,0,0,0,86,87,1,
        0,0,0,87,88,3,8,4,0,88,11,1,0,0,0,89,93,3,14,7,0,90,93,3,16,8,0,
        91,93,3,18,9,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,13,1,
        0,0,0,94,98,5,4,0,0,95,97,8,1,0,0,96,95,1,0,0,0,97,100,1,0,0,0,98,
        96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,5,
        4,0,0,102,15,1,0,0,0,103,108,5,3,0,0,104,107,3,18,9,0,105,107,8,
        2,0,0,106,104,1,0,0,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,
        0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,
        3,0,0,112,17,1,0,0,0,113,117,5,8,0,0,114,116,8,2,0,0,115,114,1,0,
        0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,
        0,0,119,117,1,0,0,0,120,121,5,8,0,0,121,19,1,0,0,0,19,25,29,33,43,
        46,50,54,59,64,68,73,77,81,85,92,98,106,108,117
    ]

class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'\\n'", "'\"'", "'''", "';'", 
                     "'<'", "'>'", "'`'", "'|'" ]

    symbolicNames = [ "<INVALID>", "UNQUOTED", "NEWLINE", "DOUBLE_QUOTE", 
                      "SINGLE_QUOTE", "SEMI", "LT", "GT", "BACKTICK", "PIPE", 
                      "WHITESPACE" ]

    RULE_command = 0
    RULE_subCommand = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_argument = 4
    RULE_redirection = 5
    RULE_quoted = 6
    RULE_singleQuoted = 7
    RULE_doubleQuoted = 8
    RULE_backQuoted = 9

    ruleNames =  [ "command", "subCommand", "pipe", "call", "argument", 
                   "redirection", "quoted", "singleQuoted", "doubleQuoted", 
                   "backQuoted" ]

    EOF = Token.EOF
    UNQUOTED=1
    NEWLINE=2
    DOUBLE_QUOTE=3
    SINGLE_QUOTE=4
    SEMI=5
    LT=6
    GT=7
    BACKTICK=8
    PIPE=9
    WHITESPACE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.SubCommandContext)
            else:
                return self.getTypedRuleContext(CommandParser.SubCommandContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.SEMI)
            else:
                return self.getToken(CommandParser.SEMI, i)

        def getRuleIndex(self):
            return CommandParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = CommandParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.subCommand()
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self.match(CommandParser.SEMI)
                    self.state = 22
                    self.subCommand() 
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 28
                self.match(CommandParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(CommandParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_subCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubCommand" ):
                listener.enterSubCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubCommand" ):
                listener.exitSubCommand(self)




    def subCommand(self):

        localctx = CommandParser.SubCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subCommand)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.CallContext)
            else:
                return self.getTypedRuleContext(CommandParser.CallContext,i)


        def PIPE(self):
            return self.getToken(CommandParser.PIPE, 0)

        def pipe(self):
            return self.getTypedRuleContext(CommandParser.PipeContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_pipe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPipe" ):
                listener.enterPipe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPipe" ):
                listener.exitPipe(self)




    def pipe(self):

        localctx = CommandParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pipe)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.call()
                self.state = 36
                self.match(CommandParser.PIPE)
                self.state = 37
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.call()
                self.state = 40
                self.match(CommandParser.PIPE)
                self.state = 41
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(CommandParser.ArgumentContext,i)


        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.WHITESPACE)
            else:
                return self.getToken(CommandParser.WHITESPACE, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandParser.RedirectionContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = CommandParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 45
                self.match(CommandParser.WHITESPACE)


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 48
                self.redirection()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 49
                    self.match(CommandParser.WHITESPACE)


                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.argument()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 58
                        self.match(CommandParser.WHITESPACE)


                    self.state = 61
                    self.argument() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==10:
                        self.state = 67
                        self.match(CommandParser.WHITESPACE)


                    self.state = 70
                    self.redirection() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 76
                self.match(CommandParser.WHITESPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self):
            return self.getTypedRuleContext(CommandParser.QuotedContext,0)


        def UNQUOTED(self):
            return self.getToken(CommandParser.UNQUOTED, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = CommandParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 8]:
                self.state = 79
                self.quoted()
                pass
            elif token in [1]:
                self.state = 80
                self.match(CommandParser.UNQUOTED)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def LT(self):
            return self.getToken(CommandParser.LT, 0)

        def GT(self):
            return self.getToken(CommandParser.GT, 0)

        def WHITESPACE(self):
            return self.getToken(CommandParser.WHITESPACE, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_redirection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRedirection" ):
                listener.enterRedirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRedirection" ):
                listener.exitRedirection(self)




    def redirection(self):

        localctx = CommandParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 84
                self.match(CommandParser.WHITESPACE)


            self.state = 87
            self.argument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(CommandParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(CommandParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuoted" ):
                listener.enterQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuoted" ):
                listener.exitQuoted(self)




    def quoted(self):

        localctx = CommandParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_quoted)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.singleQuoted()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.doubleQuoted()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.backQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.SINGLE_QUOTE)
            else:
                return self.getToken(CommandParser.SINGLE_QUOTE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.NEWLINE)
            else:
                return self.getToken(CommandParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandParser.RULE_singleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuoted" ):
                listener.enterSingleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuoted" ):
                listener.exitSingleQuoted(self)




    def singleQuoted(self):

        localctx = CommandParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(CommandParser.SINGLE_QUOTE)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 2026) != 0:
                self.state = 95
                _la = self._input.LA(1)
                if _la <= 0 or _la==2 or _la==4:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(CommandParser.SINGLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.DOUBLE_QUOTE)
            else:
                return self.getToken(CommandParser.DOUBLE_QUOTE, i)

        def backQuoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.BackQuotedContext)
            else:
                return self.getTypedRuleContext(CommandParser.BackQuotedContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.NEWLINE)
            else:
                return self.getToken(CommandParser.NEWLINE, i)

        def BACKTICK(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.BACKTICK)
            else:
                return self.getToken(CommandParser.BACKTICK, i)

        def getRuleIndex(self):
            return CommandParser.RULE_doubleQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleQuoted" ):
                listener.enterDoubleQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleQuoted" ):
                listener.exitDoubleQuoted(self)




    def doubleQuoted(self):

        localctx = CommandParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CommandParser.DOUBLE_QUOTE)
            self.state = 108
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 106
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [8]:
                        self.state = 104
                        self.backQuoted()
                        pass
                    elif token in [1, 3, 4, 5, 6, 7, 9, 10]:
                        self.state = 105
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==2 or _la==8:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 110
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 111
            self.match(CommandParser.DOUBLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKTICK(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.BACKTICK)
            else:
                return self.getToken(CommandParser.BACKTICK, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.NEWLINE)
            else:
                return self.getToken(CommandParser.NEWLINE, i)

        def getRuleIndex(self):
            return CommandParser.RULE_backQuoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackQuoted" ):
                listener.enterBackQuoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackQuoted" ):
                listener.exitBackQuoted(self)




    def backQuoted(self):

        localctx = CommandParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_backQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CommandParser.BACKTICK)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1786) != 0:
                self.state = 114
                _la = self._input.LA(1)
                if _la <= 0 or _la==2 or _la==8:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(CommandParser.BACKTICK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





