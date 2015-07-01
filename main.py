import sys;
import os;
from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer
from subprocess import call
def execute(s):
    exec(s)

def execute2(s):
    print "Calling " + s + " master"
    call(s);

def weather(s):
    print "Calling NIWA API for " + s

try:
    recog = SpeakPythonRecognizer(execute, "linux")
    recog.setDebug(1);
    while True:
        recog.recognize();

except KeyboardInterrupt:
        print "Qutting.";
