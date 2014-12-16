#!/usr/bin/python
from point import Point

focus_list=[]

class BadArgumentError(Exception):
    def __init__(self, cause):
        Exception.__init__(self, cause)


class Window(object):
    STATE_NORMAL    = 0x1
    STATE_MINIMIZED = 0x2
    STATE_MAXIMIZED = 0x4

    FOCUS_FOREGROUND = 0x1
    FOCUS_BACKGROUND = 0x2

    def __init__(self, parent, title, top_left, w, h):
    	self.parent = parent
        self.title = title
        self.top_left = top_left
        self.height = h
        self.width = w
        self.state = Window.STATE_NORMAL
	self.focus=self.FOCUS_FOREGROUND
	self.condition=None
	if len(focus_list)!=0:
		temp=focus_list.pop()
		temp.focus=Window.FOCUS_BACKGROUND
	focus_list.append(self)

    def get_title(self):
        return self.title
    
    def resize(self, w, h):
        self.width = w
        self.height = h

    def get_size(self):
        return (self.width, self.height)

    def get_state(self):
    	return self.state

    # def set_state(self, state):
    # 	if state != Window.STATE_NORMAL or state != Window.STATE_MINIMIZED or \
    # 	                                   state != Window.STATE_MAXIMIZED:
    #         state = Window.STATE_NORMAL
        
    #     self.state = state

    def __str__(self):
    	return "(Window: (%s), (width: %d, height: %d)" % (self.title, self.width, self.height)


    def setFocus(self):
	   temp=focus_list.pop()
	   if(temp==self):
	       focus_list.append(self)
	       return False
	   else:
	       temp.focus=Window.FOCUS_BACKGROUND
	       self.focus=Window.FOCUS_FOREGROUND
	       focus_list.append(self)
	       return True

    def hasFocus(self):
           if(self.focus==1):
	      return True
	   else:
	      return False
    
    def minimize(self):
           if self.focus==1:
	      """ Because window with focus should not be in minimized state """
	      pass
	   elif(self.state!=2):
	      self.state=Window.STATE_MINIMIZED
	      return True
	   else:
	      return False

    def maximize(self):
    	   temp=focus_list.pop()
	   if temp==self:
	      focus_list.append(temp)
	      return False
	   else:
	      temp.focus=Window.FOCUS_BACKGROUND
              self.state=Window.STATE_MAXIMIZED
	      focus_list.append(self)
	      return True


class Container(Window):
    def __init__(self, parent, title, top_left, w, h):
        Window.__init__(self, parent, title, top_left, w, h)
        self.children = []
        self.parents=[]
	return

    def addChildWindow(self, childWindow):
        for i in self.children:
            if i.title==childWindow.title:
                raise BadArgumentError("Expecting a valid child window instance")
        for i in self.parents:
            if i.title==childWindow.title and i.parent==childWindow.parent:
                raise BadArgumentError("Expecting a valid child window instance")

        if (isinstance(childWindow, ChildWindow) and not isinstance(childWindow,Container)) or isinstance(childWindow,AppWindow):
            self.children.append(childWindow)
            self.parent.append(childWindow.parent)
            return
        raise BadArgumentError("Expecting a valid child window instance")
    
    def childIterator(self):
        class Childiterator:
            def __init__(self,container):
	        self.l=iter(container.children)
		self.container=container
		self.__iter__()

	    def __iter__(self):
		return iter(self.container.children)

            def next(self):
		try:
			return next(self.l)
		except(IndexError):
			raise StopIteration
	return Childiterator(self)
        

class ChildWindow(Window):
    def __init__(self, parent, title, top_left, w, h):
        if parent is None or not isinstance(parent, Container):
            raise BadArgumentError("Expecting a valid parent window instance")

        Window.__init__(self, parent, title, top_left, w, h)


class AppWindow(Container):
    def __init__(self, title, top_left = Point(0, 0), w=40, h=40):
        Container.__init__(self, None, title, top_left, w, h)
