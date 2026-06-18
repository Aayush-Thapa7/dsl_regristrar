grammar Registrar;

// Parser Rules
prog: stat+ EOF ;

stat: enrollCmd
    | dropCmd
    | payCmd
    | grantCmd
    | showCmd
    | resetCmd
    ;

enrollCmd: ENROLL STUDENT ID NAME STRING MAJOR STRING ;
dropCmd: DROP STUDENT ID ;
payCmd: PAY FEE ID AMOUNT NUMBER ;
grantCmd: GRANT SCHOLARSHIP ID AMOUNT NUMBER ;
showCmd: SHOW (STUDENT ID | ALL STUDENTS | REVENUE) ;
resetCmd: RESET ;

// Lexer Rules
ENROLL: 'ENROLL' ;
STUDENT: 'STUDENT' ;
NAME: 'NAME' ;
MAJOR: 'MAJOR' ;
DROP: 'DROP' ;
PAY: 'PAY' ;
FEE: 'FEE' ;
AMOUNT: 'AMOUNT' ;
GRANT: 'GRANT' ;
SCHOLARSHIP: 'SCHOLARSHIP' ;
SHOW: 'SHOW' ;
ALL: 'ALL' ;
STUDENTS: 'STUDENTS' ;
REVENUE: 'REVENUE' ;
RESET: 'RESET' ;

ID: [0-9]+ ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
STRING: '"' ~'"'* '"' ;
WS: [ \t\r\n]+ -> skip ;
