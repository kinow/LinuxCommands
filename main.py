import sys;
import os;

#speech
from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer

#execute commands
from subprocess import call

#browser control
import telnetlib

tn = telnetlib.Telnet("localhost", 32000)

def execute(s):
	exec(s)

def execute2(s):
	print("Calling " + s + " master")
	call(s);

def makeUrl(s):
	baseUrl = 'http://weather.niwa.co.nz/'
	city = s.replace(' ', '_')
	return baseUrl + city

def weather(s):
	print("Calling NIWA API for " + s)
	url = makeUrl(s)
	print("URL: " + url)
	tn.write("window.location='"+url+"'" + "\n")

def dashboard():
	print("Opening Dashboard")

def quit():
	sys.exit(0)

try:
	recog = SpeakPythonRecognizer(execute, "linux")
	recog.setDebug(1);
	while True:
		recog.recognize();

except KeyboardInterrupt:
		print("Qutting.")
