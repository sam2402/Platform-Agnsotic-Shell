grammar Command;

/*
 * Parser Rules
 */
command: subCommand (SEMI subCommand)* SEMI?;
subCommand: pipe | call;
pipe: (call PIPE pipe) | (call PIPE call);

call: WHITESPACE? (redirection WHITESPACE?)* argument (WHITESPACE? argument)* (WHITESPACE? redirection)* WHITESPACE?;
argument: (quoted | UNQUOTED);
redirection: (LT | GT) WHITESPACE? argument;

quoted: singleQuoted | doubleQuoted | backQuoted;
singleQuoted: SINGLE_QUOTE ~(NEWLINE | SINGLE_QUOTE)* SINGLE_QUOTE;
doubleQuoted: DOUBLE_QUOTE (backQuoted | ~(NEWLINE | BACKTICK))* DOUBLE_QUOTE;
backQuoted: BACKTICK ~(NEWLINE | BACKTICK)* BACKTICK;

/*
 * Lexer Rules
 */
UNQUOTED: ~[\t\n "';<>`|]+;

NEWLINE: '\n';
DOUBLE_QUOTE: '"';
SINGLE_QUOTE: '\'';
SEMI: ';';
LT: '<';
GT: '>';
BACKTICK: '`';
PIPE: '|';

WHITESPACE: [\t ]+;
