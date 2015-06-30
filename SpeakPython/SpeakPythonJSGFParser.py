# $ANTLR 3.4 SpeakPythonJSGF.g 2015-06-16 19:11:48

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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




class SpeakPythonJSGFParser(Parser):
    grammarFileName = "SpeakPythonJSGF.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(SpeakPythonJSGFParser, self).__init__(input, state, *args, **kwargs)

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

    rules = [];
    aliasRules = {};

    parseFailed = False;



    # $ANTLR start "prog"
    # SpeakPythonJSGF.g:37:1: prog : s ( NEWLINE | WHITE_SPACE )* EOF ;
    def prog(self, ):

        self.optionVals['wordRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['varRegex'] = '[a-zA-Z0-9_\\+\\.\\-]+';
        self.optionVals['wordDelim'] = '[ ,/]+';

        try:
            try:
                # SpeakPythonJSGF.g:44:2: ( s ( NEWLINE | WHITE_SPACE )* EOF )
                # SpeakPythonJSGF.g:44:4: s ( NEWLINE | WHITE_SPACE )* EOF
                pass 
                self._state.following.append(self.FOLLOW_s_in_prog36)
                self.s()

                self._state.following.pop()

                # SpeakPythonJSGF.g:44:6: ( NEWLINE | WHITE_SPACE )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == NEWLINE or LA1_0 == WHITE_SPACE) :
                        alt1 = 1


                    if alt1 == 1:
                        # SpeakPythonJSGF.g:
                        pass 
                        if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                            self.input.consume()
                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse




                    else:
                        break #loop1


                self.match(self.input, EOF, self.FOLLOW_EOF_in_prog47)

                #action start
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "prog"



    # $ANTLR start "s"
    # SpeakPythonJSGF.g:47:1: s : ( ( WHITE_SPACE | NEWLINE )* mat s | ( WHITE_SPACE | NEWLINE )* alias s | ( WHITE_SPACE | NEWLINE )* globalOptions s |);
    def s(self, ):
        mat1 = None




        try:
            try:
                # SpeakPythonJSGF.g:51:2: ( ( WHITE_SPACE | NEWLINE )* mat s | ( WHITE_SPACE | NEWLINE )* alias s | ( WHITE_SPACE | NEWLINE )* globalOptions s |)
                alt5 = 4
                alt5 = self.dfa5.predict(self.input)
                if alt5 == 1:
                    # SpeakPythonJSGF.g:51:4: ( WHITE_SPACE | NEWLINE )* mat s
                    pass 
                    # SpeakPythonJSGF.g:51:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop2
                        alt2 = 2
                        LA2_0 = self.input.LA(1)

                        if (LA2_0 == NEWLINE or LA2_0 == WHITE_SPACE) :
                            alt2 = 1


                        if alt2 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop2


                    self._state.following.append(self.FOLLOW_mat_in_s74)
                    mat1 = self.mat()

                    self._state.following.pop()

                    #action start
                    self.rules.append(mat1); 
                    #action end


                    self._state.following.append(self.FOLLOW_s_in_s78)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 2:
                    # SpeakPythonJSGF.g:52:4: ( WHITE_SPACE | NEWLINE )* alias s
                    pass 
                    # SpeakPythonJSGF.g:52:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop3
                        alt3 = 2
                        LA3_0 = self.input.LA(1)

                        if (LA3_0 == NEWLINE or LA3_0 == WHITE_SPACE) :
                            alt3 = 1


                        if alt3 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop3


                    self._state.following.append(self.FOLLOW_alias_in_s93)
                    self.alias()

                    self._state.following.pop()

                    #action start
                    #action end


                    self._state.following.append(self.FOLLOW_s_in_s97)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 3:
                    # SpeakPythonJSGF.g:53:4: ( WHITE_SPACE | NEWLINE )* globalOptions s
                    pass 
                    # SpeakPythonJSGF.g:53:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop4
                        alt4 = 2
                        LA4_0 = self.input.LA(1)

                        if (LA4_0 == NEWLINE or LA4_0 == WHITE_SPACE) :
                            alt4 = 1


                        if alt4 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop4


                    self._state.following.append(self.FOLLOW_globalOptions_in_s112)
                    self.globalOptions()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_s_in_s114)
                    self.s()

                    self._state.following.pop()


                elif alt5 == 4:
                    # SpeakPythonJSGF.g:54:4: 
                    pass 
                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "s"



    # $ANTLR start "globalOptions"
    # SpeakPythonJSGF.g:57:1: globalOptions : AT_GLOBAL_OPTIONS myOptions AT ;
    def globalOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:58:2: ( AT_GLOBAL_OPTIONS myOptions AT )
                # SpeakPythonJSGF.g:58:4: AT_GLOBAL_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_GLOBAL_OPTIONS, self.FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions130)

                self._state.following.append(self.FOLLOW_myOptions_in_globalOptions132)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_globalOptions134)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "globalOptions"



    # $ANTLR start "localOptions"
    # SpeakPythonJSGF.g:61:1: localOptions : AT_OPTIONS myOptions AT ;
    def localOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:62:2: ( AT_OPTIONS myOptions AT )
                # SpeakPythonJSGF.g:62:4: AT_OPTIONS myOptions AT
                pass 
                self.match(self.input, AT_OPTIONS, self.FOLLOW_AT_OPTIONS_in_localOptions145)

                #action start
                self.optionValsBackup = self.optionVals; self.optionVals = self.optionValsBackup.copy(); 
                #action end


                self._state.following.append(self.FOLLOW_myOptions_in_localOptions149)
                self.myOptions()

                self._state.following.pop()

                self.match(self.input, AT, self.FOLLOW_AT_in_localOptions151)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "localOptions"



    # $ANTLR start "myOptions"
    # SpeakPythonJSGF.g:65:1: myOptions : ( ( WHITE_SPACE | NEWLINE )* myOption myOptions | ( WHITE_SPACE | NEWLINE )* );
    def myOptions(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:66:2: ( ( WHITE_SPACE | NEWLINE )* myOption myOptions | ( WHITE_SPACE | NEWLINE )* )
                alt8 = 2
                alt8 = self.dfa8.predict(self.input)
                if alt8 == 1:
                    # SpeakPythonJSGF.g:66:4: ( WHITE_SPACE | NEWLINE )* myOption myOptions
                    pass 
                    # SpeakPythonJSGF.g:66:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == NEWLINE or LA6_0 == WHITE_SPACE) :
                            alt6 = 1


                        if alt6 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop6


                    self._state.following.append(self.FOLLOW_myOption_in_myOptions171)
                    self.myOption()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_myOptions_in_myOptions173)
                    self.myOptions()

                    self._state.following.pop()


                elif alt8 == 2:
                    # SpeakPythonJSGF.g:67:4: ( WHITE_SPACE | NEWLINE )*
                    pass 
                    # SpeakPythonJSGF.g:67:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop7
                        alt7 = 2
                        LA7_0 = self.input.LA(1)

                        if (LA7_0 == NEWLINE or LA7_0 == WHITE_SPACE) :
                            alt7 = 1


                        if alt7 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop7


                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOptions"



    # $ANTLR start "myOption"
    # SpeakPythonJSGF.g:70:1: myOption : ( WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )? | WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )? );
    def myOption(self, ):
        WORD2 = None
        REGEX3 = None
        WORD4 = None

        try:
            try:
                # SpeakPythonJSGF.g:71:2: ( WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )? | WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )? )
                alt17 = 2
                alt17 = self.dfa17.predict(self.input)
                if alt17 == 1:
                    # SpeakPythonJSGF.g:71:4: WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* REGEX ( SEMI )?
                    pass 
                    WORD2 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption198)

                    # SpeakPythonJSGF.g:71:9: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop9
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if (LA9_0 == NEWLINE or LA9_0 == WHITE_SPACE) :
                            alt9 = 1


                        if alt9 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop9


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption209)

                    # SpeakPythonJSGF.g:71:37: ( RA_BR )?
                    alt10 = 2
                    LA10_0 = self.input.LA(1)

                    if (LA10_0 == RA_BR) :
                        alt10 = 1
                    if alt10 == 1:
                        # SpeakPythonJSGF.g:71:38: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption212)




                    # SpeakPythonJSGF.g:71:46: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop11
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == NEWLINE or LA11_0 == WHITE_SPACE) :
                            alt11 = 1


                        if alt11 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop11


                    REGEX3 = self.match(self.input, REGEX, self.FOLLOW_REGEX_in_myOption225)

                    # SpeakPythonJSGF.g:71:77: ( SEMI )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == SEMI) :
                        alt12 = 1
                    if alt12 == 1:
                        # SpeakPythonJSGF.g:71:78: SEMI
                        pass 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption228)




                    #action start
                    self.optionVals[WORD2.text] = REGEX3.text[1:-2]; 
                    #action end



                elif alt17 == 2:
                    # SpeakPythonJSGF.g:72:4: WORD ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* DEFAULT ( SEMI )?
                    pass 
                    WORD4 = self.match(self.input, WORD, self.FOLLOW_WORD_in_myOption237)

                    # SpeakPythonJSGF.g:72:9: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop13
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if (LA13_0 == NEWLINE or LA13_0 == WHITE_SPACE) :
                            alt13 = 1


                        if alt13 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop13


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_myOption248)

                    # SpeakPythonJSGF.g:72:37: ( RA_BR )?
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if (LA14_0 == RA_BR) :
                        alt14 = 1
                    if alt14 == 1:
                        # SpeakPythonJSGF.g:72:38: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_myOption251)




                    # SpeakPythonJSGF.g:72:46: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop15
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == NEWLINE or LA15_0 == WHITE_SPACE) :
                            alt15 = 1


                        if alt15 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop15


                    self.match(self.input, DEFAULT, self.FOLLOW_DEFAULT_in_myOption264)

                    # SpeakPythonJSGF.g:72:79: ( SEMI )?
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == SEMI) :
                        alt16 = 1
                    if alt16 == 1:
                        # SpeakPythonJSGF.g:72:80: SEMI
                        pass 
                        self.match(self.input, SEMI, self.FOLLOW_SEMI_in_myOption267)




                    #action start
                    self.optionVals[WORD4.text] = self.defaultOptionVals[WORD4.text]; 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "myOption"



    # $ANTLR start "mat"
    # SpeakPythonJSGF.g:76:1: mat returns [matR] : ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields ;
    def mat(self, ):
        matR = None


        exps5 = None




        try:
            try:
                # SpeakPythonJSGF.g:80:2: ( ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields )
                # SpeakPythonJSGF.g:80:4: ( localOptions ( WHITE_SPACE | NEWLINE )* )? exps statementFields
                pass 
                # SpeakPythonJSGF.g:80:4: ( localOptions ( WHITE_SPACE | NEWLINE )* )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == AT_OPTIONS) :
                    alt19 = 1
                if alt19 == 1:
                    # SpeakPythonJSGF.g:80:5: localOptions ( WHITE_SPACE | NEWLINE )*
                    pass 
                    self._state.following.append(self.FOLLOW_localOptions_in_mat294)
                    self.localOptions()

                    self._state.following.pop()

                    # SpeakPythonJSGF.g:80:18: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop18
                        alt18 = 2
                        LA18_0 = self.input.LA(1)

                        if (LA18_0 == NEWLINE or LA18_0 == WHITE_SPACE) :
                            alt18 = 1


                        if alt18 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop18





                self._state.following.append(self.FOLLOW_exps_in_mat307)
                exps5 = self.exps()

                self._state.following.pop()

                #action start
                self.optionVals = self.optionValsBackup; 
                #action end


                self._state.following.append(self.FOLLOW_statementFields_in_mat316)
                self.statementFields()

                self._state.following.pop()

                #action start
                matR =  exps5 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return matR

    # $ANTLR end "mat"



    # $ANTLR start "statementFields"
    # SpeakPythonJSGF.g:86:1: statementFields : ( ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields | ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields |);
    def statementFields(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:87:2: ( ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields | ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields |)
                alt22 = 3
                alt22 = self.dfa22.predict(self.input)
                if alt22 == 1:
                    # SpeakPythonJSGF.g:87:4: ( WHITE_SPACE | NEWLINE )* AT_RESULTS mResults AT statementFields
                    pass 
                    # SpeakPythonJSGF.g:87:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop20
                        alt20 = 2
                        LA20_0 = self.input.LA(1)

                        if (LA20_0 == NEWLINE or LA20_0 == WHITE_SPACE) :
                            alt20 = 1


                        if alt20 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop20


                    self.match(self.input, AT_RESULTS, self.FOLLOW_AT_RESULTS_in_statementFields341)

                    self._state.following.append(self.FOLLOW_mResults_in_statementFields343)
                    self.mResults()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields345)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields347)
                    self.statementFields()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt22 == 2:
                    # SpeakPythonJSGF.g:89:4: ( WHITE_SPACE | NEWLINE )* AT_TESTS testCases AT statementFields
                    pass 
                    # SpeakPythonJSGF.g:89:4: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop21
                        alt21 = 2
                        LA21_0 = self.input.LA(1)

                        if (LA21_0 == NEWLINE or LA21_0 == WHITE_SPACE) :
                            alt21 = 1


                        if alt21 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop21


                    self.match(self.input, AT_TESTS, self.FOLLOW_AT_TESTS_in_statementFields365)

                    self._state.following.append(self.FOLLOW_testCases_in_statementFields367)
                    self.testCases()

                    self._state.following.pop()

                    self.match(self.input, AT, self.FOLLOW_AT_in_statementFields369)

                    self._state.following.append(self.FOLLOW_statementFields_in_statementFields371)
                    self.statementFields()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt22 == 3:
                    # SpeakPythonJSGF.g:91:4: 
                    pass 
                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "statementFields"



    # $ANTLR start "alias"
    # SpeakPythonJSGF.g:94:1: alias returns [aliasR] : HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields ;
    def alias(self, ):
        aliasR = None


        HASH_NAME6 = None
        exps7 = None


        try:
            try:
                # SpeakPythonJSGF.g:95:2: ( HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields )
                # SpeakPythonJSGF.g:95:4: HASH_NAME LR_BR ( WHITE_SPACE )* RR_BR ( WHITE_SPACE )* EQ ( WHITE_SPACE )* exps statementFields
                pass 
                HASH_NAME6 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_alias395)

                self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_alias397)

                # SpeakPythonJSGF.g:95:20: ( WHITE_SPACE )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == WHITE_SPACE) :
                        alt23 = 1


                    if alt23 == 1:
                        # SpeakPythonJSGF.g:95:20: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias399)


                    else:
                        break #loop23


                self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_alias402)

                # SpeakPythonJSGF.g:95:39: ( WHITE_SPACE )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == WHITE_SPACE) :
                        alt24 = 1


                    if alt24 == 1:
                        # SpeakPythonJSGF.g:95:39: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias404)


                    else:
                        break #loop24


                self.match(self.input, EQ, self.FOLLOW_EQ_in_alias407)

                # SpeakPythonJSGF.g:95:55: ( WHITE_SPACE )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == WHITE_SPACE) :
                        alt25 = 1


                    if alt25 == 1:
                        # SpeakPythonJSGF.g:95:55: WHITE_SPACE
                        pass 
                        self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_alias409)


                    else:
                        break #loop25


                self._state.following.append(self.FOLLOW_exps_in_alias412)
                exps7 = self.exps()

                self._state.following.pop()

                self._state.following.append(self.FOLLOW_statementFields_in_alias414)
                self.statementFields()

                self._state.following.pop()

                #action start
                self.aliasRules[HASH_NAME6.text[1:]] = exps7; 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return aliasR

    # $ANTLR end "alias"



    # $ANTLR start "exps"
    # SpeakPythonJSGF.g:99:1: exps returns [expsR=''] : expVal SEMI ;
    def exps(self, ):
        expsR = ''


        expVal8 = None


        try:
            try:
                # SpeakPythonJSGF.g:100:2: ( expVal SEMI )
                # SpeakPythonJSGF.g:100:4: expVal SEMI
                pass 
                self._state.following.append(self.FOLLOW_expVal_in_exps433)
                expVal8 = self.expVal()

                self._state.following.pop()

                self.match(self.input, SEMI, self.FOLLOW_SEMI_in_exps435)

                #action start
                expsR =  expVal8 + ""; 
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expsR

    # $ANTLR end "exps"



    # $ANTLR start "expVal"
    # SpeakPythonJSGF.g:104:1: expVal returns [expValR=''] : ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp );
    def expVal(self, ):
        expValR = ''


        w1 = None
        HASH_NAME15 = None
        e1 = None

        e2 = None

        opt9 = None

        subExp10 = None

        opt11 = None

        subExp12 = None

        subExp13 = None

        subExp14 = None

        subExp16 = None


        try:
            try:
                # SpeakPythonJSGF.g:105:2: ( LS_BR e1= expVal RS_BR opt subExp | LR_BR e2= expVal RR_BR opt subExp |w1= WORD subExp | VAR_NAME subExp | HASH_NAME subExp | REGEX subExp )
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
                    nvae = NoViableAltException("", 26, 0, self.input)

                    raise nvae


                if alt26 == 1:
                    # SpeakPythonJSGF.g:105:4: LS_BR e1= expVal RS_BR opt subExp
                    pass 
                    self.match(self.input, LS_BR, self.FOLLOW_LS_BR_in_expVal453)

                    self._state.following.append(self.FOLLOW_expVal_in_expVal457)
                    e1 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RS_BR, self.FOLLOW_RS_BR_in_expVal459)

                    self._state.following.append(self.FOLLOW_opt_in_expVal461)
                    opt9 = self.opt()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_subExp_in_expVal463)
                    subExp10 = self.subExp()

                    self._state.following.pop()

                    #action start
                    expValR =  opt9[0] + e1 + opt9[1] + subExp10 
                    #action end



                elif alt26 == 2:
                    # SpeakPythonJSGF.g:108:4: LR_BR e2= expVal RR_BR opt subExp
                    pass 
                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_expVal474)

                    self._state.following.append(self.FOLLOW_expVal_in_expVal478)
                    e2 = self.expVal()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_expVal480)

                    self._state.following.append(self.FOLLOW_opt_in_expVal482)
                    opt11 = self.opt()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_subExp_in_expVal484)
                    subExp12 = self.subExp()

                    self._state.following.pop()

                    #action start
                    expValR =  opt11[0] + e2 + opt11[1] + subExp12 
                    #action end



                elif alt26 == 3:
                    # SpeakPythonJSGF.g:111:4: w1= WORD subExp
                    pass 
                    w1 = self.match(self.input, WORD, self.FOLLOW_WORD_in_expVal497)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal499)
                    subExp13 = self.subExp()

                    self._state.following.pop()

                    #action start
                    expValR =  w1.text + subExp13 
                    #action end



                elif alt26 == 4:
                    # SpeakPythonJSGF.g:114:4: VAR_NAME subExp
                    pass 
                    self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_expVal510)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal512)
                    subExp14 = self.subExp()

                    self._state.following.pop()

                    #action start
                    print "We're sorry, variables are not supported in JSGF at this time."; self.parseFailed = True; expValR =  subExp14 
                    #action end



                elif alt26 == 5:
                    # SpeakPythonJSGF.g:117:4: HASH_NAME subExp
                    pass 
                    HASH_NAME15 = self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_expVal523)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal525)
                    subExp16 = self.subExp()

                    self._state.following.pop()

                    #action start
                    name = HASH_NAME15.text[1:]; 
                    #action end


                    #action start
                    if (name not in self.aliasRules): print "The rule <" + name + "> does not exist before it is referenced."; 
                    #action end


                    #action start
                    expValR =  "<" + name + ">" + subExp16 
                    #action end



                elif alt26 == 6:
                    # SpeakPythonJSGF.g:122:4: REGEX subExp
                    pass 
                    self.match(self.input, REGEX, self.FOLLOW_REGEX_in_expVal546)

                    self._state.following.append(self.FOLLOW_subExp_in_expVal548)
                    self.subExp()

                    self._state.following.pop()

                    #action start
                    print "We're sorry, regex is not supported in JSGF at this time."; expValR =  "" 
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return expValR

    # $ANTLR end "expVal"



    # $ANTLR start "subExp"
    # SpeakPythonJSGF.g:127:1: subExp returns [subExpR=''] : ( ( WHITE_SPACE )* expVal | ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal |);
    def subExp(self, ):
        subExpR = ''


        expVal17 = None

        expVal18 = None


        try:
            try:
                # SpeakPythonJSGF.g:128:2: ( ( WHITE_SPACE )* expVal | ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal |)
                alt30 = 3
                alt30 = self.dfa30.predict(self.input)
                if alt30 == 1:
                    # SpeakPythonJSGF.g:128:4: ( WHITE_SPACE )* expVal
                    pass 
                    # SpeakPythonJSGF.g:128:4: ( WHITE_SPACE )*
                    while True: #loop27
                        alt27 = 2
                        LA27_0 = self.input.LA(1)

                        if (LA27_0 == WHITE_SPACE) :
                            alt27 = 1


                        if alt27 == 1:
                            # SpeakPythonJSGF.g:128:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp569)


                        else:
                            break #loop27


                    self._state.following.append(self.FOLLOW_expVal_in_subExp572)
                    expVal17 = self.expVal()

                    self._state.following.pop()

                    #action start
                    subExpR =  " " + expVal17 
                    #action end



                elif alt30 == 2:
                    # SpeakPythonJSGF.g:130:4: ( WHITE_SPACE )* OR ( WHITE_SPACE )* expVal
                    pass 
                    # SpeakPythonJSGF.g:130:4: ( WHITE_SPACE )*
                    while True: #loop28
                        alt28 = 2
                        LA28_0 = self.input.LA(1)

                        if (LA28_0 == WHITE_SPACE) :
                            alt28 = 1


                        if alt28 == 1:
                            # SpeakPythonJSGF.g:130:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp582)


                        else:
                            break #loop28


                    self.match(self.input, OR, self.FOLLOW_OR_in_subExp585)

                    # SpeakPythonJSGF.g:130:20: ( WHITE_SPACE )*
                    while True: #loop29
                        alt29 = 2
                        LA29_0 = self.input.LA(1)

                        if (LA29_0 == WHITE_SPACE) :
                            alt29 = 1


                        if alt29 == 1:
                            # SpeakPythonJSGF.g:130:20: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_subExp587)


                        else:
                            break #loop29


                    self._state.following.append(self.FOLLOW_expVal_in_subExp590)
                    expVal18 = self.expVal()

                    self._state.following.pop()

                    #action start
                    subExpR =  " | " + expVal18 
                    #action end



                elif alt30 == 3:
                    # SpeakPythonJSGF.g:131:4: 
                    pass 
                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return subExpR

    # $ANTLR end "subExp"



    # $ANTLR start "opt"
    # SpeakPythonJSGF.g:135:1: opt returns [optR=('(',')')] : ( QSTN | STAR | PLUS |);
    def opt(self, ):
        optR = ('(',')')


        try:
            try:
                # SpeakPythonJSGF.g:136:2: ( QSTN | STAR | PLUS |)
                alt31 = 4
                LA31 = self.input.LA(1)
                if LA31 == QSTN:
                    alt31 = 1
                elif LA31 == STAR:
                    alt31 = 2
                elif LA31 == PLUS:
                    alt31 = 3
                elif LA31 == HASH_NAME or LA31 == LR_BR or LA31 == LS_BR or LA31 == OR or LA31 == REGEX or LA31 == RR_BR or LA31 == RS_BR or LA31 == SEMI or LA31 == VAR_NAME or LA31 == WHITE_SPACE or LA31 == WORD:
                    alt31 = 4
                else:
                    nvae = NoViableAltException("", 31, 0, self.input)

                    raise nvae


                if alt31 == 1:
                    # SpeakPythonJSGF.g:136:4: QSTN
                    pass 
                    self.match(self.input, QSTN, self.FOLLOW_QSTN_in_opt614)

                    #action start
                    optR = ("[", "]") 
                    #action end



                elif alt31 == 2:
                    # SpeakPythonJSGF.g:137:4: STAR
                    pass 
                    self.match(self.input, STAR, self.FOLLOW_STAR_in_opt621)

                    #action start
                    optR = ("(", ")*") 
                    #action end



                elif alt31 == 3:
                    # SpeakPythonJSGF.g:138:4: PLUS
                    pass 
                    self.match(self.input, PLUS, self.FOLLOW_PLUS_in_opt628)

                    #action start
                    optR = ("(", ")+") 
                    #action end



                elif alt31 == 4:
                    # SpeakPythonJSGF.g:139:4: 
                    pass 
                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return optR

    # $ANTLR end "opt"



    # $ANTLR start "testCases"
    # SpeakPythonJSGF.g:142:1: testCases returns [testCasesR=[]] : ( ( NEWLINE | WHITE_SPACE )* testCase ts= testCases | ( NEWLINE | WHITE_SPACE )* );
    def testCases(self, ):
        testCasesR = []


        ts = None


        try:
            try:
                # SpeakPythonJSGF.g:143:2: ( ( NEWLINE | WHITE_SPACE )* testCase ts= testCases | ( NEWLINE | WHITE_SPACE )* )
                alt34 = 2
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # SpeakPythonJSGF.g:143:4: ( NEWLINE | WHITE_SPACE )* testCase ts= testCases
                    pass 
                    # SpeakPythonJSGF.g:143:4: ( NEWLINE | WHITE_SPACE )*
                    while True: #loop32
                        alt32 = 2
                        LA32_0 = self.input.LA(1)

                        if (LA32_0 == NEWLINE or LA32_0 == WHITE_SPACE) :
                            alt32 = 1


                        if alt32 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop32


                    self._state.following.append(self.FOLLOW_testCase_in_testCases659)
                    self.testCase()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_testCases_in_testCases663)
                    ts = self.testCases()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt34 == 2:
                    # SpeakPythonJSGF.g:145:4: ( NEWLINE | WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:145:4: ( NEWLINE | WHITE_SPACE )*
                    while True: #loop33
                        alt33 = 2
                        LA33_0 = self.input.LA(1)

                        if (LA33_0 == NEWLINE or LA33_0 == WHITE_SPACE) :
                            alt33 = 1


                        if alt33 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop33


                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCasesR

    # $ANTLR end "testCases"



    # $ANTLR start "testCase"
    # SpeakPythonJSGF.g:148:1: testCase returns [testCaseR=''] : (q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING |q3= QUOTE_STRING );
    def testCase(self, ):
        testCaseR = ''


        q1 = None
        q2 = None
        q3 = None

        try:
            try:
                # SpeakPythonJSGF.g:149:2: (q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING |q3= QUOTE_STRING )
                alt38 = 2
                alt38 = self.dfa38.predict(self.input)
                if alt38 == 1:
                    # SpeakPythonJSGF.g:149:4: q1= QUOTE_STRING ( WHITE_SPACE | NEWLINE )* EQ ( RA_BR )? ( WHITE_SPACE | NEWLINE )* q2= QUOTE_STRING
                    pass 
                    q1 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase699)

                    # SpeakPythonJSGF.g:149:20: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop35
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 == NEWLINE or LA35_0 == WHITE_SPACE) :
                            alt35 = 1


                        if alt35 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop35


                    self.match(self.input, EQ, self.FOLLOW_EQ_in_testCase710)

                    # SpeakPythonJSGF.g:149:48: ( RA_BR )?
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == RA_BR) :
                        alt36 = 1
                    if alt36 == 1:
                        # SpeakPythonJSGF.g:149:49: RA_BR
                        pass 
                        self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_testCase713)




                    # SpeakPythonJSGF.g:149:57: ( WHITE_SPACE | NEWLINE )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == NEWLINE or LA37_0 == WHITE_SPACE) :
                            alt37 = 1


                        if alt37 == 1:
                            # SpeakPythonJSGF.g:
                            pass 
                            if self.input.LA(1) == NEWLINE or self.input.LA(1) == WHITE_SPACE:
                                self.input.consume()
                                self._state.errorRecovery = False


                            else:
                                mse = MismatchedSetException(None, self.input)
                                raise mse




                        else:
                            break #loop37


                    q2 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase728)

                    #action start
                    #action end



                elif alt38 == 2:
                    # SpeakPythonJSGF.g:150:4: q3= QUOTE_STRING
                    pass 
                    q3 = self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_testCase737)

                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return testCaseR

    # $ANTLR end "testCase"



    # $ANTLR start "mResults"
    # SpeakPythonJSGF.g:155:1: mResults : ( ( NEWLINE )* m1= mResult ms= mResults | ( NEWLINE )* );
    def mResults(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:156:2: ( ( NEWLINE )* m1= mResult ms= mResults | ( NEWLINE )* )
                alt41 = 2
                alt41 = self.dfa41.predict(self.input)
                if alt41 == 1:
                    # SpeakPythonJSGF.g:156:4: ( NEWLINE )* m1= mResult ms= mResults
                    pass 
                    # SpeakPythonJSGF.g:156:4: ( NEWLINE )*
                    while True: #loop39
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == NEWLINE) :
                            alt39 = 1


                        if alt39 == 1:
                            # SpeakPythonJSGF.g:156:4: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_mResults754)


                        else:
                            break #loop39


                    self._state.following.append(self.FOLLOW_mResult_in_mResults759)
                    self.mResult()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_mResults_in_mResults763)
                    self.mResults()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt41 == 2:
                    # SpeakPythonJSGF.g:157:4: ( NEWLINE )*
                    pass 
                    # SpeakPythonJSGF.g:157:4: ( NEWLINE )*
                    while True: #loop40
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == NEWLINE) :
                            alt40 = 1


                        if alt40 == 1:
                            # SpeakPythonJSGF.g:157:4: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_mResults770)


                        else:
                            break #loop40


                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "mResults"



    # $ANTLR start "mResult"
    # SpeakPythonJSGF.g:161:1: mResult : ls= labels LC_BR results RC_BR ;
    def mResult(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:162:2: (ls= labels LC_BR results RC_BR )
                # SpeakPythonJSGF.g:162:4: ls= labels LC_BR results RC_BR
                pass 
                self._state.following.append(self.FOLLOW_labels_in_mResult788)
                self.labels()

                self._state.following.pop()

                self.match(self.input, LC_BR, self.FOLLOW_LC_BR_in_mResult790)

                self._state.following.append(self.FOLLOW_results_in_mResult792)
                self.results()

                self._state.following.pop()

                self.match(self.input, RC_BR, self.FOLLOW_RC_BR_in_mResult794)

                #action start
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "mResult"



    # $ANTLR start "labels"
    # SpeakPythonJSGF.g:166:1: labels : (l1= label labelsRest |l2= label );
    def labels(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:167:2: (l1= label labelsRest |l2= label )
                alt42 = 2
                alt42 = self.dfa42.predict(self.input)
                if alt42 == 1:
                    # SpeakPythonJSGF.g:167:4: l1= label labelsRest
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels811)
                    self.label()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_labelsRest_in_labels813)
                    self.labelsRest()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt42 == 2:
                    # SpeakPythonJSGF.g:168:4: l2= label
                    pass 
                    self._state.following.append(self.FOLLOW_label_in_labels822)
                    self.label()

                    self._state.following.pop()

                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "labels"



    # $ANTLR start "labelsRest"
    # SpeakPythonJSGF.g:171:1: labelsRest : COMMA labels ;
    def labelsRest(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:172:2: ( COMMA labels )
                # SpeakPythonJSGF.g:172:4: COMMA labels
                pass 
                self.match(self.input, COMMA, self.FOLLOW_COMMA_in_labelsRest835)

                self._state.following.append(self.FOLLOW_labels_in_labelsRest837)
                self.labels()

                self._state.following.pop()

                #action start
                #action end





            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "labelsRest"



    # $ANTLR start "label"
    # SpeakPythonJSGF.g:176:1: label : ( ( WHITE_SPACE )* NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )* | ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD ( WHITE_SPACE )* );
    def label(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:177:2: ( ( WHITE_SPACE )* NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )* | ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )* | ( WHITE_SPACE )* WORD ( WHITE_SPACE )* )
                alt53 = 5
                alt53 = self.dfa53.predict(self.input)
                if alt53 == 1:
                    # SpeakPythonJSGF.g:177:4: ( WHITE_SPACE )* NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:177:4: ( WHITE_SPACE )*
                    while True: #loop43
                        alt43 = 2
                        LA43_0 = self.input.LA(1)

                        if (LA43_0 == WHITE_SPACE) :
                            alt43 = 1


                        if alt43 == 1:
                            # SpeakPythonJSGF.g:177:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label853)


                        else:
                            break #loop43


                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label856)

                    # SpeakPythonJSGF.g:177:21: ( WHITE_SPACE )*
                    while True: #loop44
                        alt44 = 2
                        LA44_0 = self.input.LA(1)

                        if (LA44_0 == WHITE_SPACE) :
                            alt44 = 1


                        if alt44 == 1:
                            # SpeakPythonJSGF.g:177:21: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label858)


                        else:
                            break #loop44


                    #action start
                    #action end



                elif alt53 == 2:
                    # SpeakPythonJSGF.g:178:4: ( WHITE_SPACE )* HASH_NAME ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:178:4: ( WHITE_SPACE )*
                    while True: #loop45
                        alt45 = 2
                        LA45_0 = self.input.LA(1)

                        if (LA45_0 == WHITE_SPACE) :
                            alt45 = 1


                        if alt45 == 1:
                            # SpeakPythonJSGF.g:178:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label866)


                        else:
                            break #loop45


                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_label869)

                    # SpeakPythonJSGF.g:178:27: ( WHITE_SPACE )*
                    while True: #loop46
                        alt46 = 2
                        LA46_0 = self.input.LA(1)

                        if (LA46_0 == WHITE_SPACE) :
                            alt46 = 1


                        if alt46 == 1:
                            # SpeakPythonJSGF.g:178:27: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label871)


                        else:
                            break #loop46


                    #action start
                    #action end



                elif alt53 == 3:
                    # SpeakPythonJSGF.g:179:4: ( WHITE_SPACE )* KLEENE NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:179:4: ( WHITE_SPACE )*
                    while True: #loop47
                        alt47 = 2
                        LA47_0 = self.input.LA(1)

                        if (LA47_0 == WHITE_SPACE) :
                            alt47 = 1


                        if alt47 == 1:
                            # SpeakPythonJSGF.g:179:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label879)


                        else:
                            break #loop47


                    self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_label882)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label884)

                    # SpeakPythonJSGF.g:179:28: ( WHITE_SPACE )*
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == WHITE_SPACE) :
                            alt48 = 1


                        if alt48 == 1:
                            # SpeakPythonJSGF.g:179:28: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label886)


                        else:
                            break #loop48


                    #action start
                    #action end



                elif alt53 == 4:
                    # SpeakPythonJSGF.g:180:4: ( WHITE_SPACE )* WORD NUM ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:180:4: ( WHITE_SPACE )*
                    while True: #loop49
                        alt49 = 2
                        LA49_0 = self.input.LA(1)

                        if (LA49_0 == WHITE_SPACE) :
                            alt49 = 1


                        if alt49 == 1:
                            # SpeakPythonJSGF.g:180:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label894)


                        else:
                            break #loop49


                    self.match(self.input, WORD, self.FOLLOW_WORD_in_label897)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_label899)

                    # SpeakPythonJSGF.g:180:26: ( WHITE_SPACE )*
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == WHITE_SPACE) :
                            alt50 = 1


                        if alt50 == 1:
                            # SpeakPythonJSGF.g:180:26: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label901)


                        else:
                            break #loop50


                    #action start
                    #action end



                elif alt53 == 5:
                    # SpeakPythonJSGF.g:181:4: ( WHITE_SPACE )* WORD ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:181:4: ( WHITE_SPACE )*
                    while True: #loop51
                        alt51 = 2
                        LA51_0 = self.input.LA(1)

                        if (LA51_0 == WHITE_SPACE) :
                            alt51 = 1


                        if alt51 == 1:
                            # SpeakPythonJSGF.g:181:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label909)


                        else:
                            break #loop51


                    self.match(self.input, WORD, self.FOLLOW_WORD_in_label912)

                    # SpeakPythonJSGF.g:181:22: ( WHITE_SPACE )*
                    while True: #loop52
                        alt52 = 2
                        LA52_0 = self.input.LA(1)

                        if (LA52_0 == WHITE_SPACE) :
                            alt52 = 1


                        if alt52 == 1:
                            # SpeakPythonJSGF.g:181:22: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_label914)


                        else:
                            break #loop52


                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "label"



    # $ANTLR start "results"
    # SpeakPythonJSGF.g:185:1: results : ( ( WHITE_SPACE )* result rs= results | ( WHITE_SPACE )* );
    def results(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:186:2: ( ( WHITE_SPACE )* result rs= results | ( WHITE_SPACE )* )
                alt56 = 2
                alt56 = self.dfa56.predict(self.input)
                if alt56 == 1:
                    # SpeakPythonJSGF.g:186:4: ( WHITE_SPACE )* result rs= results
                    pass 
                    # SpeakPythonJSGF.g:186:4: ( WHITE_SPACE )*
                    while True: #loop54
                        alt54 = 2
                        LA54_0 = self.input.LA(1)

                        if (LA54_0 == WHITE_SPACE) :
                            alt54 = 1


                        if alt54 == 1:
                            # SpeakPythonJSGF.g:186:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_results929)


                        else:
                            break #loop54


                    self._state.following.append(self.FOLLOW_result_in_results932)
                    self.result()

                    self._state.following.pop()

                    self._state.following.append(self.FOLLOW_results_in_results936)
                    self.results()

                    self._state.following.pop()

                    #action start
                    #action end



                elif alt56 == 2:
                    # SpeakPythonJSGF.g:187:4: ( WHITE_SPACE )*
                    pass 
                    # SpeakPythonJSGF.g:187:4: ( WHITE_SPACE )*
                    while True: #loop55
                        alt55 = 2
                        LA55_0 = self.input.LA(1)

                        if (LA55_0 == WHITE_SPACE) :
                            alt55 = 1


                        if alt55 == 1:
                            # SpeakPythonJSGF.g:187:4: WHITE_SPACE
                            pass 
                            self.match(self.input, WHITE_SPACE, self.FOLLOW_WHITE_SPACE_in_results943)


                        else:
                            break #loop55


                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "results"



    # $ANTLR start "result"
    # SpeakPythonJSGF.g:190:1: result : ( QUOTE_STRING | VAR_NAME | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR );
    def result(self, ):
        try:
            try:
                # SpeakPythonJSGF.g:191:2: ( QUOTE_STRING | VAR_NAME | HASH_NAME | KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR )
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
                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae


                if alt57 == 1:
                    # SpeakPythonJSGF.g:191:4: QUOTE_STRING
                    pass 
                    self.match(self.input, QUOTE_STRING, self.FOLLOW_QUOTE_STRING_in_result957)

                    #action start
                    #action end



                elif alt57 == 2:
                    # SpeakPythonJSGF.g:192:4: VAR_NAME
                    pass 
                    self.match(self.input, VAR_NAME, self.FOLLOW_VAR_NAME_in_result964)

                    #action start
                    #action end



                elif alt57 == 3:
                    # SpeakPythonJSGF.g:193:4: HASH_NAME
                    pass 
                    self.match(self.input, HASH_NAME, self.FOLLOW_HASH_NAME_in_result971)

                    #action start
                    #action end



                elif alt57 == 4:
                    # SpeakPythonJSGF.g:194:4: KLEENE NUM LA_BR r1= results RA_BR LR_BR r2= results RR_BR
                    pass 
                    self.match(self.input, KLEENE, self.FOLLOW_KLEENE_in_result978)

                    self.match(self.input, NUM, self.FOLLOW_NUM_in_result980)

                    self.match(self.input, LA_BR, self.FOLLOW_LA_BR_in_result982)

                    self._state.following.append(self.FOLLOW_results_in_result986)
                    self.results()

                    self._state.following.pop()

                    self.match(self.input, RA_BR, self.FOLLOW_RA_BR_in_result988)

                    self.match(self.input, LR_BR, self.FOLLOW_LR_BR_in_result990)

                    self._state.following.append(self.FOLLOW_results_in_result994)
                    self.results()

                    self._state.following.pop()

                    self.match(self.input, RR_BR, self.FOLLOW_RR_BR_in_result996)

                    #action start
                    #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "result"



    # lookup tables for DFA #5

    DFA5_eot = DFA.unpack(
        u"\10\uffff"
        )

    DFA5_eof = DFA.unpack(
        u"\2\5\6\uffff"
        )

    DFA5_min = DFA.unpack(
        u"\2\6\1\uffff\1\20\2\uffff\1\20\1\uffff"
        )

    DFA5_max = DFA.unpack(
        u"\2\46\1\uffff\1\46\2\uffff\1\46\1\uffff"
        )

    DFA5_accept = DFA.unpack(
        u"\2\uffff\1\1\1\uffff\1\3\1\4\1\uffff\1\2"
        )

    DFA5_special = DFA.unpack(
        u"\10\uffff"
        )


    DFA5_transition = [
        DFA.unpack(u"\1\4\1\2\10\uffff\1\3\3\uffff\2\2\1\1\7\uffff\1\2\5"
        u"\uffff\1\2\1\1\1\2"),
        DFA.unpack(u"\1\4\1\2\10\uffff\1\3\3\uffff\2\2\1\1\7\uffff\1\2\5"
        u"\uffff\1\2\1\1\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\3\uffff\1\6\1\2\2\uffff\1\2\5\uffff\1\2\2\uffff"
        u"\1\2\2\uffff\3\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\3\uffff\2\2\10\uffff\1\2\1\7\4\uffff\1\2\1\7\1"
        u"\2"),
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
        u"\4\uffff"
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
        u"\5\uffff"
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
        u"\4\uffff"
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
        u"\5\uffff"
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
        u"\4\uffff"
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
        u"\17\uffff"
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
        u"\10\uffff"
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
        u"\4\uffff"
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


 

    FOLLOW_s_in_prog36 = frozenset([22, 37])
    FOLLOW_EOF_in_prog47 = frozenset([1])
    FOLLOW_mat_in_s74 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s78 = frozenset([1])
    FOLLOW_alias_in_s93 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s97 = frozenset([1])
    FOLLOW_globalOptions_in_s112 = frozenset([6, 7, 16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_s_in_s114 = frozenset([1])
    FOLLOW_AT_GLOBAL_OPTIONS_in_globalOptions130 = frozenset([5, 22, 37, 38])
    FOLLOW_myOptions_in_globalOptions132 = frozenset([5])
    FOLLOW_AT_in_globalOptions134 = frozenset([1])
    FOLLOW_AT_OPTIONS_in_localOptions145 = frozenset([5, 22, 37, 38])
    FOLLOW_myOptions_in_localOptions149 = frozenset([5])
    FOLLOW_AT_in_localOptions151 = frozenset([1])
    FOLLOW_myOption_in_myOptions171 = frozenset([22, 37, 38])
    FOLLOW_myOptions_in_myOptions173 = frozenset([1])
    FOLLOW_WORD_in_myOption198 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_myOption209 = frozenset([22, 28, 30, 37])
    FOLLOW_RA_BR_in_myOption212 = frozenset([22, 30, 37])
    FOLLOW_REGEX_in_myOption225 = frozenset([1, 33])
    FOLLOW_SEMI_in_myOption228 = frozenset([1])
    FOLLOW_WORD_in_myOption237 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_myOption248 = frozenset([13, 22, 28, 37])
    FOLLOW_RA_BR_in_myOption251 = frozenset([13, 22, 37])
    FOLLOW_DEFAULT_in_myOption264 = frozenset([1, 33])
    FOLLOW_SEMI_in_myOption267 = frozenset([1])
    FOLLOW_localOptions_in_mat294 = frozenset([16, 20, 21, 22, 30, 36, 37, 38])
    FOLLOW_exps_in_mat307 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_mat316 = frozenset([1])
    FOLLOW_AT_RESULTS_in_statementFields341 = frozenset([5, 16, 17, 22, 23, 37, 38])
    FOLLOW_mResults_in_statementFields343 = frozenset([5])
    FOLLOW_AT_in_statementFields345 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_statementFields347 = frozenset([1])
    FOLLOW_AT_TESTS_in_statementFields365 = frozenset([5, 22, 27, 37])
    FOLLOW_testCases_in_statementFields367 = frozenset([5])
    FOLLOW_AT_in_statementFields369 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_statementFields371 = frozenset([1])
    FOLLOW_HASH_NAME_in_alias395 = frozenset([20])
    FOLLOW_LR_BR_in_alias397 = frozenset([31, 37])
    FOLLOW_WHITE_SPACE_in_alias399 = frozenset([31, 37])
    FOLLOW_RR_BR_in_alias402 = frozenset([15, 37])
    FOLLOW_WHITE_SPACE_in_alias404 = frozenset([15, 37])
    FOLLOW_EQ_in_alias407 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_WHITE_SPACE_in_alias409 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_exps_in_alias412 = frozenset([8, 9, 22, 37])
    FOLLOW_statementFields_in_alias414 = frozenset([1])
    FOLLOW_expVal_in_exps433 = frozenset([33])
    FOLLOW_SEMI_in_exps435 = frozenset([1])
    FOLLOW_LS_BR_in_expVal453 = frozenset([16, 20, 21, 30, 36, 38])
    FOLLOW_expVal_in_expVal457 = frozenset([32])
    FOLLOW_RS_BR_in_expVal459 = frozenset([16, 20, 21, 24, 25, 26, 30, 34, 36, 37, 38])
    FOLLOW_opt_in_expVal461 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal463 = frozenset([1])
    FOLLOW_LR_BR_in_expVal474 = frozenset([16, 20, 21, 30, 36, 38])
    FOLLOW_expVal_in_expVal478 = frozenset([31])
    FOLLOW_RR_BR_in_expVal480 = frozenset([16, 20, 21, 24, 25, 26, 30, 34, 36, 37, 38])
    FOLLOW_opt_in_expVal482 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal484 = frozenset([1])
    FOLLOW_WORD_in_expVal497 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal499 = frozenset([1])
    FOLLOW_VAR_NAME_in_expVal510 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal512 = frozenset([1])
    FOLLOW_HASH_NAME_in_expVal523 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal525 = frozenset([1])
    FOLLOW_REGEX_in_expVal546 = frozenset([16, 20, 21, 24, 30, 36, 37, 38])
    FOLLOW_subExp_in_expVal548 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_subExp569 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_expVal_in_subExp572 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_subExp582 = frozenset([24, 37])
    FOLLOW_OR_in_subExp585 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_WHITE_SPACE_in_subExp587 = frozenset([16, 20, 21, 30, 36, 37, 38])
    FOLLOW_expVal_in_subExp590 = frozenset([1])
    FOLLOW_QSTN_in_opt614 = frozenset([1])
    FOLLOW_STAR_in_opt621 = frozenset([1])
    FOLLOW_PLUS_in_opt628 = frozenset([1])
    FOLLOW_testCase_in_testCases659 = frozenset([22, 27, 37])
    FOLLOW_testCases_in_testCases663 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase699 = frozenset([15, 22, 37])
    FOLLOW_EQ_in_testCase710 = frozenset([22, 27, 28, 37])
    FOLLOW_RA_BR_in_testCase713 = frozenset([22, 27, 37])
    FOLLOW_QUOTE_STRING_in_testCase728 = frozenset([1])
    FOLLOW_QUOTE_STRING_in_testCase737 = frozenset([1])
    FOLLOW_NEWLINE_in_mResults754 = frozenset([16, 17, 22, 23, 37, 38])
    FOLLOW_mResult_in_mResults759 = frozenset([16, 17, 22, 23, 37, 38])
    FOLLOW_mResults_in_mResults763 = frozenset([1])
    FOLLOW_NEWLINE_in_mResults770 = frozenset([1, 22])
    FOLLOW_labels_in_mResult788 = frozenset([19])
    FOLLOW_LC_BR_in_mResult790 = frozenset([16, 17, 27, 29, 36, 37])
    FOLLOW_results_in_mResult792 = frozenset([29])
    FOLLOW_RC_BR_in_mResult794 = frozenset([1])
    FOLLOW_label_in_labels811 = frozenset([11])
    FOLLOW_labelsRest_in_labels813 = frozenset([1])
    FOLLOW_label_in_labels822 = frozenset([1])
    FOLLOW_COMMA_in_labelsRest835 = frozenset([16, 17, 23, 37, 38])
    FOLLOW_labels_in_labelsRest837 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_label853 = frozenset([23, 37])
    FOLLOW_NUM_in_label856 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label858 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label866 = frozenset([16, 37])
    FOLLOW_HASH_NAME_in_label869 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label871 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label879 = frozenset([17, 37])
    FOLLOW_KLEENE_in_label882 = frozenset([23])
    FOLLOW_NUM_in_label884 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label886 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label894 = frozenset([37, 38])
    FOLLOW_WORD_in_label897 = frozenset([23])
    FOLLOW_NUM_in_label899 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label901 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label909 = frozenset([37, 38])
    FOLLOW_WORD_in_label912 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_label914 = frozenset([1, 37])
    FOLLOW_WHITE_SPACE_in_results929 = frozenset([16, 17, 27, 36, 37])
    FOLLOW_result_in_results932 = frozenset([16, 17, 27, 36, 37])
    FOLLOW_results_in_results936 = frozenset([1])
    FOLLOW_WHITE_SPACE_in_results943 = frozenset([1, 37])
    FOLLOW_QUOTE_STRING_in_result957 = frozenset([1])
    FOLLOW_VAR_NAME_in_result964 = frozenset([1])
    FOLLOW_HASH_NAME_in_result971 = frozenset([1])
    FOLLOW_KLEENE_in_result978 = frozenset([23])
    FOLLOW_NUM_in_result980 = frozenset([18])
    FOLLOW_LA_BR_in_result982 = frozenset([16, 17, 27, 28, 36, 37])
    FOLLOW_results_in_result986 = frozenset([28])
    FOLLOW_RA_BR_in_result988 = frozenset([20])
    FOLLOW_LR_BR_in_result990 = frozenset([16, 17, 27, 31, 36, 37])
    FOLLOW_results_in_result994 = frozenset([31])
    FOLLOW_RR_BR_in_result996 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("SpeakPythonJSGFLexer", SpeakPythonJSGFParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
