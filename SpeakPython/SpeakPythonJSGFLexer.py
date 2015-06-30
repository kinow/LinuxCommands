# $ANTLR 3.4 SpeakPythonJSGF.g 2015-06-16 19:11:49

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


class SpeakPythonJSGFLexer(Lexer):

    grammarFileName = "SpeakPythonJSGF.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(SpeakPythonJSGFLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
            )






    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:197:8: ( ( '\\r' )? '\\n' )
            # SpeakPythonJSGF.g:197:10: ( '\\r' )? '\\n'
            pass 
            # SpeakPythonJSGF.g:197:10: ( '\\r' )?
            alt1 = 2
            LA1_0 = self.input.LA(1)

            if (LA1_0 == 13) :
                alt1 = 1
            if alt1 == 1:
                # SpeakPythonJSGF.g:197:11: '\\r'
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

            # SpeakPythonJSGF.g:199:6: ( '/' ( . )+ '/r' )
            # SpeakPythonJSGF.g:199:8: '/' ( . )+ '/r'
            pass 
            self.match(47)

            # SpeakPythonJSGF.g:199:11: ( . )+
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
                    # SpeakPythonJSGF.g:199:11: .
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

            # SpeakPythonJSGF.g:200:8: ( '//' (~ ( '\\r' | '\\n' ) )* NEWLINE )
            # SpeakPythonJSGF.g:200:10: '//' (~ ( '\\r' | '\\n' ) )* NEWLINE
            pass 
            self.match("//")


            # SpeakPythonJSGF.g:200:15: (~ ( '\\r' | '\\n' ) )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 12) or (14 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # SpeakPythonJSGF.g:
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

            # SpeakPythonJSGF.g:202:5: ( '?' )
            # SpeakPythonJSGF.g:202:7: '?'
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

            # SpeakPythonJSGF.g:203:6: ( '~' )
            # SpeakPythonJSGF.g:203:8: '~'
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

            # SpeakPythonJSGF.g:204:8: ( '<-' )
            # SpeakPythonJSGF.g:204:10: '<-'
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

            # SpeakPythonJSGF.g:205:6: ( '->' )
            # SpeakPythonJSGF.g:205:8: '->'
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

            # SpeakPythonJSGF.g:206:7: ( '...' )
            # SpeakPythonJSGF.g:206:9: '...'
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

            # SpeakPythonJSGF.g:207:6: ( '[' )
            # SpeakPythonJSGF.g:207:8: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "LS_BR"



    # $ANTLR start "LC_BR"
    def mLC_BR(self, ):
        try:
            _type = LC_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:208:6: ( '{' )
            # SpeakPythonJSGF.g:208:8: '{'
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

            # SpeakPythonJSGF.g:209:6: ( '}' )
            # SpeakPythonJSGF.g:209:8: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RC_BR"



    # $ANTLR start "RS_BR"
    def mRS_BR(self, ):
        try:
            _type = RS_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:210:6: ( ']' )
            # SpeakPythonJSGF.g:210:8: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "RS_BR"



    # $ANTLR start "LR_BR"
    def mLR_BR(self, ):
        try:
            _type = LR_BR
            _channel = DEFAULT_CHANNEL

            # SpeakPythonJSGF.g:211:6: ( '(' )
            # SpeakPythonJSGF.g:211:8: '('
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

            # SpeakPythonJSGF.g:212:6: ( ')' )
            # SpeakPythonJSGF.g:212:8: ')'
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

            # SpeakPythonJSGF.g:213:6: ( '<' )
            # SpeakPythonJSGF.g:213:8: '<'
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

            # SpeakPythonJSGF.g:214:6: ( '>' )
            # SpeakPythonJSGF.g:214:8: '>'
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

            # SpeakPythonJSGF.g:215:3: ( '|' )
            # SpeakPythonJSGF.g:215:5: '|'
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

            # SpeakPythonJSGF.g:216:6: ( ',' )
            # SpeakPythonJSGF.g:216:8: ','
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

            # SpeakPythonJSGF.g:217:5: ( ';' )
            # SpeakPythonJSGF.g:217:7: ';'
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

            # SpeakPythonJSGF.g:218:3: ( '=' )
            # SpeakPythonJSGF.g:218:5: '='
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

            # SpeakPythonJSGF.g:219:9: ( '@tests' )
            # SpeakPythonJSGF.g:219:11: '@tests'
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

            # SpeakPythonJSGF.g:220:11: ( '@results' )
            # SpeakPythonJSGF.g:220:13: '@results'
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

            # SpeakPythonJSGF.g:221:18: ( '@globalOptions' )
            # SpeakPythonJSGF.g:221:20: '@globalOptions'
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

            # SpeakPythonJSGF.g:222:11: ( '@options' )
            # SpeakPythonJSGF.g:222:13: '@options'
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

            # SpeakPythonJSGF.g:223:8: ( 'default' )
            # SpeakPythonJSGF.g:223:10: 'default'
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

            # SpeakPythonJSGF.g:224:3: ( '@' )
            # SpeakPythonJSGF.g:224:5: '@'
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

            # SpeakPythonJSGF.g:225:5: ( '+' )
            # SpeakPythonJSGF.g:225:7: '+'
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

            # SpeakPythonJSGF.g:226:5: ( '*' )
            # SpeakPythonJSGF.g:226:7: '*'
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

            # SpeakPythonJSGF.g:227:7: ( 'k_' )
            # SpeakPythonJSGF.g:227:9: 'k_'
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

            # SpeakPythonJSGF.g:229:9: ( '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )* )
            # SpeakPythonJSGF.g:229:11: '$' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' )*
            pass 
            self.match(36)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPythonJSGF.g:229:33: ( 'a' .. 'z' | 'A' .. 'Z' )*
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if ((65 <= LA4_0 <= 90) or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # SpeakPythonJSGF.g:
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

            # SpeakPythonJSGF.g:230:10: ( '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )* )
            # SpeakPythonJSGF.g:230:12: '#' ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            pass 
            self.match(35)

            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # SpeakPythonJSGF.g:230:34: ( 'a' .. 'z' | 'A' .. 'Z' | '0' .. '9' )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((48 <= LA5_0 <= 57) or (65 <= LA5_0 <= 90) or (97 <= LA5_0 <= 122)) :
                    alt5 = 1


                if alt5 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    break #loop5




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

            # SpeakPythonJSGF.g:231:13: ( ( '\"' ( . )+ '\"' ) | ( '\\'' ( . )+ '\\'' ) )
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 34) :
                alt8 = 1
            elif (LA8_0 == 39) :
                alt8 = 2
            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae


            if alt8 == 1:
                # SpeakPythonJSGF.g:231:15: ( '\"' ( . )+ '\"' )
                pass 
                # SpeakPythonJSGF.g:231:15: ( '\"' ( . )+ '\"' )
                # SpeakPythonJSGF.g:231:16: '\"' ( . )+ '\"'
                pass 
                self.match(34)

                # SpeakPythonJSGF.g:231:19: ( . )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == 34) :
                        alt6 = 2
                    elif ((0 <= LA6_0 <= 33) or (35 <= LA6_0 <= 65535)) :
                        alt6 = 1


                    if alt6 == 1:
                        # SpeakPythonJSGF.g:231:19: .
                        pass 
                        self.matchAny()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self.match(34)





            elif alt8 == 2:
                # SpeakPythonJSGF.g:231:26: ( '\\'' ( . )+ '\\'' )
                pass 
                # SpeakPythonJSGF.g:231:26: ( '\\'' ( . )+ '\\'' )
                # SpeakPythonJSGF.g:231:27: '\\'' ( . )+ '\\''
                pass 
                self.match(39)

                # SpeakPythonJSGF.g:231:31: ( . )+
                cnt7 = 0
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 39) :
                        alt7 = 2
                    elif ((0 <= LA7_0 <= 38) or (40 <= LA7_0 <= 65535)) :
                        alt7 = 1


                    if alt7 == 1:
                        # SpeakPythonJSGF.g:231:31: .
                        pass 
                        self.matchAny()


                    else:
                        if cnt7 >= 1:
                            break #loop7

                        eee = EarlyExitException(7, self.input)
                        raise eee

                    cnt7 += 1


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

            # SpeakPythonJSGF.g:232:4: ( ( '0' .. '9' )+ )
            # SpeakPythonJSGF.g:232:6: ( '0' .. '9' )+
            pass 
            # SpeakPythonJSGF.g:232:6: ( '0' .. '9' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((48 <= LA9_0 <= 57)) :
                    alt9 = 1


                if alt9 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1




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

            # SpeakPythonJSGF.g:233:5: ( ( 'a' .. 'z' | 'A' .. 'Z' )+ )
            # SpeakPythonJSGF.g:233:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            pass 
            # SpeakPythonJSGF.g:233:7: ( 'a' .. 'z' | 'A' .. 'Z' )+
            cnt10 = 0
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((65 <= LA10_0 <= 90) or (97 <= LA10_0 <= 122)) :
                    alt10 = 1


                if alt10 == 1:
                    # SpeakPythonJSGF.g:
                    pass 
                    if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt10 >= 1:
                        break #loop10

                    eee = EarlyExitException(10, self.input)
                    raise eee

                cnt10 += 1




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

            # SpeakPythonJSGF.g:234:12: ( ' ' | '\\t' )
            # SpeakPythonJSGF.g:
            pass 
            if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WHITE_SPACE"



    def mTokens(self):
        # SpeakPythonJSGF.g:1:8: ( NEWLINE | REGEX | COMMENT | QSTN | TILDE | B_ARROW | ARROW | ELIPSE | LS_BR | LC_BR | RC_BR | RS_BR | LR_BR | RR_BR | LA_BR | RA_BR | OR | COMMA | SEMI | EQ | AT_TESTS | AT_RESULTS | AT_GLOBAL_OPTIONS | AT_OPTIONS | DEFAULT | AT | PLUS | STAR | KLEENE | VAR_NAME | HASH_NAME | QUOTE_STRING | NUM | WORD | WHITE_SPACE )
        alt11 = 35
        alt11 = self.dfa11.predict(self.input)
        if alt11 == 1:
            # SpeakPythonJSGF.g:1:10: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt11 == 2:
            # SpeakPythonJSGF.g:1:18: REGEX
            pass 
            self.mREGEX()



        elif alt11 == 3:
            # SpeakPythonJSGF.g:1:24: COMMENT
            pass 
            self.mCOMMENT()



        elif alt11 == 4:
            # SpeakPythonJSGF.g:1:32: QSTN
            pass 
            self.mQSTN()



        elif alt11 == 5:
            # SpeakPythonJSGF.g:1:37: TILDE
            pass 
            self.mTILDE()



        elif alt11 == 6:
            # SpeakPythonJSGF.g:1:43: B_ARROW
            pass 
            self.mB_ARROW()



        elif alt11 == 7:
            # SpeakPythonJSGF.g:1:51: ARROW
            pass 
            self.mARROW()



        elif alt11 == 8:
            # SpeakPythonJSGF.g:1:57: ELIPSE
            pass 
            self.mELIPSE()



        elif alt11 == 9:
            # SpeakPythonJSGF.g:1:64: LS_BR
            pass 
            self.mLS_BR()



        elif alt11 == 10:
            # SpeakPythonJSGF.g:1:70: LC_BR
            pass 
            self.mLC_BR()



        elif alt11 == 11:
            # SpeakPythonJSGF.g:1:76: RC_BR
            pass 
            self.mRC_BR()



        elif alt11 == 12:
            # SpeakPythonJSGF.g:1:82: RS_BR
            pass 
            self.mRS_BR()



        elif alt11 == 13:
            # SpeakPythonJSGF.g:1:88: LR_BR
            pass 
            self.mLR_BR()



        elif alt11 == 14:
            # SpeakPythonJSGF.g:1:94: RR_BR
            pass 
            self.mRR_BR()



        elif alt11 == 15:
            # SpeakPythonJSGF.g:1:100: LA_BR
            pass 
            self.mLA_BR()



        elif alt11 == 16:
            # SpeakPythonJSGF.g:1:106: RA_BR
            pass 
            self.mRA_BR()



        elif alt11 == 17:
            # SpeakPythonJSGF.g:1:112: OR
            pass 
            self.mOR()



        elif alt11 == 18:
            # SpeakPythonJSGF.g:1:115: COMMA
            pass 
            self.mCOMMA()



        elif alt11 == 19:
            # SpeakPythonJSGF.g:1:121: SEMI
            pass 
            self.mSEMI()



        elif alt11 == 20:
            # SpeakPythonJSGF.g:1:126: EQ
            pass 
            self.mEQ()



        elif alt11 == 21:
            # SpeakPythonJSGF.g:1:129: AT_TESTS
            pass 
            self.mAT_TESTS()



        elif alt11 == 22:
            # SpeakPythonJSGF.g:1:138: AT_RESULTS
            pass 
            self.mAT_RESULTS()



        elif alt11 == 23:
            # SpeakPythonJSGF.g:1:149: AT_GLOBAL_OPTIONS
            pass 
            self.mAT_GLOBAL_OPTIONS()



        elif alt11 == 24:
            # SpeakPythonJSGF.g:1:167: AT_OPTIONS
            pass 
            self.mAT_OPTIONS()



        elif alt11 == 25:
            # SpeakPythonJSGF.g:1:178: DEFAULT
            pass 
            self.mDEFAULT()



        elif alt11 == 26:
            # SpeakPythonJSGF.g:1:186: AT
            pass 
            self.mAT()



        elif alt11 == 27:
            # SpeakPythonJSGF.g:1:189: PLUS
            pass 
            self.mPLUS()



        elif alt11 == 28:
            # SpeakPythonJSGF.g:1:194: STAR
            pass 
            self.mSTAR()



        elif alt11 == 29:
            # SpeakPythonJSGF.g:1:199: KLEENE
            pass 
            self.mKLEENE()



        elif alt11 == 30:
            # SpeakPythonJSGF.g:1:206: VAR_NAME
            pass 
            self.mVAR_NAME()



        elif alt11 == 31:
            # SpeakPythonJSGF.g:1:215: HASH_NAME
            pass 
            self.mHASH_NAME()



        elif alt11 == 32:
            # SpeakPythonJSGF.g:1:225: QUOTE_STRING
            pass 
            self.mQUOTE_STRING()



        elif alt11 == 33:
            # SpeakPythonJSGF.g:1:238: NUM
            pass 
            self.mNUM()



        elif alt11 == 34:
            # SpeakPythonJSGF.g:1:242: WORD
            pass 
            self.mWORD()



        elif alt11 == 35:
            # SpeakPythonJSGF.g:1:247: WHITE_SPACE
            pass 
            self.mWHITE_SPACE()








    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\5\uffff\1\41\15\uffff\1\46\1\34\2\uffff\1\34\17\uffff\1\34\3\uffff"
        u"\1\57\1\uffff\1\34\1\37\1\uffff\3\34\1\64\1\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\65\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\11\1\uffff\1\0\2\uffff\1\55\15\uffff\1\147\1\145\2\uffff\1\137"
        u"\6\uffff\1\0\10\uffff\1\146\1\uffff\4\0\1\141\1\0\1\uffff\1\165"
        u"\1\154\1\164\1\101\1\uffff"
        )

    DFA11_max = DFA.unpack(
        u"\1\176\1\uffff\1\uffff\2\uffff\1\55\15\uffff\1\164\1\145\2\uffff"
        u"\1\137\6\uffff\1\uffff\10\uffff\1\146\1\uffff\4\uffff\1\141\1\uffff"
        u"\1\uffff\1\165\1\154\1\164\1\172\1\uffff"
        )

    DFA11_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\4\1\5\1\uffff\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\1\15\1\16\1\20\1\21\1\22\1\23\1\24\2\uffff\1\33\1\34\1\uffff"
        u"\1\36\1\37\1\40\1\41\1\42\1\43\1\uffff\1\2\1\6\1\17\1\25\1\26\1"
        u"\27\1\30\1\32\1\uffff\1\35\6\uffff\1\3\4\uffff\1\31"
        )

    DFA11_special = DFA.unpack(
        u"\2\uffff\1\3\33\uffff\1\1\12\uffff\1\2\1\5\1\4\1\6\1\uffff\1\0"
        u"\6\uffff"
        )


    DFA11_transition = [
        DFA.unpack(u"\1\35\1\1\2\uffff\1\1\22\uffff\1\35\1\uffff\1\32\1\31"
        u"\1\30\2\uffff\1\32\1\14\1\15\1\26\1\25\1\20\1\6\1\7\1\2\12\33\1"
        u"\uffff\1\21\1\5\1\22\1\16\1\3\1\23\32\34\1\10\1\uffff\1\13\3\uffff"
        u"\3\34\1\24\6\34\1\27\17\34\1\11\1\17\1\12\1\4"),
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

    # class definition for DFA #11

    class DFA11(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA11_46 = input.LA(1)

                s = -1
                if (LA11_46 == 13):
                    s = 42

                elif (LA11_46 == 10):
                    s = 43

                elif (LA11_46 == 47):
                    s = 41

                elif ((0 <= LA11_46 <= 9) or (11 <= LA11_46 <= 12) or (14 <= LA11_46 <= 46) or (48 <= LA11_46 <= 65535)):
                    s = 44

                else:
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 1: 
                LA11_30 = input.LA(1)

                s = -1
                if (LA11_30 == 47):
                    s = 41

                elif (LA11_30 == 13):
                    s = 42

                elif (LA11_30 == 10):
                    s = 43

                elif ((0 <= LA11_30 <= 9) or (11 <= LA11_30 <= 12) or (14 <= LA11_30 <= 46) or (48 <= LA11_30 <= 65535)):
                    s = 44

                if s >= 0:
                    return s
            el
            if s == 2: 
                LA11_41 = input.LA(1)

                s = -1
                if (LA11_41 == 114):
                    s = 46

                elif (LA11_41 == 13):
                    s = 42

                elif (LA11_41 == 10):
                    s = 43

                elif (LA11_41 == 47):
                    s = 41

                elif ((0 <= LA11_41 <= 9) or (11 <= LA11_41 <= 12) or (14 <= LA11_41 <= 46) or (48 <= LA11_41 <= 113) or (115 <= LA11_41 <= 65535)):
                    s = 44

                if s >= 0:
                    return s
            el
            if s == 3: 
                LA11_2 = input.LA(1)

                s = -1
                if (LA11_2 == 47):
                    s = 30

                elif ((0 <= LA11_2 <= 46) or (48 <= LA11_2 <= 65535)):
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 4: 
                LA11_43 = input.LA(1)

                s = -1
                if ((0 <= LA11_43 <= 65535)):
                    s = 31

                else:
                    s = 47

                if s >= 0:
                    return s
            el
            if s == 5: 
                LA11_42 = input.LA(1)

                s = -1
                if (LA11_42 == 10):
                    s = 43

                elif ((0 <= LA11_42 <= 9) or (11 <= LA11_42 <= 65535)):
                    s = 31

                if s >= 0:
                    return s
            el
            if s == 6: 
                LA11_44 = input.LA(1)

                s = -1
                if (LA11_44 == 13):
                    s = 42

                elif (LA11_44 == 10):
                    s = 43

                elif (LA11_44 == 47):
                    s = 41

                elif ((0 <= LA11_44 <= 9) or (11 <= LA11_44 <= 12) or (14 <= LA11_44 <= 46) or (48 <= LA11_44 <= 65535)):
                    s = 44

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 11, _s, input)
            self_.error(nvae)
            raise nvae

 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(SpeakPythonJSGFLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
