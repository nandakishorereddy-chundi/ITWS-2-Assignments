#!/usr/bin/python
from window import ChildWindow
from window import AppWindow
from window import *
from point import Point
from window import BadArgumentError
import re

""" Unicode enabled text widget,"""
class TextBox(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        #assert(parent is not None)
        #assert(isinstance(parent, (AppWindow)))
        #assert(isinstance(top_left, Point))
	self.fg=0
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)

    def setText(self, text):
    	self.text=text
	self.fg=1

    def getText(self):
        if self.fg!=0:
    	    return self.text
	else:
	    return " "

    def validate(self,validator):
        validator(self.text)

def isaNumber(text):
	text=text.replace(" ","")
	cnt=0
	for i in text:
	 	if i>='0' and i<='9':
			cnt+=1
	 	else:
	  		break
	if len(text)==cnt:
	  	return True
	else:
	   return False

def isaFloat(text):
	""" Assuming that float will always contain a point in it"""
	text=text.replace(" ","")
	cnt=0
	for i in text:
	   if i>='0' and i<='9':
	      cnt+=1
	   else:
	      break

	if len(text)==cnt+1:
	   return True
	else:
	   return False


def isaURL(text):
	x=re.findall("http://.+",text)
	y=re.findall("https://.+",text)
	if len(x)==1 or len(y)==1:
		return True
	else:
		return False
