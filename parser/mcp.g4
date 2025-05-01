grammar MCP;

prog: statement* EOF;

statement
    : modelDecl
    | contextDecl
    | interactionDecl
    ;

modelDecl
    : 'model' IDENTIFIER '{' modelField* '}'
    ;

modelField
    : 'input:' IDENTIFIER ':' typename
    | 'output:' IDENTIFIER ':' typename
    ;

contextDecl
    : 'context' IDENTIFIER '{' contextField* '}'
    ;

contextField
    : IDENTIFIER ':' typename
    ;

interactionDecl
    : 'interaction' IDENTIFIER '(' argList? ')' '->' IDENTIFIER '{' interactionBody* '}'
    ;

argList
    : argument (',' argument)*
    ;

argument
    : IDENTIFIER ':' typename
    ;

interactionBody
    : useStmt
    | bindStmt
    ;

useStmt
    : 'use' IDENTIFIER
    ;

bindStmt
    : 'bind' path 'to' path
    ;

path
    : IDENTIFIER ('.' IDENTIFIER)*
    ;

typename
    : IDENTIFIER
    ;

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
