# import Demo
# nt(a,A)  2no bhi print hoga o/p 10 20
from calendar import error

# int
# float    these are 5 fundamental data types which is immutable, no change in behaviour
# string
# complex
# boolean


# list
# tuple
# set
# frozenset
# bytes
# bytesarray
# dict
# none
# range


# print(s2)  ----> error:  int() argument must be a string, a bytes-like object or a real number, not 'complex'
# s3=float(s)
# print(s3) ----> error: float() argument must be a string or a real number, not 'co
# print(s1) ---> error: invalid literal for int() with base 10: 'abc'
# s2=float(s)
# print(s2) ---> error: could not convert string to float: 'abc'
# s5=complex(s)
# print(s5)  ---> error :complex() arg is a malformed string
# a=int(10+5j)
# print(a)  o/p error int() argument must be a string, a bytes-like object or a real number, not 'complex'
# a=int("10.3")
# print(a)   --> invalid literal for int() with base 10: '10.3'
# a=int("10.3")
# print(a)   --> invalid literal for int() with base 10: '10.3'

# a=int("ten")
# print(a)  ---> invalid literal for int() with base 10: 'ten'
# a=int("0B111123")
# print(a) -->invalid literal for int() with base 10: '0B1112'
# a=float(10+5j)
# print(a)  --> float() argument must be a string or a real number, not 'complex'

# a=float("ten")
# print(a) --> could not convert string to float: 'ten'

# a=float("0B111123")
# print(a) --> ould not convert string to float: '0B111123'

# print(type(t1))
# t2=('True')  / t2=(1) / t2=('mac') -- it will define type int bool str
# t=([1,2,3,4,5])
# print(t)   o/p list
# t3=(,)
# print(t3)   --- error

#  indexing and slicing----- forword indexing from left to right
# s='nikhil'
# print(s[0:6])  o/p nikhil end+1
# s='nikhil'
# print(s[0::2]) 0/p nki
# s='nikhil'
# print(s[1:5]) o/p ikhi
# s='nikhil'
# print(s[1::2]) o/p ihl
# s='nikhil'
# print(s[::])  o/p nikhil

# s= 'nikhil is a python developer'
# print(s[0::2])  o/p nki sapto eeoe
# s= 'nikhil is a python developer'
# print(s[0::3])  o/p nh  ph vor
# s= 'nikhil is a python developer'
# print(s[0::4]) o/p nispoeo
# s= 'nikhil is a python developer'
# print(s[0::5]) o/p nlahep
# s= 'nikhil is a python developer'
# print(s[0::6])
# s= 'nikhil is a python developer'
# print(s[0::7])



# s=[1,2,3,4,5,6,7]
# print(s[0::2])  o/p  [1, 3, 5, 7]
# print(s[:2:]) [1,2]
# print(s[1]) o/p [1]
# print(s[:3:]) [1,2,3]
# print(s[0::]) o/p [1, 2, 3, 4, 5, 6, 7]
# print(s[:0:])  o/p []
# rint(s[::])  0/p [1, 2, 3, 4, 5, 6, 7]
# print(s[0:3:2]) o/p [1,3]
# print(s[0:3:3]) o/p [1]
# print(s[1:6:-1]) o/p []
# pprint(s[-1::]) o/p error
# print(s[:-1:])  o/p [1, 2, 3, 4, 5, 6]
# print(s[:-2:]) o/p [1, 2, 3, 4, 5]
# print(s[1:-1:]) o/p  [1, 2, 3, 4, 5, 6]
# print(s[1:-2:]) o/p [2, 3, 4, 5]
# print([0:4:-1]) o/p error
# print(s[::-1]) to reverse the string  [7, 6, 5, 4, 3, 2, 1]



# s= 'nikhil is a python developer'
# print(s[0:7:2])  o/p nki
# s='nikhil is a python developer'   both o/p is nki
# print(s[0:5:2])
# s='2k4 f55 kk9 0wer'
# print(s[0:4]) space count kiya 2k4 f  o/p 2k4
# s='2k4 f55 kk9 0wer'
# print(s[0:4])
# s='2k4 f55 kk9 0wer'
# print(s[0:7])
# s='2k4 f55 kk9 0wer'
# print(s[0:8])

#  reverse indexing---- right to left
# s=[1,2,3,4,5,6,7,89,]
# print(s[-1::-2])   o/p[89, 6, 4, 2]
# s=[1,2,3,4,5,6,7,89,]
# print(s[-1:-5:-2]) o/p [89, 6]
# s=[1,2,3,4,'abcr','@#$%']
# print(s[0:6]) o/p[1, 2, 3, 4, 'abcr', '@#$%']
# s=[1,2,3,4,'abcr','@#$%',23,45]
# print(s[0::3])  o/p [1, 4, 23]

# s=[1,2,3,4,5,4,5,67,76,56]
# print(s[::-1]) o/p [56, 76, 67, 5, 4, 5, 4, 3, 2, 1] to rever the whole string
# s=[1,2,3,4,5,4,5,67,76,56]
# print(s[::1])  it will not change as it is
# s=[1,2,3,4,5,4,5,67,76,56]
# print(s[-1::]) o/p [56]
# s=[1,2,3,4,5,4,5,67,76,56]
# print(s[1::]) o/p [2, 3, 4, 5, 4, 5, 67, 76, 56] isme jo 1 hai wo skip hoga baki sab print honge

# s=[-1,-12,-34,-45,-2,-5,-10,-1]
# print(s[::-1]) o/p [-1, -10, -5, -2, -45, -34, -12, -1]
# s=[-1,-12,-34,-45,-2,-5,-10,-1]
# print(s[:5:]) o/p [-1, -12, -34, -45, -2]
# s=[-1,-12,-34,-45,-2,-5,-10,-1]
# print(s[::2]) o/p [-1, -34, -2, -10]
# s=[-1,-12,-34,-45,-2,-5,-10,-1]
# print(s[::-2]) o/p[-1, -5, -45, -12]
# s=[-1,-12,-34,-45,-2,-5,-10,-1]
# print(s[::3])
# s=(1,2,3,4,5,4,5,5,66,78,)
# print(s[0])
# s=(1,2,3,4,5,4,5,5,66,78)
# print(s[0])
# s=(1,2,3,4,5,4,5,5,66,78,)
# print(s[0:4:2])

# s=(1,234,456,123,456,'wert')
# print(s[5::])]


# s=[i * 2 for i in range (0,5) ]
# print(s)
#
# s=[i * i for i in range (5) ]
# print(s)


# import Demo
# print(Demo.x)   o/p 10

# from Demo import x,y
# print(x)
# print(x,y)  o/p 10 20

# from Demo import *
# print(x,y)  o/p 10 20

# import Demo
# print(Demo.wish("nikhil"))
# print(Demo.s)
# c= Demo.wish("mac")
# print(c)

# from Demo import wish,s
# print(wish("nik"))
# print(s)

# from Demo import *
# print(wish("nik"))
# print(s)



# ---- Abstraction ----

# from abc import abstractmethod
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     @abstractmethod
#     def m2(self):
#         pass
# class B(A):
#     def m1(self):
#         print("nagpur")
# class C(B):
#     def m2(self):
#         print("mumbai")
# obj=C()
# obj.m1()
# obj.m2()
 #   o/p
#  nagpur
# mumbai