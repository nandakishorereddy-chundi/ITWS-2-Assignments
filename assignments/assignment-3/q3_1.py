#!/usr/bin/python
class DoublyLinkedList:
		class Node:
			def __init__(self,key,val):
					self.key=key
					self.val=val
					self.next=None
					self.prev=None
			
			def __eq__(self,key):
					if(self.key==key):
						return True
					else:
						return False

			def val(self):
					return self.val
		
		def __init__(self):
				self.head=None
				self.tail=None

		class ForwardListIterator:
				def __init__(self,iterator):
						self.iter=iterator

				def next(self):
						if self.iter is not None:
							temp=self.iter.val
							self.iter=self.iter.next
							return temp
						else:
							raise StopIteration

				def __iter__(self):
						return self
		
		class ReverseListIterator:
				def __init__(self,iterator):
						self.iter=iterator

				def next(self):
						if self.iter is not None:
							temp=self.iter.val
							self.iter=self.iter.prev
							return temp
						else:
							raise StopIteration
				
				def __iter__(self):
						return self
		
		def length(self):
				cnt=0
				dum=self.head
				while(dum!=None):
						cnt=cnt+1
						dum=dum.next
				return cnt
		
		"""precondition: neither 'key' nor 'val' may be None.
		   postcondition: self.head will point to the new node."""
		def insert(self,key,val):
				if self.head is None and self.tail is None:
						self.head=self.Node(key,val)
						self.tail=self.head
						self.head.next=None
						self.head.prev=None
				else:
						temp=self.head
						self.head.prev=self.Node(key,val)
						self.head=self.head.prev
						self.head.next=temp
						self.head.prev=None

		"""postcondition: self.head should point first element of the list"""
		def find(self,key):
				dum=self.head
				while(dum!=None):
						if(dum.key==key):
								return dum.val
						else:
								dum=dum.next
				if dum==None:
						return None
			
		"""postcondition: self.tail should again point to the last element of the list after deletion
		                  if there is a single node both self.head and self.tail should be none"""
		def deleteLast(self):
				if self.tail is None:
						return None
				elif self.tail.next is None and self.tail.prev is None:
						self.tail=None
						self.head=None
				elif self.tail.prev is not None:
						self.tail=self.tail.prev
						self.tail.next=None
			
		"""postcondition: self.head should again point to the first element of the list after deletion
		                  if there is a single node both self.head and self.tail should be none"""
		def deleteFirst(self):
				if self.head is None:
						return None
				elif self.head.next is None and self.head.prev is None:
						self.head=None
						self.tail=None
				elif self.head.next is not None:
						self.head=self.head.next
						self.head.prev=None

		"""postcondition: after deletion self.head should again point to the first element of the list"""
		def delete(self,key):
				dum=self.head
				while(dum!=None):
						if(dum.key==key and dum.prev is not None and dum.next is not None):
								dum=dum.prev
								dum.next=dum.next.next
								dum.next.prev=dum
								return
						elif(dum.key==key and dum.prev is None and dum.next is not None):
								dum=dum.next
								self.head=dum
								dum.prev=None
								return
						elif(dum.key==key and dum.prev is not None and dum.next is None):
								dum=dum.prev
								self.tail=dum
								dum.next=None
								return
						elif (dum.key==key and dum.next is None and dum.prev is None):
								self.head=None
								self.tail=None
								dum=None
								return
						else:
								dum=dum.next

				if dum==None:
						return None

		def print_front(self):
				dum=self.head
				while(dum!=None):
						print dum.key,dum.val
						dum=dum.next

		def print_back(self):
				dum=self.tail
				while(dum!=None):
						print dum.key,dum.val
						dum=dum.prev

class iter_interface(DoublyLinkedList):
	
	def __init__(self,head):
		self.head=head
	
	def next(self):
		if self.head is not none:
			temp=self.head.val
			self.head=self.head.next
			return temp
		else:
			StopIteration

class New_ReverseIterator(DoublyLinkedList):
	
	def __init__(self,tail,head):
		self.tail=tail
		self.head=head
	
	def getReverseIterator(self):
		if self.tail is not None:
			temp=self.tail.val
			self.tail=self.tail.prev
			return temp
		else:
			raise StopIteration

	def getForwardIterator(self):
		if self.head is not None:
			temp=self.head.val
			self.head=self.head.next
			return temp
		else:
			raise StopIteration
