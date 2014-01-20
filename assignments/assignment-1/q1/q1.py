#!/usr/bin/python

__all__ = ["Acquaintances","Messages","Users","register","add_friend","add_friends","remove_user","get_friends","get_friends_of_friends","send_message","send_group_message","get_messages_from_friend","get_messages_from_all_friends","get_birth_day_messages","delete_message","delete_messages","delete_all_messages","delete_messaged_from_friend"]

import time

Users={}
Acquaintances={}
Messages={}
cnt=0
cnt1=0
""" Assuming that we have to create an ID in Users dictionary """
""" Function to create information about user """
def register(user_id,info):
	if user_id in Users:
	    print "Oops! this user is already registered" 
	else:
	    Users[user_id]=info
	    Acquaintances[user_id]=[]
	    Messages[user_id]=[]

def add_friend(user_id,friend_id):
	if user_id in Acquaintances:
	    if friend_id not in Acquaintances[user_id]:
	        temp=Acquaintances.get(user_id)
		temp.append(friend_id)
		return True
	    else:
		return "He is already added"
	else:
		return False

def add_friends(user_id,friends):
	if user_id in Acquaintances:
	    """ Returns a list who are new to add as friend """
	    temp_list = [x for x in friends if x not in Acquaintances[user_id]]
	    temp=Acquaintances.get(user_id)
	    temp.extend(temp_list)
	    return True
	else:
	    return False

def remove_user(user_id):
	if user_id in Users:
	    del Users[user_id]
	    del Acquaintances[user_id]
	    del Messages[user_id]
	    return True
	else:
	    return False

def get_friends(user_id):
	if user_id in Acquaintances:
	    return tuple(Acquaintances[user_id])
	else:
	    return None

""" Assuming this function should Return friends ID who are not friends of User but friends of friends of User """
def get_friends_of_friends(user_id):
	if user_id in Acquaintances:
	    try:
	        temp=[]
		for friend in Acquaintances[user_id]:
		    """ checks whether index is present or not """
		    if friend in Acquaintances:
		        for p in Acquaintances[friend]:
		            temp.append(p)
			#print temp
		for friend in Acquaintances[user_id]:
		    for p in temp:
		        #print p,friend
			if(p==friend):
			    temp.remove(p)
		for i in range(0,len(temp)):
		    for j in range(i+1,len(temp)):
		        if(temp[i]==temp[j]):
			    temp.remove(temp[j])
	    except(KeyError):
		pass
	    finally:
		return tuple(temp)
	else:
	    return None

def send_message(sender_id,receiver_id,text):
	msg=[]
	msg.append(sender_id)
	msg.append(get_message_id(receiver_id))
	msg.append(text)
	msg.append(get_date())
	msg.append(get_time())
	msg=tuple(msg)
	if sender_id and receiver_id in Messages:
	    temp=Messages.get(receiver_id)
	    temp.append(msg)
	    #print Messages
	    return True
	else:
	    return False

""" Structuring of the message functions starts from this point """

def get_time():
	return time.strftime("%H:%M:%S")

def get_date():
	return time.strftime("%d/%m/%y")

def get_message_id(receiver_id):
	try:
	    return len(Messages[receiver_id])
	except(KeyError):
		pass

""" Structuring of the message functions ends at this point """		

def send_group_message(sender_id,receiver_ids,text):
	if sender_id in Messages:
	    for user in receiver_ids:
	        if user in Messages:
		    global cnt
		    cnt+=1
	    for user in receiver_ids:
		global cnt1
		cnt1+=1
	    if(cnt==cnt1):
	        cnt=0
		cnt1=0
		for user in receiver_ids:
		    	msg=[]
		    	msg.append(sender_id)
		    	msg.append(get_message_id(user))
		    	msg.append(text)
		    	msg.append(get_date())
		    	msg.append(get_time())
		    	msg=tuple(msg)
		        temp=Messages.get(user)
		        temp.append(msg)
		return True
	    else:
		cnt=0
		cnt1=0
		return False
	else:
	    return False

def get_messages_from_friend(receiver_id,friend_id):
	if receiver_id and friend_id in Messages:
	    l=[]
	    for i in Messages[receiver_id]:
	        if(i[0]==friend_id):
		    l.append(i)
            return tuple(l)
	else:
	    return None
											
def get_messages_from_all_friends(receiver_id):
	if receiver_id in Messages:
	    try:
	        return tuple(Messages[receiver_id])
	    except(KeyError):
		pass
        else:
	    return None

def get_birth_day_messages(receiver_id):
	if receiver_id in Messages:
	    msg=[]
	    for i in Messages[receiver_id]:
		""" Considering only date and month that is first five of the present date """
		if((i[3] and range(0,5)) == (Users[receiver_id][2] and range(0,5))):
		    msg.append(i)
		return tuple(msg)
	else:
	    return None
""" Assuming msg_id is nothing but the index of the msg tuple """
def delete_message(user_id,msg_id):
	if user_id in Messages and len(Messages[user_id])>msg_id:
	    del Messages[user_id][msg_id-1]
	    return True
	else:
	    return False

def delete_messages(user_id,msg_ids):
	if user_id in Messages:
	    length=len(Messages[user_id])
	    for i in msg_ids:
	        if(i<length):
		    global cnt
		    cnt+=1
	    temp=cnt
	    cnt=0
	    return temp
	else:
	    return None

def delete_all_messages(user_id):
	if user_id in Messages:
	    del Messages[user_id]
	    return True
	else:
	    return None

def delete_messaged_from_friend(receiver_id,friend_id):
	if receiver_id and friend_id in Messages:
	    for i in Messages[receiver_id]:
		if(i[0]==friend_id):
		    Messages[receiver_id].remove(i)
	    return True
	else:
	    return None

def main():
	""" Samplpe test cases """
	register(1,("nan","hyd","19-07-1995"))
	register(2,("manu","hyd","25-12-1997"))
	register(3,("din","nellore","07-05-1995"))
	register(4,("no details"))
	add_friend(1,2)
	add_friends(3,(1,2))
	remove_user(4)
	get_friends(2)
	get_friends(4)
	get_friends_of_friends(3)
	send_message(1,2,"hi")
	send_group_message(2,(1,3),"everything is fine")
	get_messages_from_friend(3,1)
	get_messages_from_all_friends(1)
	get_birth_day_messages(2)
	delete_message(1,3)
	delete_message(1,1)
	delete_messages(3,(0,2))
	delete_all_messages(3)
	delete_messaged_from_friend(2,1)

if __name__ == "__main__" :
		main()
