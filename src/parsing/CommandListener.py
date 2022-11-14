# Generated from Command.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete listener for a parse tree produced by CommandParser.
class CommandListener(ParseTreeListener):

    # Enter a parse tree produced by CommandParser#command.
    def enterCommand(self, ctx:CommandParser.CommandContext):
        pass

    # Exit a parse tree produced by CommandParser#command.
    def exitCommand(self, ctx:CommandParser.CommandContext):
        pass


    # Enter a parse tree produced by CommandParser#sub_command.
    def enterSub_command(self, ctx:CommandParser.Sub_commandContext):
        pass

    # Exit a parse tree produced by CommandParser#sub_command.
    def exitSub_command(self, ctx:CommandParser.Sub_commandContext):
        pass


    # Enter a parse tree produced by CommandParser#pipe.
    def enterPipe(self, ctx:CommandParser.PipeContext):
        pass

    # Exit a parse tree produced by CommandParser#pipe.
    def exitPipe(self, ctx:CommandParser.PipeContext):
        pass


    # Enter a parse tree produced by CommandParser#call.
    def enterCall(self, ctx:CommandParser.CallContext):
        pass

    # Exit a parse tree produced by CommandParser#call.
    def exitCall(self, ctx:CommandParser.CallContext):
        pass


    # Enter a parse tree produced by CommandParser#atom.
    def enterAtom(self, ctx:CommandParser.AtomContext):
        pass

    # Exit a parse tree produced by CommandParser#atom.
    def exitAtom(self, ctx:CommandParser.AtomContext):
        pass


    # Enter a parse tree produced by CommandParser#argument.
    def enterArgument(self, ctx:CommandParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CommandParser#argument.
    def exitArgument(self, ctx:CommandParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CommandParser#redirection.
    def enterRedirection(self, ctx:CommandParser.RedirectionContext):
        pass

    # Exit a parse tree produced by CommandParser#redirection.
    def exitRedirection(self, ctx:CommandParser.RedirectionContext):
        pass


    # Enter a parse tree produced by CommandParser#quoted.
    def enterQuoted(self, ctx:CommandParser.QuotedContext):
        pass

    # Exit a parse tree produced by CommandParser#quoted.
    def exitQuoted(self, ctx:CommandParser.QuotedContext):
        pass


    # Enter a parse tree produced by CommandParser#singleQuoted.
    def enterSingleQuoted(self, ctx:CommandParser.SingleQuotedContext):
        pass

    # Exit a parse tree produced by CommandParser#singleQuoted.
    def exitSingleQuoted(self, ctx:CommandParser.SingleQuotedContext):
        pass


    # Enter a parse tree produced by CommandParser#backquoted.
    def enterBackquoted(self, ctx:CommandParser.BackquotedContext):
        pass

    # Exit a parse tree produced by CommandParser#backquoted.
    def exitBackquoted(self, ctx:CommandParser.BackquotedContext):
        pass


    # Enter a parse tree produced by CommandParser#doubleQuoted.
    def enterDoubleQuoted(self, ctx:CommandParser.DoubleQuotedContext):
        pass

    # Exit a parse tree produced by CommandParser#doubleQuoted.
    def exitDoubleQuoted(self, ctx:CommandParser.DoubleQuotedContext):
        pass


    # Enter a parse tree produced by CommandParser#unquoted.
    def enterUnquoted(self, ctx:CommandParser.UnquotedContext):
        pass

    # Exit a parse tree produced by CommandParser#unquoted.
    def exitUnquoted(self, ctx:CommandParser.UnquotedContext):
        pass



del CommandParser