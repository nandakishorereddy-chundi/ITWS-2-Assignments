#!/usr/bin/python
class IntermediatePoints:
	def __init__(self,p1,p2):
		self.x1,self.y1=p1
		self.x2,self.y2=p2
		if(self.x1>self.x2):
			temp1=self.x1
			temp2=self.y1
			self.x1=self.x2
			self.y1=self.y2
			self.x2=temp1
			self.y2=temp2
		if(self.y2-self.y1==0):
			self.fg=1
		elif(self.x2-self.x1==0 and self.y2<self.y1):
			temp1=self.x1
			temp2=self.y1
			self.x1=self.x2
			self.y1=self.y2
			self.x2=temp1
			self.y2=temp2
			self.fg=2
		elif(self.x2-self.x1==0):
			self.fg=2
		else:
			self.fg=0
			self.slope=(self.y2-self.y1)/float((self.x2-self.x1))
		self.i=1
		if self.fg==0:
			while(self.i<(self.x2-self.x1)):
				print ((self.slope*self.i)+self.x1,(self.slope*self.i)+self.y1)
				self.i+=1
		elif self.fg==1:
			while(self.i<(self.x2-self.x1)):
				print (self.x1+self.i,self.y1)
				self.i+=1
		elif self.fg==2:
			while(self.i<(self.y2-self.y1)):
				print (self.x1,self.y1+self.i)
				self.i+=1
