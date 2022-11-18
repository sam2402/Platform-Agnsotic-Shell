/*
 * Parser Rules
 */
grammar Command;

command: sub_command (SEMI sub_command)* SEMI?;
sub_command: pipe | call;
pipe: (call PIPE pipe) | (call PIPE call);

call: redirection* argument atom*;
atom: redirection | argument+;
argument: (quoted | UNQUOTED);
redirection: (LT argument) | (GT argument);

quoted: singleQuoted | doubleQuoted | backquoted;
singleQuoted:
	SINGLE_QUOTE ~(NEWLINE | SINGLE_QUOTE)* SINGLE_QUOTE;
backquoted: BACKTICK ~(NEWLINE | DOUBLE_QUOTE)* BACKTICK;
doubleQuoted:
	DOUBLE_QUOTE (
		backquoted
		| ~(NEWLINE | DOUBLE_QUOTE | BACKTICK)
	)* DOUBLE_QUOTE;

/*
 * Lexer Rules
 */

UNQUOTED: [!#$%&()*+,-./0-9:=?@A-Z[\]^_a-z{}~]+; // ascii without  ['"`\n;<>]

PIPE: '|';
SEMI: ';';
NEWLINE: '\n';
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"';
BACKTICK: '`';
UNDERSCORE: '_';
GT: '>';
LT: '<';
WHITESPACE: (' ' | '\t') -> skip;
