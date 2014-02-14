#!/usr/bin/python
class Rectangle:
		def __init__(self,lbp,width,height):
				self.lbp=lbp
				self.width=width
				self.height=height
				self.x,self.y=self.lbp
				self.t_w=self.x+self.width
				self.t_h=self.y+self.height
			
def check_intersection(first,second):
		if first.x<=second.x:
				if first.t_w>=second.x and first.t_h>=second.y and second.t_h>=first.y:
						return True
				else:
						return False
		elif first.x>second.x:
				if second.t_w>=first.x and second.t_h>=first.y and first.t_h>=second.y:
						return True
				else:
						return False
		else:
				return False	
