import sys;
import os;
from StringIO import StringIO

#speech
from SpeakPython.SpeakPythonRecognizer import SpeakPythonRecognizer

#execute commands
from subprocess import call

#browser control
from PyQt4.QtCore import Qt
import spynner

browser = None

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
	#browser.show()
	browser.load(url=u""+url, load_timeout=30000, tries=1)

debug_stream = StringIO()
browser = spynner.Browser(debug_level=spynner.DEBUG, debug_stream=debug_stream)
browser.show()
browser.load(url="http://weather.niwa.co.nz/auckland", load_timeout=30000, tries=1)
try:
	recog = SpeakPythonRecognizer(execute, "linux")
	recog.setDebug(1);
	while True:
		recog.recognize();

except KeyboardInterrupt:
		print("Qutting.")
