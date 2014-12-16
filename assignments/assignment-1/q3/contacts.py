#!/usr/bin/python

from phonenum import *

def create_contacts():
	return {}

def add_contacts(contacts, name, phone_num, phone_type):
	if contacts.has_key(name):
		phone_nums = contacts[name]
		phone_nums.append(Phonenum(phone_num, phone_type))
	else:
		contacts[name] = [ Phonenum(phone_num, phone_type) ]

def update_contact_number(contacts,contact_name,old_number,new_number):
	if contacts.has_key(contact_name): 
		temp=contacts.get(contact_name)
		for i in temp:
			if(i[0]==old_number):
				j=list(i)
				j.remove(i[0])
				j.insert(0,new_number)
				j=tuple(j)
				temp.remove(i)
				temp.append(j)
		return True
	else:
		return False

