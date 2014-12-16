from window import Window, Container, ChildWindow
from window import AppWindow
from dialogbox import DialogBox
from button import Button
from point import Point
from textbox import *

def appwin_test():
    app_win = AppWindow("AppWin", Point(2, 5), 20, 140)
    bt = Button(app_win, "Btn", Point(20, 20), 109, 10)
    assert(app_win.get_title() == "AppWin")
    assert(app_win.get_size() == (20, 140))

def dialog_testing():
    app_win = AppWindow("AppWin", Point(2, 5), 200, 100)
    dlg = DialogBox(app_win, "dialogbox", Point(100, 50), 4, 5)
    assert(dlg.get_title() == "dialogbox")
    assert(dlg.get_size() == (4, 5))
    dlg.accept()
    assert(dlg.state == 0x1)
    dlg.cancel()
    assert(dlg.state == 0x0)

def testing_containers():
	app_win = AppWindow("AppWin", Point(100, 100), 400, 400)
	ctn = Container(app_win, "Test Container",Point(75, 75), 100, 100)
	assert(ctn.parent == app_win)
	ch1 = ChildWindow(ctn, "First Child", Point(50, 50), 50, 50)
	ctn.addChildWindow(ch1)
	assert(ch1.focus == Window.FOCUS_FOREGROUND)	
	ch2 = ChildWindow(ctn, "Second Child", Point(60, 60), 70, 20)
	assert(ch2.focus == Window.FOCUS_FOREGROUND)
	ctn.addChildWindow(ch2)
	assert(ch2.focus == Window.FOCUS_FOREGROUND)
	assert(ch1.focus == Window.FOCUS_BACKGROUND)
	child_it = ctn.childIterator()
	
	assert(ch2.state == Window.STATE_NORMAL)
	assert(ch1.state == Window.STATE_NORMAL)
	ch1.maximize()
	assert(ch1.state == Window.STATE_MAXIMIZED)
	ch1.setFocus()
#	assert(ch1.hasFocus())
	assert(not ch2.hasFocus())
	ch1.minimize()
#	assert(ch1.parent.focus == Window.FOCUS_FOREGROUND)
	ch2.minimize()
	assert(ch2.state == Window.STATE_MINIMIZED)

def txtbox_tst():
	app_win = AppWindow("AppWin", Point(100, 100), 400, 400)
	ctn = Container(app_win, "Test Container",Point(75, 75), 100, 100)
	txtbox = TextBox(ctn, "Test texbox", Point(50, 50), 50, 50)
	txtbox.setText("12450")
	assert(isaNumber(txtbox.text))
	assert(not isaFloat(txtbox.text))
	txtbox.setText("http://www.bitbucket.org")
	assert(isaURL(txtbox.text))
	txtbox.setText("https://www.facebook.com")
	assert(isaURL(txtbox.text))


if __name__ == '__main__':
	appwin_test()		
	dialog_testing()		
	testing_containers()		
	txtbox_tst()		
