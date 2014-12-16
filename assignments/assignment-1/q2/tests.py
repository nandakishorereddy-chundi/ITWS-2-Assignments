#!/usr/bin/python

from Q2 import *
	
p1=(0,0,0)
p2=(1,2,3)
p3=(1,1,1)
p4=(3,4,5)
vector1=(p1,p2)
vector2=(p3,p4)

def test_length():
	assert (length(vector1) == '3.742')

def test_normalize():
	assert (normalize(vector1) == ((0, 0, 0), ('0.267', '0.535', '0.802')))

def test_dot_product():
	assert (dot_product(vector1,vector2) == 20)

def test_cross_product():
	assert (cross_product(vector1,vector2) == ((0, 0, 0), (-1, 2, -1)))

if __name__ == "__main__" :
	test_length()
	test_normalize()
	test_dot_product()
	test_cross_product()
