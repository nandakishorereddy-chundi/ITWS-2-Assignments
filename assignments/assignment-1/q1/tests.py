#!/usr/bin/python

from Q1 import *

def test_add_friend():
	add_friend(1,3)
	add_friend(2,4)
	assert (len(Acquaintances[1])==1 and len(Acquaintances[2])==1)

def test_register():
	register(1,("nanda","hyderabad","19-07-1995"))
	register(2,("manu","hyderabad","25-12-1997"))
	register(3,("dinesh","nellore","05-05-1995"))
	register(4,("harsha","nellore","13-09-1993"))
	register(5,("unknown","unknown","unknown"))
	assert (Users[1]==("nanda","hyderabad","19-07-1995"))

def test_add_friends():
	add_friends(1,(2,4))
	add_friends(2,(1,3))
	add_friends(3,(2,4))
	add_friends(4,(1,3))
	assert (len(Acquaintances[1])==3 and len(Acquaintances[2])==3)

def test_remove_user():
	assert (remove_user(5)==True)

def test_get_friends():
	assert (get_friends(2) == (4,1,3))
	assert (get_friends(5) == None)

def test_get_friends_of_friends():
	assert (get_friends_of_friends(2) == (3,2))
	assert (get_friends_of_friends(5) == None)

def test_send_message():
	assert (send_message(1,3,"hi") == True)
	assert (send_message(1,5,"hi") == False)

def test_send_group_message():
	assert (send_group_message(1,(2,3,4),"bye") == True)
	""" user_id=5 is not present in users and acquaintances dictionary so assertion should be False"""
	assert (send_group_message(1,(2,3,5),"bye") == False)

def test_get_messages_from_friend():
	""" When ever we run this program time and date  will be updated so it won't be 17/01/14 """
	assert (get_messages_from_friend(3,1) != ((1, 0, 'hi', '17/01/14', '19:15:03'), (1, 1, 'bye', '17/01/14', '19:15:03')))
	assert (get_messages_from_friend(1,3) == ())
	assert (get_messages_from_friend(1,5) == None)

def test_get_messages_from_all_friends():
	""" When ever we run this program time and date  will be updated so it won't be 17/01/14 """
	assert (get_messages_from_all_friends(3) != ((1, 0, 'hi', '17/01/14', '19:15:03'), (1, 1, 'bye', '17/01/14', '19:15:03')))
	assert (get_messages_from_all_friends(5) == None)

def test_get_birth_day_messages():
	""" When ever we run this program time and date  will be updated so it won't be 17/01/14 """
	assert (get_birth_day_messages(3) != (1, 0, 'hi', '17/01/14', '19:35:03'))
	assert (get_birth_day_messages(5) == None)

def test_delete_message():
	assert (delete_message(3,0) == True)
	assert (delete_message(5,0) == False)

def test_delete_messages():
	assert (delete_messages(3,(0,1,4,7)) == 1)
	assert (delete_messages(5,(0,3)) == None)

def test_delete_all_messages():
	assert (delete_all_messages(3) == True)
	assert (delete_all_messages(5) == None)

def test_delete_messaged_from_friend():
	assert (delete_messaged_from_friend(4,2) == True)
	assert (delete_messaged_from_friend(2,5) == None)

if __name__ == "__main__" :
	test_register()
	test_add_friend()
	test_add_friends()
	test_remove_user()
	test_get_friends()
	test_get_friends_of_friends()
	test_send_message()
	test_send_group_message()
	test_get_messages_from_friend()
	test_get_messages_from_all_friends()
	test_get_birth_day_messages()
	test_delete_message()
	test_delete_messages()
	test_delete_all_messages()
	test_delete_messaged_from_friend()
