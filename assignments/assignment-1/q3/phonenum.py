#!/usr/bin/python

"""Phonenum - an abstraction to represent mobile phone numbers."""

"This type is meant to be used only in the classroom!"

__all__ = ["Phonenum", "phonenum_work", "phonenum_home", "phonenum_same","check"]

_phonenum_types_ = ["work", "home"]

cnt=0

def Phonenum(numstr, type,code=None):
	"""constructs an instance of a phone-number."""
	if code is None:
		num = numstr.strip()
		if len(num) is not 10 or check(num) is False:
			return None
		return (num, type.strip().lower())
		""" Assuming country code will start with '+' and can contain any number of digits and symbols """
	elif(code[0]=='+' and len(numstr)==10):
		num=numstr.strip()
		num=str(code)+num
		return (num, type.strip().lower())
	else:
		return False

def phonenum_work(tn):
	num, type = tn
	return type == "work"

def phonenum_home(tn):
	num, type = tn
	return type == "home"

def phonenum_same(this, that):
	return _phonenum_valid_(this) and _phonenum_valid_(that) and this[0] == that[0]

def _phonenum_valid_(tn):
	return isinstance(tn, tuple) and len(tn) == 2 and \
		isinstance(tn[0], str) and len(tn[0]) == 10

def check(num):
	for i in num:
		if(i>='0' and i<='9'):
			global cnt
			cnt+=1
	if(len(num)==cnt):
		cnt=0
		return True
	else:
	 	cnt=0
	 	return False
