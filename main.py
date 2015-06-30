import sys;
import os;
from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer

def execute(s):
    print s;

try:
    recog = SpeakPythonRecognizer(execute, "linux")
    recog.setDebug(1);
    while True:
        recog.recognize();

except KeyboardInterrupt:
        print "Qutting.";
