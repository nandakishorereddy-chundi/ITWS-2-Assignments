from window import Window, Container, AppWindow, ChildWindow
from point import Point
from window import BadArgumentError

class DialogBox(Container, ChildWindow):
    STATE_ACCEPT=0x1
    STATE_CANCEL=0x0
    def __init__(self, parent, title, top_left, w, h):
    	assert(parent is not None)
    	assert(isinstance(parent, (AppWindow)))
        assert(isinstance(top_left, Point))
        Container.__init__(self, parent, title, top_left, w, h)

    def accept(self):
    	self.state=DialogBox.STATE_ACCEPT

    def cancel(self):
    	self.state=DialogBox.STATE_CANCEL

    def getState(self):
	return self.state
