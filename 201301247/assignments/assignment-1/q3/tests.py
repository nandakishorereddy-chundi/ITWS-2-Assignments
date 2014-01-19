#!/usr/bin/python

from contacts import create_contacts
from contacts import add_contacts
from contacts import update_contact_number
from phonenum import *

contacts = {}

def test_add_multiple_contact_numbers():
	    c = create_contacts()
	    add_contacts(c, 'ken', "1234567890", "home")
	    add_contacts(c, 'ken', "2345678901", "work")
	    add_contacts(c, 'ken', "2345678902", "work")
	    assert(len(c.keys()) == 1)

def test_generic_contacts_behavior():
		    contacts["Guido"] = Phonenum("0987654321", "home")
		    contacts["Ritchie"] = Phonenum("5678904321", "home")
		    contacts["Rob"] = Phonenum("1234567890", "work")
		    contacts["Steve"] = Phonenum("1234567", "work")
		    assert(len(contacts.keys()) == 4)

		    phone_steve = contacts["Steve"] 
		    assert(phone_steve is None)

		    try:
			phone_ken = contacts["ken"]
			assert(0)
		    except KeyError as e:
			     assert(1)

def test_num():
	assert (check("8790659549") == True)
	assert (check("8790abc") == False)

def test_optional_country_code():
	assert (Phonenum("8790659549","home") == ('8790659549', 'home'))
	""" Allows optional country code """
	assert (Phonenum("8790659549","home","+91") == ('+918790659549', 'home'))

def test_update_contact_number():
	assert (update_contact_number(contacts,"Guido","0987654321","8790659549") == True)
	assert (update_contact_number(contacts,"dinesh","0987654321","8790659549") == False)

if __name__  ==  "__main__":
	test_generic_contacts_behavior()
	test_add_multiple_contact_numbers()
	test_num()
	test_optional_country_code()
	test_update_contact_number()
