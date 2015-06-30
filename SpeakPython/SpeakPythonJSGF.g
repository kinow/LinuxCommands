/*
#SpeakPython allows developers to add speech recognition support to their Python applications
#Copyright (C) 2015  Eric Matthews

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by 
#the Free Software Foundation, either version 3 of the License, or 
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of 
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

grammar SpeakPythonJSGF;

options
{
	language=Python;
}

@members
{
optionVals = {};
optionValsBackup = optionVals;

rules = [];
aliasRules = {};

parseFailed = False;
}

prog
@init
{
self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
self.optionVals['wordDelim'] = '[ ,/]+';
}
	: s (NEWLINE | WHITE_SPACE)* EOF {}
	;

s
@init
{
}
	: (WHITE_SPACE | NEWLINE)* mat { self.rules.append($mat.matR); } s 
	| (WHITE_SPACE | NEWLINE)* alias { } s 
	| (WHITE_SPACE | NEWLINE)* globalOptions s
	| {}
	;

globalOptions
	: AT_GLOBAL_OPTIONS myOptions AT
	;

localOptions
	: AT_OPTIONS { self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); } myOptions AT
	;

myOptions
	: (WHITE_SPACE | NEWLINE)* myOption myOptions
	| (WHITE_SPACE | NEWLINE)* {}
	;

myOption
	: WORD (WHITE_SPACE | NEWLINE)* EQ (RA_BR)? (WHITE_SPACE | NEWLINE)* REGEX (SEMI)? { self.optionVals[$WORD.text] = $REGEX.text[1:-2]; }
	| WORD (WHITE_SPACE | NEWLINE)* EQ (RA_BR)? (WHITE_SPACE | NEWLINE)* DEFAULT (SEMI)? { self.optionVals[$WORD.text] = self.defaultOptionVals[$WORD.text]; }
	;

/*Returns a Match() object*/
mat returns [matR]
@init
{
}
	: (localOptions (WHITE_SPACE | NEWLINE)*)? exps
			{ self.optionVals = self.optionValsBackup; }
		statementFields
			{ $matR = $exps.expsR; }
	;

statementFields
	: (WHITE_SPACE | NEWLINE)* AT_RESULTS mResults AT statementFields
		{ }
	| (WHITE_SPACE | NEWLINE)* AT_TESTS testCases AT statementFields
		{ }
	| {}
	;

alias returns [aliasR]
	: HASH_NAME LR_BR WHITE_SPACE* RR_BR WHITE_SPACE* EQ WHITE_SPACE* exps statementFields
		{ self.aliasRules[$HASH_NAME.text[1:]] = $exps.expsR; }
	;

exps returns [expsR='']
	: expVal SEMI { $expsR = $expVal.expValR + ";"; }
	;

//returns an expression derivative
expVal returns [expValR='']
	: LS_BR e1=expVal RS_BR opt subExp
			{ $expValR = $opt.optR[0] + $e1.expValR + $opt.optR[1] + $subExp.subExpR; }

	| LR_BR e2=expVal RR_BR opt subExp
			{ $expValR = $opt.optR[0] + $e2.expValR + $opt.optR[1] + $subExp.subExpR; }

	| w1=WORD subExp
			{ $expValR = $w1.text + $subExp.subExpR; }

	| VAR_NAME subExp
			{ print "We're sorry, variables are not supported in JSGF at this time."; self.parseFailed = True; $expValR = $subExp.subExpR; }

	| HASH_NAME subExp
			{ name = $HASH_NAME.text[1:]; }
			{ if (name not in self.aliasRules): print "The rule <" + name + "> does not exist before it is referenced."; }
			{ $expValR = "<" + name + ">" + $subExp.subExpR; }

	| REGEX	subExp
			{ print "We're sorry, regex is not supported in JSGF at this time."; $expValR = ""; }
	;

//this subExp handles OR properly so that we can't have OR OR OR expVal
subExp returns [subExpR='']
	: WHITE_SPACE* expVal
			{ $subExpR = " " + $expVal.expValR; }
	| WHITE_SPACE* OR WHITE_SPACE* expVal { $subExpR = " | " + $expVal.expValR; }
	| {}
	; 

//returns a prefix, and a suffix to attach to the expression
opt returns [optR=('(',')')]
	: QSTN { $optR=("[", "]"); }
	| STAR { $optR=("(", ")*"); }
	| PLUS { $optR=("(", ")+"); }
	| {}
	;

testCases returns [testCasesR=[\]]
	: (NEWLINE | WHITE_SPACE)* testCase ts=testCases
			{ }
	| (NEWLINE | WHITE_SPACE)* {}
	;

testCase returns [testCaseR='']
	: q1=QUOTE_STRING (WHITE_SPACE | NEWLINE)* EQ (RA_BR)? (WHITE_SPACE | NEWLINE)* q2=QUOTE_STRING { }
	| q3=QUOTE_STRING
		{ }
	;

/*Returns a list of Result() objects*/
mResults
	: NEWLINE* m1=mResult ms=mResults { }
	| NEWLINE* { }
	;

/*Returns a Result() object*/
mResult
	: ls=labels LC_BR results RC_BR { }
	;

/*Returns a list of numeric labels*/
labels
	: l1=label labelsRest { }
	| l2=label { }
	;

labelsRest
	: COMMA labels { }
	;
	
/*Returns a numeric label*/
label
	: WHITE_SPACE* NUM WHITE_SPACE* { }
	| WHITE_SPACE* HASH_NAME WHITE_SPACE* { }
	| WHITE_SPACE* KLEENE NUM WHITE_SPACE* { }
	| WHITE_SPACE* WORD NUM WHITE_SPACE* { }
	| WHITE_SPACE* WORD WHITE_SPACE* { }
	;

//Parse result list
results
	: WHITE_SPACE* result rs=results { }
	| WHITE_SPACE* { }
	;

result
	: QUOTE_STRING { }
	| VAR_NAME { }
	| HASH_NAME { }
	| KLEENE NUM LA_BR r1=results RA_BR LR_BR r2=results RR_BR { }
	;

NEWLINE: ('\r')?'\n';

REGEX: '/'.+'/r';
COMMENT: '//' ~('\r'|'\n')* NEWLINE { self.skip(); };

QSTN: '?';
TILDE: '~';
B_ARROW: '<-';
ARROW: '->';
ELIPSE: '...';
LS_BR: '[';
LC_BR: '{';
RC_BR: '}';
RS_BR: ']';
LR_BR: '(';
RR_BR: ')';
LA_BR: '<';
RA_BR: '>';
OR: '|';
COMMA: ',';
SEMI: ';';
EQ: '=';
AT_TESTS: '@tests';
AT_RESULTS: '@results';
AT_GLOBAL_OPTIONS: '@globalOptions';
AT_OPTIONS: '@options';
DEFAULT: 'default';
AT: '@';
PLUS: '+';
STAR: '*';
KLEENE: 'k_';

VAR_NAME: '$'('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z')*;
HASH_NAME: '#'('a'..'z'|'A'..'Z')('a'..'z'|'A'..'Z'|'0'..'9')*;
QUOTE_STRING: ('"'.+'"')|('\''.+'\'');
NUM: ('0'..'9')+;
WORD: ('a'..'z'|'A'..'Z')+;
WHITE_SPACE: ' '|'\t';
