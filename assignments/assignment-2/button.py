#!/usr/bin/python
from window import *
from window import AppWindow
from point import Point
from window import BadArgumentError
from dialogbox import DialogBox

class Button(ChildWindow):
    def __init__(self, parent, title, top_left, w, h):
        #assert(parent is not None)
        #assert(isinstance(parent, (AppWindow)))
        #assert(isinstance(top_left, Point))
        if parent is None or not isinstance(parent, Container):
        	raise BadArgumentError("Expecting a valid parent window")
        
        Window.__init__(self, parent, title, top_left, w, h)

class OK(Button):
	def __init__(self,parent,title,top_left,w,h):
		Button.__init__(self,parent,title,top_left,w,h)
	def click(self):
		self.parent.accept

class Cancel(Button):
	def __init__(self,parent,title,top_left,w,h):
		Button.__init__(self,parent,title,top_left,w,h)
	def click(self):
		self.parent.cancel

class RadioButtonGroup(Container):
    def __init__(self,parent,title,top_left,w,h):
        Container.__init__(self,parent,title,top_left,w,h)
    def addRadioButton(self,radiobutton):
        if isinstance(radiobutton,RadioButton):
            self.children.append(RadioButton)
            return
        raise BadArgumentError("Expecting a valid RadioButton instance")

class RadioButton(Button):
	RADIO_ACTIVE=0x1
	RADIO_INACTIVE=0x0
	def __init__(self,parent,title,top_left,w,h):
		if parent is None or not isinstance(parent,Container):
        		raise BadArgumentError("Expecting a valid parent window")
					
		Window.__init__(self,parent,title,top_left,w,h)

	def click(self):
		if self.state==RadioButton.RADIO_ACTIVE:
			return False
		else:
			for i in self.parent.children:
				i.state=RadioButton.RADIO_INACTIVE
			self.state=RadioButton.RADIO_ACTIVE
			return True

	def getState(self):
		return self.state
				
