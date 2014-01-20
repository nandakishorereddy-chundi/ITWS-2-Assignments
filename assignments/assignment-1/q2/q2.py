#!/usr/bin/python

import math

__all__ =["length","normalize","dot_product","cross_product"]

sqrt=math.sqrt
def length(vector):
	ans=sqrt(pow((vector[0][0]-vector[1][0]),2)+pow((vector[0][1]-vector[1][1]),2)+pow((vector[0][2]-vector[1][2]),2))
	""" Returns only first 3 places after decimal point """
	return  "%.3f" % ans 

def normalize(vector):
	p1,p2=vector
	a=p2[0]-p1[0]
	b=p2[1]-p1[1]
	c=p2[2]-p1[2]
	vector1=(0,0,0)
	co1=(a/float(sqrt((a*a)+(b*b)+(c*c))))
	co2=(b/float(sqrt((a*a)+(b*b)+(c*c))))
	co3=(c/float(sqrt((a*a)+(b*b)+(c*c))))
	co1="%.3f" % co1
	co2="%.3f" % co2
	co3="%.3f" % co3
	vector2=(co1,co2,co3)
	return (vector1,vector2)

def dot_product(vector1,vector2):
	p1,p2=vector1
	p3,p4=vector2
	return (((p2[0]-p1[0])*(p4[0]-p3[0]))+((p2[1]-p1[1])*(p4[1]-p3[1]))+((p2[2]-p1[2])*(p4[2]-p3[2])))

def cross_product(vector1,vector2):
	p1,p2=vector1
	p3,p4=vector2
	a=p2[0]-p1[0]
	b=p2[1]-p1[1]
	c=p2[2]-p1[2]
	d=p4[0]-p3[0]
	e=p4[1]-p3[1]
	f=p4[2]-p3[2]
	vector1=(0,0,0)
	vector2=((b*f-e*c),(c*d-a*f),(a*e-b*d))
	return (vector1,vector2)

def main():
    pass
if __name__ == "__main__" :
	main()
