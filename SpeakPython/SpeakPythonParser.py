# $ANTLR 3.4 SpeakPython.g 2015-06-16 19:11:42

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


import re;
sub = re.sub;
from Match import Match;
from Match import GroupCounter;
from Result import Result;
from StringResult import StringResult;
from VarResult import VarResult;
from FunctionResult import FunctionResult;
from KleeneResult import KleeneResult;
from Function import Function;



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
ARROW=4
AT=5
AT_GLOBAL_OPTIONS=6
AT_OPTIONS=7
AT_RESULTS=8
AT_TESTS=9
B_ARROW=10
COMMA=11
COMMENT=12
DEFAULT=13
ELIPSE=14
EQ=15
HASH_NAME=16
KLEENE=17
LA_BR=18
LC_BR=19
LR_BR=20
LS_BR=21
NEWLINE=22
NUM=23
OR=24
PLUS=25
QSTN=26
QUOTE_STRING=27
RA_BR=28
RC_BR=29
REGEX=30
RR_BR=31
RS_BR=32
SEMI=33
STAR=34
TILDE=35
VAR_NAME=36
WHITE_SPACE=37
WORD=38

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "ARROW", "AT", "AT_GLOBAL_OPTIONS", "AT_OPTIONS", "AT_RESULTS", "AT_TESTS", 
    "B_ARROW", "COMMA", "COMMENT", "DEFAULT", "ELIPSE", "EQ", "HASH_NAME", 
    "KLEENE", "LA_BR", "LC_BR", "LR_BR", "LS_BR", "NEWLINE", "NUM", "OR", 
    "PLUS", "QSTN", "QUOTE_STRING", "RA_BR", "RC_BR", "REGEX", "RR_BR", 
    "RS_BR", "SEMI", "STAR", "TILDE", "VAR_NAME", "WHITE_SPACE", "WORD"
]




class SpeakPythonParser(Parser):
    grammarFileName = "SpeakPython.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SpeakPythonParser, self).__init__(input, state, *args, **kwargs)

        self.dfa5 = self.DFA5(
            self, 5,
            eot = self.DFA5_eot,
            eof = self.DFA5_eof,
            min = self.DFA5_min,
            max = self.DFA5_max,
            accept = self.DFA5_accept,
            special = self.DFA5_special,
            transition = self.DFA5_transition
            )

        self.dfa8 = self.DFA8(
            self, 8,
            eot = self.DFA8_eot,
            eof = self.DFA8_eof,
            min = self.DFA8_min,
            max = self.DFA8_max,
            accept = self.DFA8_accept,
            special = self.DFA8_special,
            transition = self.DFA8_transition
            )

        self.dfa17 = self.DFA17(
            self, 17,
            eot = self.DFA17_eot,
            eof = self.DFA17_eof,
            min = self.DFA17_min,
            max = self.DFA17_max,
            accept = self.DFA17_accept,
            special = self.DFA17_special,
            transition = self.DFA17_transition
            )

        self.dfa22 = self.DFA22(
            self, 22,
            eot = self.DFA22_eot,
            eof = self.DFA22_eof,
            min = self.DFA22_min,
            max = self.DFA22_max,
            accept = self.DFA22_accept,
            special = self.DFA22_special,
            transition = self.DFA22_transition
            )

        self.dfa30 = self.DFA30(
            self, 30,
            eot = self.DFA30_eot,
            eof = self.DFA30_eof,
            min = self.DFA30_min,
            max = self.DFA30_max,
            accept = self.DFA30_accept,
            special = self.DFA30_special,
            transition = self.DFA30_transition
            )

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
            )

        self.dfa38 = self.DFA38(
            self, 38,
            eot = self.DFA38_eot,
            eof = self.DFA38_eof,
            min = self.DFA38_min,
            max = self.DFA38_max,
            accept = self.DFA38_accept,
            special = self.DFA38_special,
            transition = self.DFA38_transition
            )

        self.dfa41 = self.DFA41(
            self, 41,
            eot = self.DFA41_eot,
            eof = self.DFA41_eof,
            min = self.DFA41_min,
            max = self.DFA41_max,
            accept = self.DFA41_accept,
            special = self.DFA41_special,
            transition = self.DFA41_transition
            )

        self.dfa42 = self.DFA42(
            self, 42,
            eot = self.DFA42_eot,
            eof = self.DFA42_eof,
            min = self.DFA42_min,
            max = self.DFA42_max,
            accept = self.DFA42_accept,
            special = self.DFA42_special,
            transition = self.DFA42_transition
            )

        self.dfa53 = self.DFA53(
            self, 53,
            eot = self.DFA53_eot,
            eof = self.DFA53_eof,
            min = self.DFA53_min,
            max = self.DFA53_max,
            accept = self.DFA53_accept,
            special = self.DFA53_special,
            transition = self.DFA53_transition
            )

        self.dfa56 = self.DFA56(
            self, 56,
            eot = self.DFA56_eot,
            eof = self.DFA56_eof,
            min = self.DFA56_min,
            max = self.DFA56_max,
            accept = self.DFA56_accept,
            special = self.DFA56_special,
            transition = self.DFA56_transition
            )




        self.delegates = []





    optionVals = {};
    optionValsBackup = optionVals;
    statementFieldDict = {};
    isKeyword = True;
    wordEncountered = False;
    finishedKeywords = False;
    globalTests = {};
    upCount = 0;
    matches = [];
    aliases = {};
    aliasWord = '';
    aliasUseCount = {};
    aliasKeywords = {}
    kGroupRegexes = {};
    isKleene = False;
    kGroupCount = 0;
    keywords = [];
    termNum = 0;



    # $ANTLR start "prog"
    # SpeakPython.g:65:1: prog : s ( NEWLINE | WHITE_SPACE )* EOF ;
    def prog(self, ):

        self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['wordDelim'] = '[ ,/]';
        self.defaultOptionVals = self.optionVals.copy();

        try:
            try:
                # SpeakPython.g:74:2: ( s ( NEWLINE | WHITE_SPACE )* EOF )
                # SpeakPython.g:74:4: s ( NEWLINE | WHITE_SPACE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_s_in_prog47)
                self.s()

                self._state.following.pop()

                # SpeakPython.g:74:6: ( NEWLINE | WHITE_SPACE )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE or LA1_0 == WHITE_SPACE) :
                        alt1 = 1


                    if alt1 == 1:
                        # SpeakPython.g:
                        pass 
                        if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                            self.input.consume()
                            self._state.errorRecovery = False


                        else:
                            if self._state.backtracking > 0:
                                raise BacktrackingFailed


                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop1


                self.match(self.input, EOF, self.FOLLOW_EOF_in_prog58)

                if self._state.backtracking == 0:
                    pass






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prog"



    # $ANTLR start "s"
    # SpeakPython.g:77:1: s : ( ( WHITE_SPACE | NEWLINE )* alias s | ( WHITE_SPACE | NEWLINE )* mat s | ( WHITE_SPACE | NEWLINE )* globalOptions s |);
    def s(self, ):
        alias1 = None

        mat2 = None



        self.statementFieldDict = {};
        self.statementFieldDict['testCases'] = [];
        self.statementFieldDict['results'] = [];
        self.upCount = 0;
        self.bracketCount = 0;
        self.wordEncountered = False;
        self.isKeyword = True;
        self.finishedKeywords = False;
        self.keywords = [];
        self.wordAtBracket = 0;
        self.kGroupCount = 0;
        self.isKleene = False;
        self.kGroupRegexes = {};
        self.aliasWord = '';
        aliasUseCount = {};

        try:
            try:
                # SpeakPython.g:99:2: ( ( WHITE_SPACE | NEWLINE )* alias s | ( WHITE_SPACE | NEWLINE )* mat s | ( WHITE_SPACE | NEWLINE )* globalOptions s |)
                alt5 = 4
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # SpeakPython.g:99:4: ( WHITE_SPACE | NEWLINE )* alias s
                    pass 
                    # SpeakPython.g:99:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == NEWLINE or LA2_0 == WHITE_SPACE) :
                            alt2 = 1


                        if alt2 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop2


                    self._state.following.append(self.FOLLOW_alias_in_s85)
                    alias1 = self.alias()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.aliases[self.aliasWord] = alias1; 



                    self._state.following.append(self.FOLLOW_s_in_s89)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 2:
                    # SpeakPython.g:100:4: ( WHITE_SPACE | NEWLINE )* mat s
                    pass 
                    # SpeakPython.g:100:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == NEWLINE or LA3_0 == WHITE_SPACE) :
                            alt3 = 1


                        if alt3 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop3


                    self._state.following.append(self.FOLLOW_mat_in_s104)
                    mat2 = self.mat()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.matches.append(mat2); 



                    self._state.following.append(self.FOLLOW_s_in_s108)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 3:
                    # SpeakPython.g:101:4: ( WHITE_SPACE | NEWLINE )* globalOptions s
                    pass 
                    # SpeakPython.g:101:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == NEWLINE or LA4_0 == WHITE_SPACE) :
                            alt4 = 1


                        if alt4 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop4


                    self._state.following.append(self.FOLLOW_globalOptions_in_s123)
                    self.globalOptions()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_s_in_s125)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 4:
                    # SpeakPython.g:102:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "s"



    # $ANTLR start "globalOptions"
    # SpeakPython.g:105:1: globalOptions : AT_GLOBAL_OPTIONS myOptions AT ;
    def globalOptions(self, ):
        try:
            try:
                # SpeakPython.g:106:2: ( AT_GLOBAL_OPTIONS myOptions AT )
                # SpeakPython.g:106:4: AT_GLOBAL_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_GLOBAL_OPTIONS, self.FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions141)

                self._state.following.append(self.FOLLOW_myOptions_in_globalOptions143)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_globalOptions145)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "globalOptions"



    # $ANTLR start "localOptions"
    # SpeakPython.g:109:1: localOptions : AT_OPTIONS myOptions AT ;
    def localOptions(self, ):
        try:
            try:
                # SpeakPython.g:110:2: ( AT_OPTIONS myOptions AT )
                # SpeakPython.g:110:4: AT_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_OPTIONS, self.FOLLOW_AT_OPTIONS_in_localOptions156)

                if self._state.backtracking == 0:
                    pass
                    self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); 



                self._state.following.append(self.FOLLOW_myOptions_in_localOptions160)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_localOptions162)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "localOptions"



    # $ANTLR start "myOptions"
    # SpeakPython.g:113:1: myOptions : ( ( WHITE_SPACE | NEWLINE )* myOption myOptions | ( WHITE_SPACE | NEWLINE )* );
    def myOptions(self, ):
        try:
            try:
                # SpeakPython.g:114:2: ( ( WHITE_SPACE | NEWLINE )* myOption myOptions | ( WHITE_SPACE | NEWLINE )* )
                alt8 = 2
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # SpeakPython.g:114:4: ( WHITE_SPACE | NEWLINE )* myOption myOptions
                    pass 
                    # SpeakPython.g:114:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == NEWLINE or LA6_0 == WHITE_SPACE) :
                            alt6 = 1


                        if alt6 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop6


                    self._state.following.append(self.FOLLOW_myOption_in_myOptions182)
                    self.myOption()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_myOptions_in_myOptions184)
                    self.myOptions()

                    self._state.following.pop()


                elif alt8 == 2:
                    # SpeakPython.g:115:4: ( WHITE_SPACE | NEWLINE )*
                    pass 
                    # SpeakPython.g:115:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == NEWLINE or LA7_0 == WHITE_SPACE) :
                            alt7 = 1


                        if alt7 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop7


                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOptions"



    # $ANTLR start "myOption"
    # SpeakPython.g:118:1: myOption : ( WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )? | WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )? );
    def myOption(self, ):
        WORD3 = None
        REGEX4 = None
        WORD5 = None

        try:
            try:
                # SpeakPython.g:119:2: ( WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )? | WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )? )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # SpeakPython.g:119:4: WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )?
                    pass 
                    WORD3 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption209)

                    # SpeakPython.g:119:9: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == NEWLINE or LA9_0 == WHITE_SPACE) :
                            alt9 = 1


                        if alt9 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop9


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption220)

                    # SpeakPython.g:119:37: ( RA_BR )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == RA_BR) :
                        alt10 = 1
                    if alt10 == 1:
                        # SpeakPython.g:119:38: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption223)




                    # SpeakPython.g:119:46: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == NEWLINE or LA11_0 == WHITE_SPACE) :
                            alt11 = 1


                        if alt11 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop11


                    REGEX4 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_myOption236)

                    # SpeakPython.g:119:77: ( SEMI )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == SEMI) :
                        alt12 = 1
                    if alt12 == 1:
                        # SpeakPython.g:119:78: SEMI
                        pass 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption239)




                    if self._state.backtracking == 0:
                        pass
                        self.optionVals[WORD3.text] = REGEX4.text[1:-2]; 




                elif alt17 == 2:
                    # SpeakPython.g:120:4: WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )?
                    pass 
                    WORD5 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption248)

                    # SpeakPython.g:120:9: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == NEWLINE or LA13_0 == WHITE_SPACE) :
                            alt13 = 1


                        if alt13 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop13


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption259)

                    # SpeakPython.g:120:37: ( RA_BR )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == RA_BR) :
                        alt14 = 1
                    if alt14 == 1:
                        # SpeakPython.g:120:38: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption262)




                    # SpeakPython.g:120:46: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == NEWLINE or LA15_0 == WHITE_SPACE) :
                            alt15 = 1


                        if alt15 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop15


                    self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_myOption275)

                    # SpeakPython.g:120:79: ( SEMI )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == SEMI) :
                        alt16 = 1
                    if alt16 == 1:
                        # SpeakPython.g:120:80: SEMI
                        pass 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption278)




                    if self._state.backtracking == 0:
                        pass
                        self.optionVals[WORD5.text] = self.defaultOptionVals[WORD5.text]; 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOption"



    # $ANTLR start "mat"
    # SpeakPython.g:124:1: mat returns [matR] : ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields ;
    def mat(self, ):
        matR = None


        exps6 = None



        self.keywords = [];

        try:
            try:
                # SpeakPython.g:129:2: ( ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields )
                # SpeakPython.g:129:4: ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields
                pass 
                # SpeakPython.g:129:4: ( localOptions ( WHITE_SPACE | NEWLINE )* )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == AT_OPTIONS) :
                    alt19 = 1
                if alt19 == 1:
                    # SpeakPython.g:129:5: localOptions ( WHITE_SPACE | NEWLINE )*
                    pass 
                    self._state.following.append(self.FOLLOW_localOptions_in_mat305)
                    self.localOptions()

                    self._state.following.pop()

                    # SpeakPython.g:129:18: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == NEWLINE or LA18_0 == WHITE_SPACE) :
                            alt18 = 1


                        if alt18 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop18





                self._state.following.append(self.FOLLOW_exps_in_mat318)
                exps6 = self.exps()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.optionVals = self.optionValsBackup; 



                self._state.following.append(self.FOLLOW_statementFields_in_mat327)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    matR =  Match(exps6, self.statementFieldDict['testCases'], self.keywords, self.kGroupRegexes, self.statementFieldDict['results']) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return matR

    # $ANTLR end "mat"



    # $ANTLR start "statementFields"
    # SpeakPython.g:135:1: statementFields : ( ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields | ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields |);
    def statementFields(self, ):
        mResults7 = None

        testCases8 = None


        try:
            try:
                # SpeakPython.g:136:2: ( ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields | ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields |)
                alt22 = 3
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # SpeakPython.g:136:4: ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields
                    pass 
                    # SpeakPython.g:136:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == NEWLINE or LA20_0 == WHITE_SPACE) :
                            alt20 = 1


                        if alt20 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop20


                    self.match(self.input, AT_RESULTS, self.FOLLOW_AT_RESULTS_in_statementFields352)

                    self._state.following.append(self.FOLLOW_mResults_in_statementFields354)
                    mResults7 = self.mResults()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields356)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields358)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.statementFieldDict['results'] = mResults7; 




                elif alt22 == 2:
                    # SpeakPython.g:138:4: ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields
                    pass 
                    # SpeakPython.g:138:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == NEWLINE or LA21_0 == WHITE_SPACE) :
                            alt21 = 1


                        if alt21 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop21


                    self.match(self.input, AT_TESTS, self.FOLLOW_AT_TESTS_in_statementFields376)

                    self._state.following.append(self.FOLLOW_testCases_in_statementFields378)
                    testCases8 = self.testCases()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields380)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields382)
                    self.statementFields()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        self.statementFieldDict['testCases'] = testCases8; 




                elif alt22 == 3:
                    # SpeakPython.g:140:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "statementFields"



    # $ANTLR start "alias"
    # SpeakPython.g:143:1: alias returns [aliasR] : HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields ;
    def alias(self, ):
        aliasR = None


        HASH_NAME9 = None
        exps10 = None


        try:
            try:
                # SpeakPython.g:144:2: ( HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields )
                # SpeakPython.g:144:4: HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields
                pass 
                HASH_NAME9 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_alias406)

                self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_alias408)

                # SpeakPython.g:144:20: ( WHITE_SPACE )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == WHITE_SPACE) :
                        alt23 = 1


                    if alt23 == 1:
                        # SpeakPython.g:144:20: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias410)


                    else:
                        break #loop23


                self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_alias413)

                # SpeakPython.g:144:39: ( WHITE_SPACE )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == WHITE_SPACE) :
                        alt24 = 1


                    if alt24 == 1:
                        # SpeakPython.g:144:39: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias415)


                    else:
                        break #loop24


                self.match(self.input, EQ, self.FOLLOW_EQ_in_alias418)

                # SpeakPython.g:144:55: ( WHITE_SPACE )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == WHITE_SPACE) :
                        alt25 = 1


                    if alt25 == 1:
                        # SpeakPython.g:144:55: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias420)


                    else:
                        break #loop25


                self._state.following.append(self.FOLLOW_exps_in_alias423)
                exps10 = self.exps()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_statementFields_in_alias425)
                self.statementFields()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    self.aliasWord = HASH_NAME9.text[1:]; self.aliasKeywords[self.aliasWord] = self.keywords; print self.aliasWord + ": " + str(self.keywords); aliasR =  Function(self.aliasWord, exps10, self.statementFieldDict['testCases'], self.kGroupRegexes, self.statementFieldDict['results']) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return aliasR

    # $ANTLR end "alias"



    # $ANTLR start "exps"
    # SpeakPython.g:148:1: exps returns [expsR=''] : expVal SEMI ;
    def exps(self, ):
        expsR = ''


        expVal11 = None


        try:
            try:
                # SpeakPython.g:149:2: ( expVal SEMI )
                # SpeakPython.g:149:4: expVal SEMI
                pass 
                self._state.following.append(self.FOLLOW_expVal_in_exps444)
                expVal11 = self.expVal()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_exps446)

                if self._state.backtracking == 0:
                    pass
                    expsR =  sub(r"\?P<\*>", GroupCounter(), expVal11) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expsR

    # $ANTLR end "exps"



    # $ANTLR start "expVal"
    # SpeakPython.g:153:1: expVal returns [expValR=''] : ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp );
    def expVal(self, ):
        expValR = ''


        w1 = None
        VAR_NAME17 = None
        HASH_NAME19 = None
        REGEX21 = None
        e1 = None

        e2 = None

        opt12 = None

        subExp13 = None

        opt14 = None

        subExp15 = None

        subExp16 = None

        subExp18 = None

        subExp20 = None

        subExp22 = None


        try:
            try:
                # SpeakPython.g:154:2: ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp )
                alt26 = 6
                LA26 = self.input.LA(1)
                if LA26 == LS_BR:
                    alt26 = 1
                elif LA26 == LR_BR:
                    alt26 = 2
                elif LA26 == WORD:
                    alt26 = 3
                elif LA26 == VAR_NAME:
                    alt26 = 4
                elif LA26 == HASH_NAME:
                    alt26 = 5
                elif LA26 == REGEX:
                    alt26 = 6
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # SpeakPython.g:154:4: LS_BR e1= expVal RS_BR opt subExp
                    pass 
                    self.match(self.input, LS_BR, self.FOLLOW_LS_BR_in_expVal464)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount += 1; 



                    self._state.following.append(self.FOLLOW_expVal_in_expVal475)
                    e1 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RS_BR, self.FOLLOW_RS_BR_in_expVal477)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount -= 1; 



                    self._state.following.append(self.FOLLOW_opt_in_expVal486)
                    opt12 = self.opt()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0 and (opt12[1] not in "?*" or len(opt12[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; 



                    if self._state.backtracking == 0:
                        pass
                        if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = e1; self.kGroupCount += 1; self.isKleene = False; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal500)
                    subExp13 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt12[0] + "(?P<*>" + e1 + ")" + opt12[1] + subExp13 




                elif alt26 == 2:
                    # SpeakPython.g:164:4: LR_BR e2= expVal RR_BR opt subExp
                    pass 
                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_expVal511)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount += 1; 



                    self._state.following.append(self.FOLLOW_expVal_in_expVal522)
                    e2 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_expVal524)

                    if self._state.backtracking == 0:
                        pass
                        self.bracketCount -= 1; 



                    self._state.following.append(self.FOLLOW_opt_in_expVal533)
                    opt14 = self.opt()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0 and (opt14[1] not in "?*" or len(opt14[1]) == 0)): self.finishedKeywords = True; self.wordAtBracket = 0; 



                    if self._state.backtracking == 0:
                        pass
                        if self.isKleene: self.kGroupRegexes[str(self.kGroupCount)] = e2; self.kGroupCount += 1; self.isKleene = False; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal558)
                    subExp15 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  opt14[0] + "(?:" + e2 + ")" + opt14[1] + subExp15 




                elif alt26 == 3:
                    # SpeakPython.g:178:4: w1= WORD subExp
                    pass 
                    w1 = self.match(self.input, WORD, self.FOLLOW_WORD_in_expVal576)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append(w1.text.lower()); print self.keywords; self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = True; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal587)
                    subExp16 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  "(?:" + w1.text.lower() + ")" + subExp16 




                elif alt26 == 4:
                    # SpeakPython.g:183:4: VAR_NAME subExp
                    pass 
                    VAR_NAME17 = self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_expVal598)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = True; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal609)
                    subExp18 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        expValR =  "(?P<" + VAR_NAME17.text[1:] + ">" + self.optionVals['varRegex'] + ")" + subExp18 




                elif alt26 == 5:
                    # SpeakPython.g:188:4: HASH_NAME subExp
                    pass 
                    HASH_NAME19 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_expVal620)

                    if self._state.backtracking == 0:
                        pass
                        name = HASH_NAME19.text[1:]; self.aliasUseCount[name] = 0 if (name not in self.aliasUseCount) else self.aliasUseCount[name] + 1; 



                    if self._state.backtracking == 0:
                        pass
                        storedValue = self.aliasUseCount[name]; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.extend(self.aliasKeywords[name]); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount == 0): self.finishedKeywords = True; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal641)
                    subExp20 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        retVal = subExp20; 



                    if self._state.backtracking == 0:
                        pass
                        retVal = "(?P<" + "_" + name + "_" + str(storedValue) + "_>" + sub(r"<([^>]+)>", "<_" + name + "_" + str(storedValue) + r"_\g<1>" + ">", self.aliases[name].getExp()) + ")" + subExp20; 



                    if self._state.backtracking == 0:
                        pass
                        expValR =  retVal 




                elif alt26 == 6:
                    # SpeakPython.g:197:4: REGEX subExp
                    pass 
                    REGEX21 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_expVal662)

                    if self._state.backtracking == 0:
                        pass
                        if (self.isKeyword and not self.finishedKeywords): self.keywords.append("*"); self.isKeyword = False; self.wordAtBracket = self.bracketCount; 



                    self._state.following.append(self.FOLLOW_subExp_in_expVal671)
                    subExp22 = self.subExp()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        reg = REGEX21.text[1:-2]; reg = sub(r"\(\?<([^>]+)>", r"(?P<\1>", reg); reg = sub(r"\([^\?]", r"(?:", reg); expValR =  reg + subExp22 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expValR

    # $ANTLR end "expVal"



    # $ANTLR start "subExp"
    # SpeakPython.g:204:1: subExp returns [subExpR=''] : ( ( WHITE_SPACE )* expVal | ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal |);
    def subExp(self, ):
        subExpR = ''


        expVal23 = None

        expVal24 = None


        try:
            try:
                # SpeakPython.g:205:2: ( ( WHITE_SPACE )* expVal | ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal |)
                alt30 = 3
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # SpeakPython.g:205:4: ( WHITE_SPACE )* expVal
                    pass 
                    # SpeakPython.g:205:4: ( WHITE_SPACE )*
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == WHITE_SPACE) :
                            alt27 = 1


                        if alt27 == 1:
                            # SpeakPython.g:205:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp692)


                        else:
                            break #loop27


                    self._state.following.append(self.FOLLOW_expVal_in_subExp695)
                    expVal23 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  self.optionVals['wordDelim'] + "*" + expVal23 




                elif alt30 == 2:
                    # SpeakPython.g:207:4: ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal
                    pass 
                    # SpeakPython.g:207:4: ( WHITE_SPACE )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == WHITE_SPACE) :
                            alt28 = 1


                        if alt28 == 1:
                            # SpeakPython.g:207:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp705)


                        else:
                            break #loop28


                    self.match(self.input, OR, self.FOLLOW_OR_in_subExp708)

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount <= self.wordAtBracket): self.isKeyword = True; self.finishedKeywords = False; 



                    # SpeakPython.g:209:3: ( WHITE_SPACE )*
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == WHITE_SPACE) :
                            alt29 = 1


                        if alt29 == 1:
                            # SpeakPython.g:209:3: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp718)


                        else:
                            break #loop29


                    self._state.following.append(self.FOLLOW_expVal_in_subExp721)
                    expVal24 = self.expVal()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        subExpR =  "|" + expVal24 




                elif alt30 == 3:
                    # SpeakPython.g:212:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return subExpR

    # $ANTLR end "subExp"



    # $ANTLR start "opt"
    # SpeakPython.g:216:1: opt returns [optR=('','')] : ( QSTN | STAR | PLUS |);
    def opt(self, ):
        optR = ('','')


        try:
            try:
                # SpeakPython.g:217:2: ( QSTN | STAR | PLUS |)
                alt31 = 4
                LA31 = self.input.LA(1)
                if LA31 == QSTN:
                    alt31 = 1
                elif LA31 == STAR:
                    alt31 = 2
                elif LA31 == PLUS:
                    alt31 = 3
                elif LA31 == EOF or LA31 == HASH_NAME or LA31 == LR_BR or LA31 == LS_BR or LA31 == OR or LA31 == REGEX or LA31 == RR_BR or LA31 == RS_BR or LA31 == SEMI or LA31 == VAR_NAME or LA31 == WHITE_SPACE or LA31 == WORD:
                    alt31 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # SpeakPython.g:217:4: QSTN
                    pass 
                    self.match(self.input, QSTN, self.FOLLOW_QSTN_in_opt750)

                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("","?") 




                elif alt31 == 2:
                    # SpeakPython.g:218:4: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_opt759)

                    if self._state.backtracking == 0:
                        pass
                        self.isKleene = True; 



                    if self._state.backtracking == 0:
                        pass
                        if (self.bracketCount < self.wordAtBracket): self.isKeyword = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)*)") 




                elif alt31 == 3:
                    # SpeakPython.g:219:4: PLUS
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_opt770)

                    if self._state.backtracking == 0:
                        pass
                        self.isKleene = True; 



                    if self._state.backtracking == 0:
                        pass
                        optR = ("(?P<k_" + str(self.kGroupCount) + ">(?:", self.optionVals['wordDelim'] + "+)+)") 




                elif alt31 == 4:
                    # SpeakPython.g:220:4: 
                    pass 
                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return optR

    # $ANTLR end "opt"



    # $ANTLR start "testCases"
    # SpeakPython.g:223:1: testCases returns [testCasesR=[]] : ( ( NEWLINE | WHITE_SPACE )* testCase ts= testCases | ( NEWLINE | WHITE_SPACE )* );
    def testCases(self, ):
        testCasesR = []


        ts = None

        testCase25 = None


        try:
            try:
                # SpeakPython.g:224:2: ( ( NEWLINE | WHITE_SPACE )* testCase ts= testCases | ( NEWLINE | WHITE_SPACE )* )
                alt34 = 2
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # SpeakPython.g:224:4: ( NEWLINE | WHITE_SPACE )* testCase ts= testCases
                    pass 
                    # SpeakPython.g:224:4: ( NEWLINE | WHITE_SPACE )*
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == NEWLINE or LA32_0 == WHITE_SPACE) :
                            alt32 = 1


                        if alt32 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop32


                    self._state.following.append(self.FOLLOW_testCase_in_testCases803)
                    testCase25 = self.testCase()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_testCases_in_testCases807)
                    ts = self.testCases()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        ts.append(testCase25); testCasesR =  ts 




                elif alt34 == 2:
                    # SpeakPython.g:226:4: ( NEWLINE | WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:226:4: ( NEWLINE | WHITE_SPACE )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == NEWLINE or LA33_0 == WHITE_SPACE) :
                            alt33 = 1


                        if alt33 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop33


                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCasesR

    # $ANTLR end "testCases"



    # $ANTLR start "testCase"
    # SpeakPython.g:229:1: testCase returns [testCaseR=''] : (q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING |q3= QUOTE_STRING );
    def testCase(self, ):
        testCaseR = ''


        q1 = None
        q2 = None
        q3 = None

        try:
            try:
                # SpeakPython.g:230:2: (q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING |q3= QUOTE_STRING )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # SpeakPython.g:230:4: q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING
                    pass 
                    q1 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase843)

                    # SpeakPython.g:230:20: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == NEWLINE or LA35_0 == WHITE_SPACE) :
                            alt35 = 1


                        if alt35 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop35


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_testCase854)

                    # SpeakPython.g:230:48: ( RA_BR )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == RA_BR) :
                        alt36 = 1
                    if alt36 == 1:
                        # SpeakPython.g:230:49: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_testCase857)




                    # SpeakPython.g:230:57: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == NEWLINE or LA37_0 == WHITE_SPACE) :
                            alt37 = 1


                        if alt37 == 1:
                            # SpeakPython.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                if self._state.backtracking > 0:
                                    raise BacktrackingFailed


                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop37


                    q2 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase872)

                    if self._state.backtracking == 0:
                        pass
                        self.globalTests[q1.text[1:-1]] = q2.text[1:-1]; testCaseR =  q1.text[1:-1] 




                elif alt38 == 2:
                    # SpeakPython.g:231:4: q3= QUOTE_STRING
                    pass 
                    q3 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase881)

                    if self._state.backtracking == 0:
                        pass
                        testCaseR =  q3.text[1:-1] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCaseR

    # $ANTLR end "testCase"



    # $ANTLR start "mResults"
    # SpeakPython.g:236:1: mResults returns [mResultsR=[]] : ( ( NEWLINE )* m1= mResult ms= mResults | ( NEWLINE )* );
    def mResults(self, ):
        mResultsR = []


        m1 = None

        ms = None


        try:
            try:
                # SpeakPython.g:237:2: ( ( NEWLINE )* m1= mResult ms= mResults | ( NEWLINE )* )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # SpeakPython.g:237:4: ( NEWLINE )* m1= mResult ms= mResults
                    pass 
                    # SpeakPython.g:237:4: ( NEWLINE )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == NEWLINE) :
                            alt39 = 1


                        if alt39 == 1:
                            # SpeakPython.g:237:4: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_mResults902)


                        else:
                            break #loop39


                    self._state.following.append(self.FOLLOW_mResult_in_mResults907)
                    m1 = self.mResult()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_mResults_in_mResults911)
                    ms = self.mResults()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        ms.append(m1); mResultsR =  ms 




                elif alt41 == 2:
                    # SpeakPython.g:238:4: ( NEWLINE )*
                    pass 
                    # SpeakPython.g:238:4: ( NEWLINE )*
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == NEWLINE) :
                            alt40 = 1


                        if alt40 == 1:
                            # SpeakPython.g:238:4: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_mResults918)


                        else:
                            break #loop40


                    if self._state.backtracking == 0:
                        pass
                        mResultsR =  [] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return mResultsR

    # $ANTLR end "mResults"



    # $ANTLR start "mResult"
    # SpeakPython.g:242:1: mResult returns [mResultR] : ls= labels LC_BR resultant RC_BR ;
    def mResult(self, ):
        mResultR = None


        ls = None

        resultant26 = None


        try:
            try:
                # SpeakPython.g:243:2: (ls= labels LC_BR resultant RC_BR )
                # SpeakPython.g:243:4: ls= labels LC_BR resultant RC_BR
                pass 
                self._state.following.append(self.FOLLOW_labels_in_mResult940)
                ls = self.labels()

                self._state.following.pop()

                self.match(self.input, LC_BR, self.FOLLOW_LC_BR_in_mResult942)

                self._state.following.append(self.FOLLOW_resultant_in_mResult944)
                resultant26 = self.resultant()

                self._state.following.pop()

                self.match(self.input, RC_BR, self.FOLLOW_RC_BR_in_mResult946)

                if self._state.backtracking == 0:
                    pass
                    mResultR =  Result(ls, resultant26) 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return mResultR

    # $ANTLR end "mResult"



    # $ANTLR start "resultant"
    # SpeakPython.g:246:1: resultant returns [resultantR] : results ;
    def resultant(self, ):
        resultantR = None


        results27 = None


        try:
            try:
                # SpeakPython.g:247:2: ( results )
                # SpeakPython.g:247:4: results
                pass 
                self._state.following.append(self.FOLLOW_results_in_resultant963)
                results27 = self.results()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    resultantR =  results27 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultantR

    # $ANTLR end "resultant"



    # $ANTLR start "labels"
    # SpeakPython.g:251:1: labels returns [labelsR] : (l1= label labelsRest |l2= label );
    def labels(self, ):
        labelsR = None


        l1 = None

        l2 = None

        labelsRest28 = None


        try:
            try:
                # SpeakPython.g:252:2: (l1= label labelsRest |l2= label )
                alt42 = 2
                alt42 = self.dfa42.predict(self.input)
                if alt42 == 1:
                    # SpeakPython.g:252:4: l1= label labelsRest
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels984)
                    l1 = self.label()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_labelsRest_in_labels986)
                    labelsRest28 = self.labelsRest()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        labelsRest28.append(l1); labelsR =  labelsRest28 




                elif alt42 == 2:
                    # SpeakPython.g:253:4: l2= label
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels995)
                    l2 = self.label()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        labelsR = [l2] 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelsR

    # $ANTLR end "labels"



    # $ANTLR start "labelsRest"
    # SpeakPython.g:256:1: labelsRest returns [labelsRestR] : COMMA labels ;
    def labelsRest(self, ):
        labelsRestR = None


        labels29 = None


        try:
            try:
                # SpeakPython.g:257:2: ( COMMA labels )
                # SpeakPython.g:257:4: COMMA labels
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_labelsRest1012)

                self._state.following.append(self.FOLLOW_labels_in_labelsRest1014)
                labels29 = self.labels()

                self._state.following.pop()

                if self._state.backtracking == 0:
                    pass
                    labelsRestR =  labels29 






            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelsRestR

    # $ANTLR end "labelsRest"



    # $ANTLR start "label"
    # SpeakPython.g:261:1: label returns [labelR] : ( ( WHITE_SPACE )* NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )* | ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD ( WHITE_SPACE )* );
    def label(self, ):
        labelR = None


        NUM30 = None
        HASH_NAME31 = None
        KLEENE32 = None
        NUM33 = None
        WORD34 = None
        NUM35 = None
        WORD36 = None

        try:
            try:
                # SpeakPython.g:262:2: ( ( WHITE_SPACE )* NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )* | ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD ( WHITE_SPACE )* )
                alt53 = 5
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # SpeakPython.g:262:4: ( WHITE_SPACE )* NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:262:4: ( WHITE_SPACE )*
                    while True: #loop43
                        alt43 = 2
                        LA43_0 = self.input.LA(1)

                        if (LA43_0 == WHITE_SPACE) :
                            alt43 = 1


                        if alt43 == 1:
                            # SpeakPython.g:262:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1034)


                        else:
                            break #loop43


                    NUM30 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label1037)

                    # SpeakPython.g:262:21: ( WHITE_SPACE )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == WHITE_SPACE) :
                            alt44 = 1


                        if alt44 == 1:
                            # SpeakPython.g:262:21: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1039)


                        else:
                            break #loop44


                    if self._state.backtracking == 0:
                        pass
                        labelR =  NUM30.text 




                elif alt53 == 2:
                    # SpeakPython.g:263:4: ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:263:4: ( WHITE_SPACE )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == WHITE_SPACE) :
                            alt45 = 1


                        if alt45 == 1:
                            # SpeakPython.g:263:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1047)


                        else:
                            break #loop45


                    HASH_NAME31 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label1050)

                    # SpeakPython.g:263:27: ( WHITE_SPACE )*
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == WHITE_SPACE) :
                            alt46 = 1


                        if alt46 == 1:
                            # SpeakPython.g:263:27: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1052)


                        else:
                            break #loop46


                    if self._state.backtracking == 0:
                        pass
                        labelR =  HASH_NAME31.text[1:] 




                elif alt53 == 3:
                    # SpeakPython.g:264:4: ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:264:4: ( WHITE_SPACE )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == WHITE_SPACE) :
                            alt47 = 1


                        if alt47 == 1:
                            # SpeakPython.g:264:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1060)


                        else:
                            break #loop47


                    KLEENE32 = self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_label1063)

                    NUM33 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label1065)

                    # SpeakPython.g:264:28: ( WHITE_SPACE )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == WHITE_SPACE) :
                            alt48 = 1


                        if alt48 == 1:
                            # SpeakPython.g:264:28: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1067)


                        else:
                            break #loop48


                    if self._state.backtracking == 0:
                        pass
                        labelR =  KLEENE32.text + NUM33.text 




                elif alt53 == 4:
                    # SpeakPython.g:265:4: ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:265:4: ( WHITE_SPACE )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == WHITE_SPACE) :
                            alt49 = 1


                        if alt49 == 1:
                            # SpeakPython.g:265:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1075)


                        else:
                            break #loop49


                    WORD34 = self.match(self.input, WORD, self.FOLLOW_WORD_in_label1078)

                    NUM35 = self.match(self.input, NUM, self.FOLLOW_NUM_in_label1080)

                    # SpeakPython.g:265:26: ( WHITE_SPACE )*
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == WHITE_SPACE) :
                            alt50 = 1


                        if alt50 == 1:
                            # SpeakPython.g:265:26: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1082)


                        else:
                            break #loop50


                    if self._state.backtracking == 0:
                        pass
                        labelR =  WORD34.text + NUM35.text 




                elif alt53 == 5:
                    # SpeakPython.g:266:4: ( WHITE_SPACE )* WORD ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:266:4: ( WHITE_SPACE )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == WHITE_SPACE) :
                            alt51 = 1


                        if alt51 == 1:
                            # SpeakPython.g:266:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1090)


                        else:
                            break #loop51


                    WORD36 = self.match(self.input, WORD, self.FOLLOW_WORD_in_label1093)

                    # SpeakPython.g:266:22: ( WHITE_SPACE )*
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == WHITE_SPACE) :
                            alt52 = 1


                        if alt52 == 1:
                            # SpeakPython.g:266:22: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label1095)


                        else:
                            break #loop52


                    if self._state.backtracking == 0:
                        pass
                        labelR =  WORD36.text 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return labelR

    # $ANTLR end "label"



    # $ANTLR start "results"
    # SpeakPython.g:270:1: results returns [resultsR=[]] : ( ( WHITE_SPACE )* result rs= results | ( WHITE_SPACE )* );
    def results(self, ):
        resultsR = []


        rs = None

        result37 = None


        try:
            try:
                # SpeakPython.g:271:2: ( ( WHITE_SPACE )* result rs= results | ( WHITE_SPACE )* )
                alt56 = 2
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # SpeakPython.g:271:4: ( WHITE_SPACE )* result rs= results
                    pass 
                    # SpeakPython.g:271:4: ( WHITE_SPACE )*
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == WHITE_SPACE) :
                            alt54 = 1


                        if alt54 == 1:
                            # SpeakPython.g:271:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_results1114)


                        else:
                            break #loop54


                    self._state.following.append(self.FOLLOW_result_in_results1117)
                    result37 = self.result()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_results_in_results1121)
                    rs = self.results()

                    self._state.following.pop()

                    if self._state.backtracking == 0:
                        pass
                        rs.insert(0, result37); resultsR =  rs 




                elif alt56 == 2:
                    # SpeakPython.g:272:4: ( WHITE_SPACE )*
                    pass 
                    # SpeakPython.g:272:4: ( WHITE_SPACE )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == WHITE_SPACE) :
                            alt55 = 1


                        if alt55 == 1:
                            # SpeakPython.g:272:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_results1128)


                        else:
                            break #loop55


                    if self._state.backtracking == 0:
                        pass





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultsR

    # $ANTLR end "results"



    # $ANTLR start "result"
    # SpeakPython.g:275:1: result returns [resultR] : ( QUOTE_STRING | VAR_NAME | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR );
    def result(self, ):
        resultR = None


        QUOTE_STRING38 = None
        VAR_NAME39 = None
        HASH_NAME40 = None
        KLEENE41 = None
        NUM42 = None
        r1 = None

        r2 = None


        try:
            try:
                # SpeakPython.g:276:2: ( QUOTE_STRING | VAR_NAME | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR )
                alt57 = 4
                LA57 = self.input.LA(1)
                if LA57 == QUOTE_STRING:
                    alt57 = 1
                elif LA57 == VAR_NAME:
                    alt57 = 2
                elif LA57 == HASH_NAME:
                    alt57 = 3
                elif LA57 == KLEENE:
                    alt57 = 4
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed


                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae


                if alt57 == 1:
                    # SpeakPython.g:276:4: QUOTE_STRING
                    pass 
                    QUOTE_STRING38 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result1146)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  StringResult(QUOTE_STRING38.text[1:-1]) 




                elif alt57 == 2:
                    # SpeakPython.g:277:4: VAR_NAME
                    pass 
                    VAR_NAME39 = self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_result1153)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  VarResult(VAR_NAME39.text[1:]) 




                elif alt57 == 3:
                    # SpeakPython.g:278:4: HASH_NAME
                    pass 
                    HASH_NAME40 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result1160)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  FunctionResult(HASH_NAME40.text[1:]) 




                elif alt57 == 4:
                    # SpeakPython.g:279:4: KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR
                    pass 
                    KLEENE41 = self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_result1167)

                    NUM42 = self.match(self.input, NUM, self.FOLLOW_NUM_in_result1169)

                    self.match(self.input, LA_BR, self.FOLLOW_LA_BR_in_result1171)

                    self._state.following.append(self.FOLLOW_results_in_result1175)
                    r1 = self.results()

                    self._state.following.pop()

                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_result1177)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result1179)

                    self._state.following.append(self.FOLLOW_results_in_result1183)
                    r2 = self.results()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result1185)

                    if self._state.backtracking == 0:
                        pass
                        resultR =  KleeneResult(KLEENE41.text + NUM42.text, r1, r2) 





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return resultR

    # $ANTLR end "result"



    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\2\5\6\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\2\6\1\20\3\uffff\1\20\1\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\3\46\3\uffff\1\46\1\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\3\uffff\1\2\1\3\1\4\1\uffff\1\1"
        )

    DFA5_special = DFA.unpack(
        u"\10\uffff"
        )


    DFA5_transition = [
        DFA.unpack(u"\1\4\1\3\10\uffff\1\2\3\uffff\2\3\1\1\7\uffff\1\3\5"
        u"\uffff\1\3\1\1\1\3"),
        DFA.unpack(u"\1\4\1\3\10\uffff\1\2\3\uffff\2\3\1\1\7\uffff\1\3\5"
        u"\uffff\1\3\1\1\1\3"),
        DFA.unpack(u"\1\3\3\uffff\1\6\1\3\2\uffff\1\3\5\uffff\1\3\2\uffff"
        u"\1\3\2\uffff\3\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\3\uffff\2\3\10\uffff\1\3\1\7\4\uffff\1\3\1\7\1"
        u"\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #5

    class DFA5(DFA):
        pass


    # lookup tables for DFA #8

    DFA8_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA8_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA8_min = DFA.unpack(
        u"\2\5\2\uffff"
        )

    DFA8_max = DFA.unpack(
        u"\2\46\2\uffff"
        )

    DFA8_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA8_special = DFA.unpack(
        u"\4\uffff"
        )


    DFA8_transition = [
        DFA.unpack(u"\1\3\20\uffff\1\1\16\uffff\1\1\1\2"),
        DFA.unpack(u"\1\3\20\uffff\1\1\16\uffff\1\1\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #8

    class DFA8(DFA):
        pass


    # lookup tables for DFA #17

    DFA17_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA17_eof = DFA.unpack(
        u"\10\uffff"
        )

    DFA17_min = DFA.unpack(
        u"\1\46\2\17\3\15\2\uffff"
        )

    DFA17_max = DFA.unpack(
        u"\1\46\5\45\2\uffff"
        )

    DFA17_accept = DFA.unpack(
        u"\6\uffff\1\1\1\2"
        )

    DFA17_special = DFA.unpack(
        u"\10\uffff"
        )


    DFA17_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\3\6\uffff\1\2\16\uffff\1\2"),
        DFA.unpack(u"\1\3\6\uffff\1\2\16\uffff\1\2"),
        DFA.unpack(u"\1\7\10\uffff\1\5\5\uffff\1\4\1\uffff\1\6\6\uffff\1"
        u"\5"),
        DFA.unpack(u"\1\7\10\uffff\1\5\7\uffff\1\6\6\uffff\1\5"),
        DFA.unpack(u"\1\7\10\uffff\1\5\7\uffff\1\6\6\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #17

    class DFA17(DFA):
        pass


    # lookup tables for DFA #22

    DFA22_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA22_eof = DFA.unpack(
        u"\2\4\3\uffff"
        )

    DFA22_min = DFA.unpack(
        u"\2\6\3\uffff"
        )

    DFA22_max = DFA.unpack(
        u"\2\46\3\uffff"
        )

    DFA22_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\3"
        )

    DFA22_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA22_transition = [
        DFA.unpack(u"\2\4\1\2\1\3\6\uffff\1\4\3\uffff\2\4\1\1\7\uffff\1\4"
        u"\5\uffff\1\4\1\1\1\4"),
        DFA.unpack(u"\2\4\1\2\1\3\6\uffff\1\4\3\uffff\2\4\1\1\7\uffff\1"
        u"\4\5\uffff\1\4\1\1\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #22

    class DFA22(DFA):
        pass


    # lookup tables for DFA #30

    DFA30_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA30_eof = DFA.unpack(
        u"\1\4\4\uffff"
        )

    DFA30_min = DFA.unpack(
        u"\2\20\3\uffff"
        )

    DFA30_max = DFA.unpack(
        u"\2\46\3\uffff"
        )

    DFA30_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\3"
        )

    DFA30_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA30_transition = [
        DFA.unpack(u"\1\2\3\uffff\2\2\2\uffff\1\3\5\uffff\1\2\3\4\2\uffff"
        u"\1\2\1\1\1\2"),
        DFA.unpack(u"\1\2\3\uffff\2\2\2\uffff\1\3\5\uffff\1\2\5\uffff\1"
        u"\2\1\1\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #30

    class DFA30(DFA):
        pass


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\2\5\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\2\45\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA34_special = DFA.unpack(
        u"\4\uffff"
        )


    DFA34_transition = [
        DFA.unpack(u"\1\3\20\uffff\1\1\4\uffff\1\2\11\uffff\1\1"),
        DFA.unpack(u"\1\3\20\uffff\1\1\4\uffff\1\2\11\uffff\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #38

    DFA38_eot = DFA.unpack(
        u"\5\uffff"
        )

    DFA38_eof = DFA.unpack(
        u"\1\uffff\2\4\2\uffff"
        )

    DFA38_min = DFA.unpack(
        u"\1\33\2\5\2\uffff"
        )

    DFA38_max = DFA.unpack(
        u"\1\33\2\45\2\uffff"
        )

    DFA38_accept = DFA.unpack(
        u"\3\uffff\1\1\1\2"
        )

    DFA38_special = DFA.unpack(
        u"\5\uffff"
        )


    DFA38_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\4\11\uffff\1\3\6\uffff\1\2\4\uffff\1\4\11\uffff"
        u"\1\2"),
        DFA.unpack(u"\1\4\11\uffff\1\3\6\uffff\1\2\4\uffff\1\4\11\uffff"
        u"\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #38

    class DFA38(DFA):
        pass


    # lookup tables for DFA #41

    DFA41_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA41_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA41_min = DFA.unpack(
        u"\2\5\2\uffff"
        )

    DFA41_max = DFA.unpack(
        u"\2\46\2\uffff"
        )

    DFA41_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA41_special = DFA.unpack(
        u"\4\uffff"
        )


    DFA41_transition = [
        DFA.unpack(u"\1\3\12\uffff\2\2\4\uffff\1\1\1\2\15\uffff\2\2"),
        DFA.unpack(u"\1\3\12\uffff\2\2\4\uffff\1\1\1\2\15\uffff\2\2"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #41

    class DFA41(DFA):
        pass


    # lookup tables for DFA #42

    DFA42_eot = DFA.unpack(
        u"\17\uffff"
        )

    DFA42_eof = DFA.unpack(
        u"\2\uffff\2\10\1\uffff\2\10\2\uffff\6\10"
        )

    DFA42_min = DFA.unpack(
        u"\2\20\2\13\1\27\2\13\2\uffff\6\13"
        )

    DFA42_max = DFA.unpack(
        u"\2\46\2\45\1\27\2\45\2\uffff\6\45"
        )

    DFA42_accept = DFA.unpack(
        u"\7\uffff\1\1\1\2\6\uffff"
        )

    DFA42_special = DFA.unpack(
        u"\17\uffff"
        )


    DFA42_transition = [
        DFA.unpack(u"\1\3\1\4\5\uffff\1\2\15\uffff\1\1\1\5"),
        DFA.unpack(u"\1\3\1\4\5\uffff\1\2\15\uffff\1\1\1\5"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\6"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\11"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\7\7\uffff\1\10\3\uffff\1\13\15\uffff\1\14"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\6"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\11"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\15"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\16"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\14"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\15"),
        DFA.unpack(u"\1\7\7\uffff\1\10\21\uffff\1\16")
    ]

    # class definition for DFA #42

    class DFA42(DFA):
        pass


    # lookup tables for DFA #53

    DFA53_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA53_eof = DFA.unpack(
        u"\5\uffff\1\7\2\uffff"
        )

    DFA53_min = DFA.unpack(
        u"\2\20\3\uffff\1\13\2\uffff"
        )

    DFA53_max = DFA.unpack(
        u"\2\46\3\uffff\1\45\2\uffff"
        )

    DFA53_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2\1\3\1\uffff\1\4\1\5"
        )

    DFA53_special = DFA.unpack(
        u"\10\uffff"
        )


    DFA53_transition = [
        DFA.unpack(u"\1\3\1\4\5\uffff\1\2\15\uffff\1\1\1\5"),
        DFA.unpack(u"\1\3\1\4\5\uffff\1\2\15\uffff\1\1\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\7\7\uffff\1\7\3\uffff\1\6\15\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #53

    class DFA53(DFA):
        pass


    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\4\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\2\3\2\uffff"
        )

    DFA56_min = DFA.unpack(
        u"\2\20\2\uffff"
        )

    DFA56_max = DFA.unpack(
        u"\2\45\2\uffff"
        )

    DFA56_accept = DFA.unpack(
        u"\2\uffff\1\1\1\2"
        )

    DFA56_special = DFA.unpack(
        u"\4\uffff"
        )


    DFA56_transition = [
        DFA.unpack(u"\2\2\11\uffff\1\2\2\3\1\uffff\1\3\4\uffff\1\2\1\1"),
        DFA.unpack(u"\2\2\11\uffff\1\2\2\3\1\uffff\1\3\4\uffff\1\2\1\1"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #56

    class DFA56(DFA):
        pass


 

    FOLLOW_s_in_prog47 = frozenset([22, 37])
    FOLLOW_EOF_in_prog58 = frozenset([1])
    FOLLOW_alias_in_s85 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s89 = frozenset([1])
    FOLLOW_mat_in_s104 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s108 = frozenset([1])
    FOLLOW_globalOptions_in_s123 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s125 = frozenset([1])
    FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions141 = frozenset([5, 22, 37, 38])
    FOLLOW_myOptions_in_globalOptions143 = frozenset([5])
    FOLLOW_AT_in_globalOptions145 = frozenset([1])
    FOLLOW_AT_OPTIONS_in_localOptions156 = frozenset([5, 22, 37, 38])
    FOLLOW_myOptions_in_localOptions160 = frozenset([5])
    FOLLOW_AT_in_localOptions162 = frozenset([1])
    FOLLOW_myOption_in_myOptions182 = frozenset([22, 37, 38])
    FOLLOW_myOptions_in_myOptions184 = frozenset([1])
    FOLLOW_WORD_in_myOption209 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_myOption220 = frozenset([22, 28, 30, 37])
    FOLLOW_RA_BR_in_myOption223 = frozenset([22, 30, 37])
    FOLLOW_REGEX_in_myOption236 = frozenset([1, 33])
    FOLLOW_SEMI_in_myOption239 = frozenset([1])
    FOLLOW_WORD_in_myOption248 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_myOption259 = frozenset([13, 22, 28, 37])
    FOLLOW_RA_BR_in_myOption262 = frozenset([13, 22, 37])
    FOLLOW_DEFAULT_in_myOption275 = frozenset([1, 33])
    FOLLOW_SEMI_in_myOption278 = frozenset([1])
    FOLLOW_localOptions_in_mat305 = frozenset([16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_exps_in_mat318 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_mat327 = frozenset([1])
    FOLLOW_AT_RESULTS_in_statementFields352 = frozenset([5, 16, 17, 22, 23, 37, 38])
    FOLLOW_mResults_in_statementFields354 = frozenset([5])
    FOLLOW_AT_in_statementFields356 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_statementFields358 = frozenset([1])
    FOLLOW_AT_TESTS_in_statementFields376 = frozenset([5, 22, 27, 37])
    FOLLOW_testCases_in_statementFields378 = frozenset([5])
    FOLLOW_AT_in_statementFields380 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_statementFields382 = frozenset([1])
    FOLLOW_HASH_NAME_in_alias406 = frozenset([20])
    FOLLOW_LR_BR_in_alias408 = frozenset([31, 37])
    FOLLOW_WHITE_SPACE_in_alias410 = frozenset([31, 37])
    FOLLOW_RR_BR_in_alias413 = frozenset([15, 37])
    FOLLOW_WHITE_SPACE_in_alias415 = frozenset([15, 37])
    FOLLOW_EQ_in_alias418 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_WHITE_SPACE_in_alias420 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_exps_in_alias423 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_alias425 = frozenset([1])
    FOLLOW_expVal_in_exps444 = frozenset([33])
    FOLLOW_SEMI_in_exps446 = frozenset([1])
    FOLLOW_LS_BR_in_expVal464 = frozenset([16, 20, 21, 30, 36, 38])
    FOLLOW_expVal_in_expVal475 = frozenset([32])
    FOLLOW_RS_BR_in_expVal477 = frozenset([16, 20, 21, 24, 25, 26, 30, 34, 36, 37, 38])
    FOLLOW_opt_in_expVal486 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal500 = frozenset([1])
    FOLLOW_LR_BR_in_expVal511 = frozenset([16, 20, 21, 30, 36, 38])
    FOLLOW_expVal_in_expVal522 = frozenset([31])
    FOLLOW_RR_BR_in_expVal524 = frozenset([16, 20, 21, 24, 25, 26, 30, 34, 36, 37, 38])
    FOLLOW_opt_in_expVal533 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal558 = frozenset([1])
    FOLLOW_WORD_in_expVal576 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal587 = frozenset([1])
    FOLLOW_VAR_NAME_in_expVal598 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal609 = frozenset([1])
    FOLLOW_HASH_NAME_in_expVal620 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal641 = frozenset([1])
    FOLLOW_REGEX_in_expVal662 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal671 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_subExp692 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_expVal_in_subExp695 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_subExp705 = frozenset([24, 37])
    FOLLOW_OR_in_subExp708 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_WHITE_SPACE_in_subExp718 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_expVal_in_subExp721 = frozenset([1])
    FOLLOW_QSTN_in_opt750 = frozenset([1])
    FOLLOW_STAR_in_opt759 = frozenset([1])
    FOLLOW_PLUS_in_opt770 = frozenset([1])
    FOLLOW_testCase_in_testCases803 = frozenset([22, 27, 37])
    FOLLOW_testCases_in_testCases807 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase843 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_testCase854 = frozenset([22, 27, 28, 37])
    FOLLOW_RA_BR_in_testCase857 = frozenset([22, 27, 37])
    FOLLOW_QUOTE_STRING_in_testCase872 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase881 = frozenset([1])
    FOLLOW_NEWLINE_in_mResults902 = frozenset([16, 17, 22, 23, 37, 38])
    FOLLOW_mResult_in_mResults907 = frozenset([16, 17, 22, 23, 37, 38])
    FOLLOW_mResults_in_mResults911 = frozenset([1])
    FOLLOW_NEWLINE_in_mResults918 = frozenset([1, 22])
    FOLLOW_labels_in_mResult940 = frozenset([19])
    FOLLOW_LC_BR_in_mResult942 = frozenset([16, 17, 27, 36, 37])
    FOLLOW_resultant_in_mResult944 = frozenset([29])
    FOLLOW_RC_BR_in_mResult946 = frozenset([1])
    FOLLOW_results_in_resultant963 = frozenset([1])
    FOLLOW_label_in_labels984 = frozenset([11])
    FOLLOW_labelsRest_in_labels986 = frozenset([1])
    FOLLOW_label_in_labels995 = frozenset([1])
    FOLLOW_COMMA_in_labelsRest1012 = frozenset([16, 17, 23, 37, 38])
    FOLLOW_labels_in_labelsRest1014 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_label1034 = frozenset([23, 37])
    FOLLOW_NUM_in_label1037 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1039 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1047 = frozenset([16, 37])
    FOLLOW_HASH_NAME_in_label1050 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1052 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1060 = frozenset([17, 37])
    FOLLOW_KLEENE_in_label1063 = frozenset([23])
    FOLLOW_NUM_in_label1065 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1067 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1075 = frozenset([37, 38])
    FOLLOW_WORD_in_label1078 = frozenset([23])
    FOLLOW_NUM_in_label1080 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1082 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1090 = frozenset([37, 38])
    FOLLOW_WORD_in_label1093 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label1095 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_results1114 = frozenset([16, 17, 27, 36, 37])
    FOLLOW_result_in_results1117 = frozenset([16, 17, 27, 36, 37])
    FOLLOW_results_in_results1121 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_results1128 = frozenset([1, 37])
    FOLLOW_QUOTE_STRING_in_result1146 = frozenset([1])
    FOLLOW_VAR_NAME_in_result1153 = frozenset([1])
    FOLLOW_HASH_NAME_in_result1160 = frozenset([1])
    FOLLOW_KLEENE_in_result1167 = frozenset([23])
    FOLLOW_NUM_in_result1169 = frozenset([18])
    FOLLOW_LA_BR_in_result1171 = frozenset([16, 17, 27, 28, 36, 37])
    FOLLOW_results_in_result1175 = frozenset([28])
    FOLLOW_RA_BR_in_result1177 = frozenset([20])
    FOLLOW_LR_BR_in_result1179 = frozenset([16, 17, 27, 31, 36, 37])
    FOLLOW_results_in_result1183 = frozenset([31])
    FOLLOW_RR_BR_in_result1185 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SpeakPythonLexer", SpeakPythonParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
