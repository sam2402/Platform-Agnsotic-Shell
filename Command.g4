/*
 * Parser Rules
 */
grammar Command;

command: sub_command (SEMI sub_command)* SEMI?;
sub_command: pipe | call;
pipe: (call PIPE pipe) | (call PIPE call);

call: redirection* argument atom*;
atom: redirection | argument;
argument: (quoted | unquoted)+;
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

unquoted:
	~(
		SINGLE_QUOTE
		| DOUBLE_QUOTE
		| BACKTICK
		| NEWLINE
		| SEMI
		| PIPE
		| LT
		| GT
	);

/*
 * Lexer Rules
 */

CAT: 'cat';
CD: 'cd';
CUT: 'cut';
ECHO: 'echo';
FIND: 'find';
GREP: 'grep';
HEAD: 'head';
TAIL: 'tail';
LS: 'ls';
PWD: 'pwd';
SORT: 'sort';
UNIQ: 'uniq';

PIPE: '|';
SEMI: ';';
NEWLINE: '\n';
SINGLE_QUOTE: '\'';
DOUBLE_QUOTE: '"';
BACKTICK: '`';
UNDERSCORE: '_';
GT: '>';
LT: '<';
WHITESPACE: ' ' -> skip;