# $ANTLR 3.4 SpeakPython.g 2015-06-16 19:11:43

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


class SpeakPythonLexer(Lexer):

    grammarFileName = "SpeakPython.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SpeakPythonLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )






    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:283:8: ( ( '\\r' )? '\\n' )
            # SpeakPython.g:283:10: ( '\\r' )? '\\n'
            pass 
            # SpeakPython.g:283:10: ( '\\r' )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 13) :
                alt1 = 1
            if alt1 == 1:
                # SpeakPython.g:283:11: '\\r'
                pass 
                self.match(13)




            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "REGEX"
    def mREGEX(self, ):
        try:
            _type = REGEX
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:285:6: ( '/' ( . )+ '/r' )
            # SpeakPython.g:285:8: '/' ( . )+ '/r'
            pass 
            self.match(47)

            # SpeakPython.g:285:11: ( . )+
            cnt2 = 0
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 47) :
                    LA2_1 = self.input.LA(2)

                    if (LA2_1 == 114) :
                        alt2 = 2
                    elif ((0 <= LA2_1 <= 113) or (115 <= LA2_1 <= 65535)) :
                        alt2 = 1


                elif ((0 <= LA2_0 <= 46) or (48 <= LA2_0 <= 65535)) :
                    alt2 = 1


                if alt2 == 1:
                    # SpeakPython.g:285:11: .
                    pass 
                    self.matchAny()


                else:
                    if cnt2 >= 1:
                        break #loop2

                    eee = EarlyExitException(2, self.input)
                    raise eee

                cnt2 += 1


            self.match("/r")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REGEX"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:286:8: ( '//' (~ ( '\\r' | '\\n' ) )* NEWLINE )
            # SpeakPython.g:286:10: '//' (~ ( '\\r' | '\\n' ) )* NEWLINE
            pass 
            self.match("//")


            # SpeakPython.g:286:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # SpeakPython.g:
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop3


            self.mNEWLINE()


            #action start
            self.skip(); 
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "QSTN"
    def mQSTN(self, ):
        try:
            _type = QSTN
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:288:5: ( '?' )
            # SpeakPython.g:288:7: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QSTN"



    # $ANTLR start "TILDE"
    def mTILDE(self, ):
        try:
            _type = TILDE
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:289:6: ( '~' )
            # SpeakPython.g:289:8: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TILDE"



    # $ANTLR start "B_ARROW"
    def mB_ARROW(self, ):
        try:
            _type = B_ARROW
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:290:8: ( '<-' )
            # SpeakPython.g:290:10: '<-'
            pass 
            self.match("<-")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "B_ARROW"



    # $ANTLR start "ARROW"
    def mARROW(self, ):
        try:
            _type = ARROW
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:291:6: ( '->' )
            # SpeakPython.g:291:8: '->'
            pass 
            self.match("->")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ARROW"



    # $ANTLR start "ELIPSE"
    def mELIPSE(self, ):
        try:
            _type = ELIPSE
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:292:7: ( '...' )
            # SpeakPython.g:292:9: '...'
            pass 
            self.match("...")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "ELIPSE"



    # $ANTLR start "LS_BR"
    def mLS_BR(self, ):
        try:
            _type = LS_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:293:6: ( '[' )
            # SpeakPython.g:293:8: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LS_BR"



    # $ANTLR start "RS_BR"
    def mRS_BR(self, ):
        try:
            _type = RS_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:294:6: ( ']' )
            # SpeakPython.g:294:8: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RS_BR"



    # $ANTLR start "LC_BR"
    def mLC_BR(self, ):
        try:
            _type = LC_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:295:6: ( '{' )
            # SpeakPython.g:295:8: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LC_BR"



    # $ANTLR start "RC_BR"
    def mRC_BR(self, ):
        try:
            _type = RC_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:296:6: ( '}' )
            # SpeakPython.g:296:8: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RC_BR"



    # $ANTLR start "LR_BR"
    def mLR_BR(self, ):
        try:
            _type = LR_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:297:6: ( '(' )
            # SpeakPython.g:297:8: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LR_BR"



    # $ANTLR start "RR_BR"
    def mRR_BR(self, ):
        try:
            _type = RR_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:298:6: ( ')' )
            # SpeakPython.g:298:8: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RR_BR"



    # $ANTLR start "LA_BR"
    def mLA_BR(self, ):
        try:
            _type = LA_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:299:6: ( '<' )
            # SpeakPython.g:299:8: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LA_BR"



    # $ANTLR start "RA_BR"
    def mRA_BR(self, ):
        try:
            _type = RA_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:300:6: ( '>' )
            # SpeakPython.g:300:8: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RA_BR"



    # $ANTLR start "OR"
    def mOR(self, ):
        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:301:3: ( '|' )
            # SpeakPython.g:301:5: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "OR"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):
        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:302:6: ( ',' )
            # SpeakPython.g:302:8: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):
        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:303:5: ( ';' )
            # SpeakPython.g:303:7: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "EQ"
    def mEQ(self, ):
        try:
            _type = EQ
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:304:3: ( '=' )
            # SpeakPython.g:304:5: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "EQ"



    # $ANTLR start "AT_TESTS"
    def mAT_TESTS(self, ):
        try:
            _type = AT_TESTS
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:305:9: ( '@tests' )
            # SpeakPython.g:305:11: '@tests'
            pass 
            self.match("@tests")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_TESTS"



    # $ANTLR start "AT_RESULTS"
    def mAT_RESULTS(self, ):
        try:
            _type = AT_RESULTS
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:306:11: ( '@results' )
            # SpeakPython.g:306:13: '@results'
            pass 
            self.match("@results")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_RESULTS"



    # $ANTLR start "AT_GLOBAL_OPTIONS"
    def mAT_GLOBAL_OPTIONS(self, ):
        try:
            _type = AT_GLOBAL_OPTIONS
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:307:18: ( '@globalOptions' )
            # SpeakPython.g:307:20: '@globalOptions'
            pass 
            self.match("@globalOptions")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_GLOBAL_OPTIONS"



    # $ANTLR start "AT_OPTIONS"
    def mAT_OPTIONS(self, ):
        try:
            _type = AT_OPTIONS
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:308:11: ( '@options' )
            # SpeakPython.g:308:13: '@options'
            pass 
            self.match("@options")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT_OPTIONS"



    # $ANTLR start "DEFAULT"
    def mDEFAULT(self, ):
        try:
            _type = DEFAULT
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:309:8: ( 'default' )
            # SpeakPython.g:309:10: 'default'
            pass 
            self.match("default")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "DEFAULT"



    # $ANTLR start "AT"
    def mAT(self, ):
        try:
            _type = AT
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:310:3: ( '@' )
            # SpeakPython.g:310:5: '@'
            pass 
            self.match(64)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "AT"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):
        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:311:5: ( '+' )
            # SpeakPython.g:311:7: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "STAR"
    def mSTAR(self, ):
        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:312:5: ( '*' )
            # SpeakPython.g:312:7: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STAR"



    # $ANTLR start "KLEENE"
    def mKLEENE(self, ):
        try:
            _type = KLEENE
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:313:7: ( 'k_' )
            # SpeakPython.g:313:9: 'k_'
            pass 
            self.match("k_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "KLEENE"



    # $ANTLR start "VAR_NAME"
    def mVAR_NAME(self, ):
        try:
            _type = VAR_NAME
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:315:9: ( '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )* )
            # SpeakPython.g:315:11: '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )*
            pass 
            self.match(36)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPython.g:315:33: ( 'a' .. 'z' | 'A' .. 'Z' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((65 <= LA4_0 <= 90) or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # SpeakPython.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop4




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "VAR_NAME"



    # $ANTLR start "HASH_NAME"
    def mHASH_NAME(self, ):
        try:
            _type = HASH_NAME
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:316:10: ( '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '_' ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+ )* )
            # SpeakPython.g:316:12: '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* ( '_' ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+ )*
            pass 
            self.match(35)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPython.g:316:34: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # SpeakPython.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5


            # SpeakPython.g:316:63: ( '_' ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+ )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == 95) :
                    alt7 = 1


                if alt7 == 1:
                    # SpeakPython.g:316:64: '_' ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+
                    pass 
                    self.match(95)

                    # SpeakPython.g:316:67: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )+
                    cnt6 = 0
                    while True: #loop6
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if ((48 <= LA6_0 <= 57) or (65 <= LA6_0 <= 90) or (97 <= LA6_0 <= 122)) :
                            alt6 = 1


                        if alt6 == 1:
                            # SpeakPython.g:
                            pass 
                            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                                self.input.consume()
                            else:
                                mse = MismatchedSetException(None, self.input)
                                self.recover(mse)
                                raise mse




                        else:
                            if cnt6 >= 1:
                                break #loop6

                            eee = EarlyExitException(6, self.input)
                            raise eee

                        cnt6 += 1



                else:
                    break #loop7




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "HASH_NAME"



    # $ANTLR start "QUOTE_STRING"
    def mQUOTE_STRING(self, ):
        try:
            _type = QUOTE_STRING
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:317:13: ( ( '\"' ( . )+ '\"' ) | ( '\\'' ( . )+ '\\'' ) )
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 34) :
                alt10 = 1
            elif (LA10_0 == 39) :
                alt10 = 2
            else:
                nvae = NoViableAltException("", 10, 0, self.input)

                raise nvae


            if alt10 == 1:
                # SpeakPython.g:317:15: ( '\"' ( . )+ '\"' )
                pass 
                # SpeakPython.g:317:15: ( '\"' ( . )+ '\"' )
                # SpeakPython.g:317:16: '\"' ( . )+ '\"'
                pass 
                self.match(34)

                # SpeakPython.g:317:19: ( . )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 34) :
                        alt8 = 2
                    elif ((0 <= LA8_0 <= 33) or (35 <= LA8_0 <= 65535)) :
                        alt8 = 1


                    if alt8 == 1:
                        # SpeakPython.g:317:19: .
                        pass 
                        self.matchAny()


                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.match(34)





            elif alt10 == 2:
                # SpeakPython.g:317:26: ( '\\'' ( . )+ '\\'' )
                pass 
                # SpeakPython.g:317:26: ( '\\'' ( . )+ '\\'' )
                # SpeakPython.g:317:27: '\\'' ( . )+ '\\''
                pass 
                self.match(39)

                # SpeakPython.g:317:31: ( . )+
                cnt9 = 0
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 39) :
                        alt9 = 2
                    elif ((0 <= LA9_0 <= 38) or (40 <= LA9_0 <= 65535)) :
                        alt9 = 1


                    if alt9 == 1:
                        # SpeakPython.g:317:31: .
                        pass 
                        self.matchAny()


                    else:
                        if cnt9 >= 1:
                            break #loop9

                        eee = EarlyExitException(9, self.input)
                        raise eee

                    cnt9 += 1


                self.match(39)





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "QUOTE_STRING"



    # $ANTLR start "NUM"
    def mNUM(self, ):
        try:
            _type = NUM
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:318:4: ( ( '0' .. '9' )+ ( '.' ( '0' .. '9' )+ )? )
            # SpeakPython.g:318:6: ( '0' .. '9' )+ ( '.' ( '0' .. '9' )+ )?
            pass 
            # SpeakPython.g:318:6: ( '0' .. '9' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((48 <= LA11_0 <= 57)) :
                    alt11 = 1


                if alt11 == 1:
                    # SpeakPython.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1


            # SpeakPython.g:318:17: ( '.' ( '0' .. '9' )+ )?
            alt13 = 2
            LA13_0 = self.input.LA(1)

            if (LA13_0 == 46) :
                alt13 = 1
            if alt13 == 1:
                # SpeakPython.g:318:18: '.' ( '0' .. '9' )+
                pass 
                self.match(46)

                # SpeakPython.g:318:21: ( '0' .. '9' )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if ((48 <= LA12_0 <= 57)) :
                        alt12 = 1


                    if alt12 == 1:
                        # SpeakPython.g:
                        pass 
                        if (48 <= self.input.LA(1) <= 57):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1







            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NUM"



    # $ANTLR start "WORD"
    def mWORD(self, ):
        try:
            _type = WORD
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:319:5: ( ( 'a' .. 'z' | 'A' .. 'Z' )+ )
            # SpeakPython.g:319:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            pass 
            # SpeakPython.g:319:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            cnt14 = 0
            while True: #loop14
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((65 <= LA14_0 <= 90) or (97 <= LA14_0 <= 122)) :
                    alt14 = 1


                if alt14 == 1:
                    # SpeakPython.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt14 >= 1:
                        break #loop14

                    eee = EarlyExitException(14, self.input)
                    raise eee

                cnt14 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WORD"



    # $ANTLR start "WHITE_SPACE"
    def mWHITE_SPACE(self, ):
        try:
            _type = WHITE_SPACE
            _channel = DEFAULT_CHANNEL

            # SpeakPython.g:320:12: ( ' ' | '\\t' )
            alt15 = 2
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 32) :
                alt15 = 1
            elif (LA15_0 == 9) :
                alt15 = 2
            else:
                nvae = NoViableAltException("", 15, 0, self.input)

                raise nvae


            if alt15 == 1:
                # SpeakPython.g:320:14: ' '
                pass 
                self.match(32)


            elif alt15 == 2:
                # SpeakPython.g:320:18: '\\t'
                pass 
                self.match(9)

                #action start
                self.skip(); 
                #action end



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITE_SPACE"



    def mTokens(self):
        # SpeakPython.g:1:8: ( NEWLINE | REGEX | COMMENT | QSTN | TILDE | B_ARROW | ARROW | ELIPSE | LS_BR | RS_BR | LC_BR | RC_BR | LR_BR | RR_BR | LA_BR | RA_BR | OR | COMMA | SEMI | EQ | AT_TESTS | AT_RESULTS | AT_GLOBAL_OPTIONS | AT_OPTIONS | DEFAULT | AT | PLUS | STAR | KLEENE | VAR_NAME | HASH_NAME | QUOTE_STRING | NUM | WORD | WHITE_SPACE )
        alt16 = 35
        alt16 = self.dfa16.predict(self.input)
        if alt16 == 1:
            # SpeakPython.g:1:10: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt16 == 2:
            # SpeakPython.g:1:18: REGEX
            pass 
            self.mREGEX()



        elif alt16 == 3:
            # SpeakPython.g:1:24: COMMENT
            pass 
            self.mCOMMENT()



        elif alt16 == 4:
            # SpeakPython.g:1:32: QSTN
            pass 
            self.mQSTN()



        elif alt16 == 5:
            # SpeakPython.g:1:37: TILDE
            pass 
            self.mTILDE()



        elif alt16 == 6:
            # SpeakPython.g:1:43: B_ARROW
            pass 
            self.mB_ARROW()



        elif alt16 == 7:
            # SpeakPython.g:1:51: ARROW
            pass 
            self.mARROW()



        elif alt16 == 8:
            # SpeakPython.g:1:57: ELIPSE
            pass 
            self.mELIPSE()



        elif alt16 == 9:
            # SpeakPython.g:1:64: LS_BR
            pass 
            self.mLS_BR()



        elif alt16 == 10:
            # SpeakPython.g:1:70: RS_BR
            pass 
            self.mRS_BR()



        elif alt16 == 11:
            # SpeakPython.g:1:76: LC_BR
            pass 
            self.mLC_BR()



        elif alt16 == 12:
            # SpeakPython.g:1:82: RC_BR
            pass 
            self.mRC_BR()



        elif alt16 == 13:
            # SpeakPython.g:1:88: LR_BR
            pass 
            self.mLR_BR()



        elif alt16 == 14:
            # SpeakPython.g:1:94: RR_BR
            pass 
            self.mRR_BR()



        elif alt16 == 15:
            # SpeakPython.g:1:100: LA_BR
            pass 
            self.mLA_BR()



        elif alt16 == 16:
            # SpeakPython.g:1:106: RA_BR
            pass 
            self.mRA_BR()



        elif alt16 == 17:
            # SpeakPython.g:1:112: OR
            pass 
            self.mOR()



        elif alt16 == 18:
            # SpeakPython.g:1:115: COMMA
            pass 
            self.mCOMMA()



        elif alt16 == 19:
            # SpeakPython.g:1:121: SEMI
            pass 
            self.mSEMI()



        elif alt16 == 20:
            # SpeakPython.g:1:126: EQ
            pass 
            self.mEQ()



        elif alt16 == 21:
            # SpeakPython.g:1:129: AT_TESTS
            pass 
            self.mAT_TESTS()



        elif alt16 == 22:
            # SpeakPython.g:1:138: AT_RESULTS
            pass 
            self.mAT_RESULTS()



        elif alt16 == 23:
            # SpeakPython.g:1:149: AT_GLOBAL_OPTIONS
            pass 
            self.mAT_GLOBAL_OPTIONS()



        elif alt16 == 24:
            # SpeakPython.g:1:167: AT_OPTIONS
            pass 
            self.mAT_OPTIONS()



        elif alt16 == 25:
            # SpeakPython.g:1:178: DEFAULT
            pass 
            self.mDEFAULT()



        elif alt16 == 26:
            # SpeakPython.g:1:186: AT
            pass 
            self.mAT()



        elif alt16 == 27:
            # SpeakPython.g:1:189: PLUS
            pass 
            self.mPLUS()



        elif alt16 == 28:
            # SpeakPython.g:1:194: STAR
            pass 
            self.mSTAR()



        elif alt16 == 29:
            # SpeakPython.g:1:199: KLEENE
            pass 
            self.mKLEENE()



        elif alt16 == 30:
            # SpeakPython.g:1:206: VAR_NAME
            pass 
            self.mVAR_NAME()



        elif alt16 == 31:
            # SpeakPython.g:1:215: HASH_NAME
            pass 
            self.mHASH_NAME()



        elif alt16 == 32:
            # SpeakPython.g:1:225: QUOTE_STRING
            pass 
            self.mQUOTE_STRING()



        elif alt16 == 33:
            # SpeakPython.g:1:238: NUM
            pass 
            self.mNUM()



        elif alt16 == 34:
            # SpeakPython.g:1:242: WORD
            pass 
            self.mWORD()



        elif alt16 == 35:
            # SpeakPython.g:1:247: WHITE_SPACE
            pass 
            self.mWHITE_SPACE()








    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\5\uffff\1\41\15\uffff\1\46\1\34\2\uffff\1\34\17\uffff\1\34\3\uffff"
        u"\1\57\1\uffff\1\34\1\37\1\uffff\3\34\1\64\1\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\65\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\1\11\1\uffff\1\0\2\uffff\1\55\15\uffff\1\147\1\145\2\uffff\1\137"
        u"\6\uffff\1\0\10\uffff\1\146\1\uffff\4\0\1\141\1\0\1\uffff\1\165"
        u"\1\154\1\164\1\101\1\uffff"
        )

    DFA16_max = DFA.unpack(
        u"\1\176\1\uffff\1\uffff\2\uffff\1\55\15\uffff\1\164\1\145\2\uffff"
        u"\1\137\6\uffff\1\uffff\10\uffff\1\146\1\uffff\4\uffff\1\141\1\uffff"
        u"\1\uffff\1\165\1\154\1\164\1\172\1\uffff"
        )

    DFA16_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\4\1\5\1\uffff\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\1\15\1\16\1\20\1\21\1\22\1\23\1\24\2\uffff\1\33\1\34\1\uffff"
        u"\1\36\1\37\1\40\1\41\1\42\1\43\1\uffff\1\2\1\6\1\17\1\25\1\26\1"
        u"\27\1\30\1\32\1\uffff\1\35\6\uffff\1\3\4\uffff\1\31"
        )

    DFA16_special = DFA.unpack(
        u"\2\uffff\1\3\33\uffff\1\1\12\uffff\1\2\1\5\1\0\1\6\1\uffff\1\4"
        u"\6\uffff"
        )


    DFA16_transition = [
        DFA.unpack(u"\1\35\1\1\2\uffff\1\1\22\uffff\1\35\1\uffff\1\32\1\31"
        u"\1\30\2\uffff\1\32\1\14\1\15\1\26\1\25\1\20\1\6\1\7\1\2\12\33\1"
        u"\uffff\1\21\1\5\1\22\1\16\1\3\1\23\32\34\1\10\1\uffff\1\11\3\uffff"
        u"\3\34\1\24\6\34\1\27\17\34\1\12\1\17\1\13\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\57\37\1\36\uffd0\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44\7\uffff\1\45\2\uffff\1\43\1\uffff\1\42"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\1\53\2\54\1\52\41\54\1\51\uffd0\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\1\53\2\54\1\52\41\54\1\51\102\54\1\56\uff8d"
        u"\54"),
        DFA.unpack(u"\12\37\1\53\ufff5\37"),
        DFA.unpack(u"\0\37"),
        DFA.unpack(u"\12\54\1\53\2\54\1\52\41\54\1\51\uffd0\54"),
        DFA.unpack(u"\1\60"),
        DFA.unpack(u"\12\54\1\53\2\54\1\52\41\54\1\51\uffd0\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\32\34\6\uffff\32\34"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA16_43 = input.LA(1)

                s = -1
                if ((0 <= LA16_43 <= 65535)):
                    s = 31

                else:
                    s = 47

                if s >= 0:
                    return s
            el
            if s == 1: 
                LA16_30 = input.LA(1)

                s = -1
                if (LA16_30 == 47):
                    s = 41

                elif (LA16_30 == 13):
                    s = 42

                elif (LA16_30 == 10):
                    s = 43

                elif ((0 <= LA16_30 <= 9) or (11 <= LA16_30 <= 12) or (14 <= LA16_30 <= 46) or (48 <= LA16_30 <= 65535)):
                    s = 44

                if s >= 0:
                    return s
            el
            if s == 2: 
                LA16_41 = input.LA(1)

                s = -1
                if (LA16_41 == 114):
                    s = 46

                elif (LA16_41 == 13):
                    s = 42

                elif (LA16_41 == 10):
                    s = 43

                elif (LA16_41 == 47):
                    s = 41

                elif ((0 <= LA16_41 <= 9) or (11 <= LA16_41 <= 12) or (14 <= LA16_41 <= 46) or (48 <= LA16_41 <= 113) or (115 <= LA16_41 <= 65535)):
                    s = 44

                if s >= 0:
                    return s
            el
            if s == 3: 
                LA16_2 = input.LA(1)

                s = -1
                if (LA16_2 == 47):
                    s = 30

                elif ((0 <= LA16_2 <= 46) or (48 <= LA16_2 <= 65535)):
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 4: 
                LA16_46 = input.LA(1)

                s = -1
                if (LA16_46 == 13):
                    s = 42

                elif (LA16_46 == 10):
                    s = 43

                elif (LA16_46 == 47):
                    s = 41

                elif ((0 <= LA16_46 <= 9) or (11 <= LA16_46 <= 12) or (14 <= LA16_46 <= 46) or (48 <= LA16_46 <= 65535)):
                    s = 44

                else:
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 5: 
                LA16_42 = input.LA(1)

                s = -1
                if (LA16_42 == 10):
                    s = 43

                elif ((0 <= LA16_42 <= 9) or (11 <= LA16_42 <= 65535)):
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 6: 
                LA16_44 = input.LA(1)

                s = -1
                if (LA16_44 == 13):
                    s = 42

                elif (LA16_44 == 10):
                    s = 43

                elif (LA16_44 == 47):
                    s = 41

                elif ((0 <= LA16_44 <= 9) or (11 <= LA16_44 <= 12) or (14 <= LA16_44 <= 46) or (48 <= LA16_44 <= 65535)):
                    s = 44

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 16, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SpeakPythonLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
