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
        4,1,22,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,5,0,28,
        8,0,10,0,12,0,31,9,0,1,0,3,0,34,8,0,1,1,1,1,3,1,38,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,5,3,51,8,3,10,3,12,3,54,9,3,
        1,3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,4,1,4,3,4,65,8,4,1,5,1,5,4,
        5,69,8,5,11,5,12,5,70,1,6,1,6,1,6,1,6,3,6,77,8,6,1,7,1,7,1,7,3,7,
        82,8,7,1,8,1,8,5,8,86,8,8,10,8,12,8,89,9,8,1,8,1,8,1,9,1,9,5,9,95,
        8,9,10,9,12,9,98,9,9,1,9,1,9,1,10,1,10,1,10,5,10,105,8,10,10,10,
        12,10,108,9,10,1,10,1,10,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,
        16,18,20,22,0,4,1,0,15,16,2,0,15,15,17,17,2,0,15,15,17,18,2,0,13,
        18,20,21,117,0,24,1,0,0,0,2,37,1,0,0,0,4,47,1,0,0,0,6,52,1,0,0,0,
        8,64,1,0,0,0,10,68,1,0,0,0,12,76,1,0,0,0,14,81,1,0,0,0,16,83,1,0,
        0,0,18,92,1,0,0,0,20,101,1,0,0,0,22,111,1,0,0,0,24,29,3,2,1,0,25,
        26,5,14,0,0,26,28,3,2,1,0,27,25,1,0,0,0,28,31,1,0,0,0,29,27,1,0,
        0,0,29,30,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,32,34,5,14,0,0,33,
        32,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,0,35,38,3,4,2,0,36,38,3,6,3,
        0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,3,6,3,0,40,41,5,
        13,0,0,41,42,3,4,2,0,42,48,1,0,0,0,43,44,3,6,3,0,44,45,5,13,0,0,
        45,46,3,6,3,0,46,48,1,0,0,0,47,39,1,0,0,0,47,43,1,0,0,0,48,5,1,0,
        0,0,49,51,3,12,6,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,
        53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,59,3,10,5,0,56,58,3,8,
        4,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,7,
        1,0,0,0,61,59,1,0,0,0,62,65,3,12,6,0,63,65,3,10,5,0,64,62,1,0,0,
        0,64,63,1,0,0,0,65,9,1,0,0,0,66,69,3,14,7,0,67,69,3,22,11,0,68,66,
        1,0,0,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,
        71,11,1,0,0,0,72,73,5,21,0,0,73,77,3,10,5,0,74,75,5,20,0,0,75,77,
        3,10,5,0,76,72,1,0,0,0,76,74,1,0,0,0,77,13,1,0,0,0,78,82,3,16,8,
        0,79,82,3,20,10,0,80,82,3,18,9,0,81,78,1,0,0,0,81,79,1,0,0,0,81,
        80,1,0,0,0,82,15,1,0,0,0,83,87,5,16,0,0,84,86,8,0,0,0,85,84,1,0,
        0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,
        1,0,0,0,90,91,5,16,0,0,91,17,1,0,0,0,92,96,5,18,0,0,93,95,8,1,0,
        0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,
        1,0,0,0,98,96,1,0,0,0,99,100,5,18,0,0,100,19,1,0,0,0,101,106,5,17,
        0,0,102,105,3,18,9,0,103,105,8,2,0,0,104,102,1,0,0,0,104,103,1,0,
        0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,109,1,0,
        0,0,108,106,1,0,0,0,109,110,5,17,0,0,110,21,1,0,0,0,111,112,8,3,
        0,0,112,23,1,0,0,0,15,29,33,37,47,52,59,64,68,70,76,81,87,96,104,
        106
    ]

class CommandParser ( Parser ):

    grammarFileName = "Command.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'cat'", "'cd'", "'cut'", "'echo'", "'find'", 
                     "'grep'", "'head'", "'tail'", "'ls'", "'pwd'", "'sort'", 
                     "'uniq'", "'|'", "';'", "'\\n'", "'''", "'\"'", "'`'", 
                     "'_'", "'>'", "'<'", "' '" ]

    symbolicNames = [ "<INVALID>", "CAT", "CD", "CUT", "ECHO", "FIND", "GREP", 
                      "HEAD", "TAIL", "LS", "PWD", "SORT", "UNIQ", "PIPE", 
                      "SEMI", "NEWLINE", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "BACKTICK", "UNDERSCORE", "GT", "LT", "WHITESPACE" ]

    RULE_command = 0
    RULE_sub_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_redirection = 6
    RULE_quoted = 7
    RULE_singleQuoted = 8
    RULE_backquoted = 9
    RULE_doubleQuoted = 10
    RULE_unquoted = 11

    ruleNames =  [ "command", "sub_command", "pipe", "call", "atom", "argument", 
                   "redirection", "quoted", "singleQuoted", "backquoted", 
                   "doubleQuoted", "unquoted" ]

    EOF = Token.EOF
    CAT=1
    CD=2
    CUT=3
    ECHO=4
    FIND=5
    GREP=6
    HEAD=7
    TAIL=8
    LS=9
    PWD=10
    SORT=11
    UNIQ=12
    PIPE=13
    SEMI=14
    NEWLINE=15
    SINGLE_QUOTE=16
    DOUBLE_QUOTE=17
    BACKTICK=18
    UNDERSCORE=19
    GT=20
    LT=21
    WHITESPACE=22

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

        def sub_command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.Sub_commandContext)
            else:
                return self.getTypedRuleContext(CommandParser.Sub_commandContext,i)


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
            self.state = 24
            self.sub_command()
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 25
                    self.match(CommandParser.SEMI)
                    self.state = 26
                    self.sub_command() 
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 32
                self.match(CommandParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_commandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pipe(self):
            return self.getTypedRuleContext(CommandParser.PipeContext,0)


        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_sub_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_command" ):
                listener.enterSub_command(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_command" ):
                listener.exitSub_command(self)




    def sub_command(self):

        localctx = CommandParser.Sub_commandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sub_command)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
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
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.call()
                self.state = 40
                self.match(CommandParser.PIPE)
                self.state = 41
                self.pipe()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.call()
                self.state = 44
                self.match(CommandParser.PIPE)
                self.state = 45
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

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.AtomContext)
            else:
                return self.getTypedRuleContext(CommandParser.AtomContext,i)


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
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 49
                self.redirection()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.argument()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8331262) != 0:
                self.state = 56
                self.atom()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(CommandParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CommandParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.redirection()
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.argument()
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


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.QuotedContext)
            else:
                return self.getTypedRuleContext(CommandParser.QuotedContext,i)


        def unquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.UnquotedContext)
            else:
                return self.getTypedRuleContext(CommandParser.UnquotedContext,i)


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
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 68
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [16, 17, 18]:
                        self.state = 66
                        self.quoted()
                        pass
                    elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 22]:
                        self.state = 67
                        self.unquoted()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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

        def LT(self):
            return self.getToken(CommandParser.LT, 0)

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def GT(self):
            return self.getToken(CommandParser.GT, 0)

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
        self.enterRule(localctx, 12, self.RULE_redirection)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(CommandParser.LT)
                self.state = 73
                self.argument()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(CommandParser.GT)
                self.state = 75
                self.argument()
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


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(CommandParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandParser.DoubleQuotedContext,0)


        def backquoted(self):
            return self.getTypedRuleContext(CommandParser.BackquotedContext,0)


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
        self.enterRule(localctx, 14, self.RULE_quoted)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.singleQuoted()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.doubleQuoted()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.backquoted()
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
        self.enterRule(localctx, 16, self.RULE_singleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(CommandParser.SINGLE_QUOTE)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8290302) != 0:
                self.state = 84
                _la = self._input.LA(1)
                if _la <= 0 or _la==15 or _la==16:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(CommandParser.SINGLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackquotedContext(ParserRuleContext):
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

        def DOUBLE_QUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.DOUBLE_QUOTE)
            else:
                return self.getToken(CommandParser.DOUBLE_QUOTE, i)

        def getRuleIndex(self):
            return CommandParser.RULE_backquoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackquoted" ):
                listener.enterBackquoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackquoted" ):
                listener.exitBackquoted(self)




    def backquoted(self):

        localctx = CommandParser.BackquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_backquoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CommandParser.BACKTICK)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==15 or _la==17:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 99
            self.match(CommandParser.BACKTICK)
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

        def backquoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.BackquotedContext)
            else:
                return self.getTypedRuleContext(CommandParser.BackquotedContext,i)


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
        self.enterRule(localctx, 20, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(CommandParser.DOUBLE_QUOTE)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 8224766) != 0:
                self.state = 104
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 102
                    self.backquoted()
                    pass
                elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 19, 20, 21, 22]:
                    self.state = 103
                    _la = self._input.LA(1)
                    if _la <= 0 or ((_la) & ~0x3f) == 0 and ((1 << _la) & 425984) != 0:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 109
            self.match(CommandParser.DOUBLE_QUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnquotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINGLE_QUOTE(self):
            return self.getToken(CommandParser.SINGLE_QUOTE, 0)

        def DOUBLE_QUOTE(self):
            return self.getToken(CommandParser.DOUBLE_QUOTE, 0)

        def BACKTICK(self):
            return self.getToken(CommandParser.BACKTICK, 0)

        def NEWLINE(self):
            return self.getToken(CommandParser.NEWLINE, 0)

        def SEMI(self):
            return self.getToken(CommandParser.SEMI, 0)

        def PIPE(self):
            return self.getToken(CommandParser.PIPE, 0)

        def LT(self):
            return self.getToken(CommandParser.LT, 0)

        def GT(self):
            return self.getToken(CommandParser.GT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_unquoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnquoted" ):
                listener.enterUnquoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnquoted" ):
                listener.exitUnquoted(self)




    def unquoted(self):

        localctx = CommandParser.UnquotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unquoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if _la <= 0 or ((_la) & ~0x3f) == 0 and ((1 << _la) & 3661824) != 0:
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





