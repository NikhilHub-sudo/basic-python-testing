# import keyword
# import re

# print("Nikhil")
print("this is new code")
print("my new file ")
# import keyword
# d=keyword.kwlist
# print(d)
# print(type(d))

# d= 100+200j
# print(d.real)
# print(d.imag)
# print(type(d))

"""
a=233
b2=23
c='nikhil'
d="sam"
print(d)
print(type(d))
"""



# s=False
# print(s)
# s1=int(s)
# print(s1)
# s2=float(s)
# print(s2)
# s3=str(s)
# print(s3)
# s4=bool(s)
# print(s4)
# s5=complex(s)
# print(s5)

# s1=False
# print(s1)
# s3=int(s1)
# print(s3)
# s4=float(s1)
# print(s4)
# s5=str(s1)
# print(s5)
# s6=complex(s1)
# print(s1)



# s=4+5j
# print(s)
# s2=int(s)
# print(s2)  ----> error:  int() argument must be a string, a bytes-like object or a real number, not 'complex'
# s3=float(s)
# print(s3) ----> error: float() argument must be a string or a real number, not 'complex'
# s4=str(s)
# print(s4)
# s5=bool(s)
# print(s5)



# s=10.00
# print(s)
# s1=int(s)
# print(s1)
# s2=str(s)
# print(type(s2))
# print(s2)
# s3=bool(s)
# print(s3)
# s4=complex(s)
# print(s4)

# s='abc'
# print(s)
# s1=int(s)
# print(s1) ---> error: invalid literal for int() with base 10: 'abc'
# s2=float(s)
# print(s2) ---> error: could not convert string to float: 'abc'
# s3=str(s)
# print(s3)
# s4=bool(s)
# print(s4)
# s5=complex(s)
# print(s5)  ---> error :complex() arg is a malformed string

# List--------
# list=[1,2,3,4,5,"nikhil",'True', '123']
# list1=set(list)
# print(list1)
# l3=[]
# print(l3)
# l4=[1]
# print(l4)

# tuple------
# t=(1,2,3, 'mac')
# print(type(t))
# t1=list(t)
# print(type(t1))
# t2=('True')  / t2=(1) / t2=('mac') -- it will define type int bool str
# print(t2)
# print(type(t2))
# t3=(,)
# print(t3)   --- error

# t4=(1,)
# print(t4)
# t5=('tuple')
# print(t5)
# t6=([1,2,3,4])
# print(t6)  --- will return list cz comma seperated values are not define
# t7=([1,2,3,4],[1,2]) -- it will return tuple
# print(type(t7))
# print(t7)

# a=int(123.234)
# print(a)    o/p 123

# a=int(True)
# print(a)  o/p 1

# a=int(10+5j)
# print(a)  o/p error int() argument must be a string, a bytes-like object or a real number, not 'complex'

# a=int("10")
# print(a)  o/p 10
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






# ----set----
# set={1,2,3,4,5,5,5,5}
# print(set)
#range--------

# for i in range(10):
#  print(i)  ---use print after an space otherwise it wil through an error

# for i in range(1,10):
#     print(i)
# for i in range(2,22):
#     print(i)

# for i2 in range(1,11):
#     print(i2)
# for i3 in range(2,21,2):   -----21-1
#     print(i3)
# for i4 in range(3,32,3):
#     print(i4)
# for i5 in range(1,22,2):
#     print(i5)
# for i6 in range(0,22,2):
#     print(i6)

# s=[1,2,3,4,6]
# s1=bytes(s)
# print(s1)
# print(type(s1))

# s=[1,2,3,4,5]
# s1=bytearray(s)
# print(s1)
# print(type(s1))
'''
# a=20
# b=10
# # c=a-b
# # print(c)
# # c=a*b
# # print(c)
# c=a//b
# print(c)
'''
# a=10
# b=10
# c=a/b
# print(c) o/p- 1.0
# a=10
# b=10
# c=a//b
# print(c)  o/p-1
# a=10
# b=20
# c=a/b
# print(c) o/p-0.5
# a=10
# b=20
# c=a//b
# print(c) o/p -0

# print(2**2) 0/p -4 2 to the power 2
# print(2**3)  o/p 2 to the power 3 o/p 8
# print(2**4) o/p 16

# a=4
# b=3   ----- for multiplication
# print(a*b)
# a=4
# b='nikhil'
# print(a*b)  o/p -nikhilnikhilnikhilnikhil   (repeatation)

#s=[1,2,3,4,5,6,6]
# print(s[0]) o/p -1
# print(s[5]) o/p 5
# s='roman'
# print(s[4])  o/p- n

# s={1,2,3,4,5,6}
# print(s[2])    o/p set object is not subscriptable   which means not allow


# relational operator------

# s='nik'
# s1='NIK'
# print(s>s1)
# s='NIK'
# s1='nik'
# print(s>s1)
# s='NIK'
# s1='NIK'
# print(s>s1)
# s='nik'
# s1='nik'
# print(s>s1)

# s='NIK'
# s1='nik'
# print(s<s1)
# s='nik'
# s1='NIK'
# print(s<s1)
# s='NIK'
# s1='NIK'
# print(s<s1)
# s='nik'
# s1='nik'
# print(s<s1)


# s='Nikh'
# s1='nik'
# print(s>s1)
# s='Nik'
# s1='nikh'
# print(s>s1)
# s='Nikh'
# s1='nik'
# print(s>=s1)
# s='Nik'
# s1='nikh'
# print(s>=s1)
# s='Nikh'
# s1='nik'
# print(s<=s1)
# s='Nik'
# s1='nikh'
# print(s<=s1)

# Equality operator-----
# = & ==
# Logical operator----
'''
a=10
b=20
c=30
d=40
print(a>b & c>d)
a=10
b=20
c=30
d=40
print(a>b & c<d)

a=10
b=20
c=30
d=40
print(a<b & b<c)
a=10
b=20
c=30
d=40
print(a==b & b==c &c>d)
a=10
b=20
c=30
d=40
print(a>=b & b>=c)
a=10
b=20
c=30
d=40
print(a<=b & b<=c &c>d)

# a=10
# b=10
# c=30
# d=40
# print(a>b & c<d)
# a=10
# b=20
# c=30
# d=40
print(a==b & b>c)
'''
# a=10
# b=10
# c=30
# d=40
# print(a==b & b<c)
# s='''i love india '''
# print(s)

# a=10
# b=50
# c=40
# d=60
# max = a if a>b and a>b and a>d else b if b>c and b>d else c if c>d else d
# print(max)

# max = a if a>=b and a>=b and a>=d else b if b>=c and b>=d else c if c>=d else d
# print(max)

# max = a if a<b and a<b and a<d else b if b<c and b<d else c if c<d else d
# print(max)  o/p 10

# a='nik'
# b="NIK"
# c='nikhil'
# d='machine'
# max= a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
# print (a)

# a='nik123'
# b="NIK234"
# c='nikhil432'
# d='machine2367'
# max= a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
# print (a)

# # a='nik'
# # b="NIK"
# # c='nikhil'
# # d='machine'
# # print(ord('a'))
# # print(ord('d'))
# # print(type(a))
# # max= a if a<b and a<c and a<d else b if b<c and b<d else c if c<d else d
# # print (a)

# a=10
# a+=5
# print(a)
# a=20
# a*=5
# print(a)
# a=10
# print(a+5)


#  is and is not identity operator it is only work on immutable data types if we write any mutable data type the result will be false
# s=10
# s1=10
# print(s==s1)  o/p true
# print(s is s1)
# print(s is not s1) o/p false
# s=10
# s1=20
# print(s is s1) o/p false

#  membership operator  in and not in
# s=123345
# print ('2'in s) o/p int is not iterable error

# s='12345'
# print('3' in s) o/p true

# input

# age=30
# s=input(age) o/p
# s=input('my age is',age) o/p input expected at most 1 argument got 2
# a=input('enter your first value:')
# b=input('enter your second value:')
# print(a+b) o/p will come concatination 3256 cz value we are taking in string
# a=int(input('enter your first value:'))
# b=int(input('enter your second value:'))
# print(a+b)
# a=float(input('enter your first value:'))
# b=float(input('enter your second value:'))
# print(a/b)

# a=string(input('enter your first value:'))
# b=string(input('enter your second value:'))
# print() ----- not getting ask sir
# a=int(input('enter your first value:'))
# b=int(input('enter your second value:'))
# c=a=int(input('enter your third value:'))
# d=a=int(input('enter your fourth value:'))
# max = a if a<b and a<b and a<d else b if b<c and b<d else c if c<d else d
# print(max)
# print(a+b*c-d) yaha wo check karega b ki value true hai to multi karke value print karega

#  eval()
# s=eval('10+39*3') take expression always in string we can use eval in list tuple and set
# print(s)
# s=eval(input('enter the list'))
# print(s)
# s=eval(input('enter the tuple'))
# print(s)

# FLOW CONTROL
#  Conditional statement if elif else
# a=20
# b=10
# if a>b:
#     print("nik")
# else:
#     print('mac')

# a = 20
# b = 10
# c=30
# d=25
# if a > b and b>c and c>d and c<=a:
#         print("nik")
# else:
#         print('mac')

# a=24
# b=30
# c=23
# d=14
# if a>b:
#     print('yellow')
# elif a==b:
#     print('black')
# elif a<=b:
#     print('blue')
# elif a>=b:
#     print('white')
# else:
#     print('none')

# a=24
# b=30
# c=23
# d=14
# if a<b:
#     print('apple')
# else:
#     print('false')
# if b<c:
#     print('mango')
# else:
#     print('false')
# if c<d:
#     print('banana')
# else:
#     print('false')

# akash='nike'
# saransh='add'
# nikhil='puma'
# mrunmayee='zara'
# dhawal='road'
# mrunal='brand is not define'

# brand=input('enter the brand:')
# if brand=='nike':
#     print('akash')
# elif brand=='add':
#     print('sarash')
# elif brand=='puma':
#     print('nikhil')
# elif brand=='zara':
#     print('mrunmayee')
# elif brand=='road':
#     print('dhawal')
# else:
#     print('brand is not define')



# brand = input("enter ur brand:")
# value1 = int(input("enter ur v1:"))
# value2 = int(input("enter ur v2:"))
# if value2 > value1:
#     if brand == "nike":
#         print("its a akash brand")
#     elif brand == "add":
#         print("its a saransh brand")
#     elif brand == "puma":
#         print("its a nikhil brand")
#     elif brand == "zara":
#         print("its a mrunmyee brand")
#     elif brand == "roadstar":
#         print("its a dhawal brand")
#     else:
#         print("its a mrunal brand")  ----nested if statment
# else:
#     print( 'the brand  you are searching its not in the list')


# a= int(input('enter your 1st value:'))
# b= int(input('enter your 2nd value:'))
# c= int(input('enter your 3rd value:'))
# lowest= a if a<=b and a<=c else b if b<=c else c
# print(lowest)

# a= int(input('enter your 1st value:'))
# b= int(input('enter your 2nd value:'))
# c= int(input('enter your 3rd value:'))
# if a<b:
#     print(a)
# else:
#     print('maximum')
# if b<c:
#     print(b)
# else:
#     print('maximum')
# if c:
#     print(c)
# else:
#     print('maximum')

# a=int(input('enter your 1st value:'))
# b=int(input('enter your 2nd value:'))
# c=int(input('enter your 3rd value:'))
# if a<=b and a<=c:
#     print(a)
# elif b<=a and b<=c:
#     print(b)
# else:
#     print(c)

# num=int(input('enter any value between 1 to 101:'))
# for a in range(1,101):
#  if a%2==0:
#     print('the a is even number')
#  elif a%2!=0:
#      print('the a is odd number')
# else:
#     print('the value is not in a range' )


# a=int(input('enter any number:'))
# if a%2==0:
#     print('entered no is a an even')
# else:
#     print('entered no is odd')

# name=input('enter the name of technology')
# while name!="python":
#     print('java developer')
#     print('12345')

# #  while loop -------
# a=1
# while a<=12:
#     print(a)
#     a=a+2
# subject=input('enter the subjects')
# while subject!='economics':
#     print('you are eligible')

# num=1
# while num<=5:     print num 1 to 5
#     print(num)
#     num +=1

# count=10
# while count >0:
#     print(count)
#     count -=1

# count = 1
# while count < 11 :
#     print(count)
#     count += 1

#  transfer statement-------
# s=[1,2,3,4,5,6,7,8]
# for i in s:
#     if i==4:    0/p 123
#         break
#     print(i)

# s=[1,2,3,4,5,6,6,6,6,7,5,7,8]
# for i in s:
#     if i==6:
#         continue
#     print(i)
# s=[1,2,3,4,5,'nik','mac12344$', '@#$%%^']
# for i in s:
#     if i=='nik':
#         continue
#     print(i)

# s=[300,465,567,7890,3245,5432,6785,7864,0000]
# for i in s:
#     if i > 5432:
#         break
#     print(i)

# s=[300,465,567,7890,3245,5432,6785,7864,0000]
# for i in s:
#     if i < 5432:
#         break
#     print(i)

#  ---- pass-----
# a=100
# b=20
# if a>b:
#     pass
# a=10
# b=20     condition false hai fir bhi pass hua
# if a>b:
#     pass

#  indexing and slicing----- forword indexing from left to right
# s='nikhil'
# print(s[0:6])
# s='nikhil'
# print(s[0::2]) 0/p nki
# s='nikhil'
# print(s[1:5]) o/p ikhi
# s='nikhil'
# print(s[1::2]) o/p ihl

# s= 'nikhil is a python developer'
# print(s[0::7]) o/p nitv

# s=[1,2,3,4,5,6,7]
# print(s[0::2])



# s= 'nikhil is a python developer'
# print(s[0:7:2])
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

#  ---------  string functionality--------- strip lstrip rstrip

# a=input('enter the city:')
#                             in output if i take """"""""""" mumbai """"""" it says invalid
# print(a)                   also when i take only mumbai in output it still says invalid
# a1=input('enter the city:')
# print(a1.strip())

# s= "        nikhil is a django developer      "
# print(s)   o/p         nikhil is a django developer  space nahi jayegi
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())



# a2=input('enter the city:')
# if "" in a2 :
#     print("invalid membership")
# else:
#     print(a2)
# s="************ nikhil @@@@@@@@@@@@@"
# print(s.strip('*')) o/p ************ nikhil

# s="************ nikhil  **********"
# print(s.strip('*')) o/p nikhil

# s="************ nikhil @@@@@@@@@@@@"
# print(s.lstrip())  o/p************ nikhil @@@@@@@@@@@@@

# s="************ nikhil **********"
# print(s.lstrip('*')) o/p  nikhil **********
# s="************ nikhil @@@@@@@@@@@@"
# print(s.rstrip('*'))  o/p ************ nikhil @@@@@@@@@@@@
# s="************ nikhil **********"
# print(s.rstrip('*')) o/p ************ nikhil

# print(s.lstrip())   o/p nikhil

# s= input('enter the city name:')
# if " " in s or "" in s:
#     print('invalid city')
# else:
#     print(s)
# when ever i put only city name without space and any empty string it should print the city name a well but it says invalid city why is that so

#    interview question ask ----
# import time
# x=5
# print(id(x))
# time.sleep(10)
# print(id(x))
# print('exist')




#  finding substring-------

# s=input('enter your main string')
# s1=input('enter your substring')
# print(s.find(s1))

# find() and index() ------
# s="123pythondev"
# print(s.find("py", 0,5))  o/p 3  0 se 5 tak dekhege ki py hai kya useme
# s="123pythondev"
# print(s.find("java"))  o/p -1
# s="123pythondev"
# print(s.find("pyd")) o/p -1
# s="123pythondev"
# print(s.index("java")) o/p substring not found
# s="123pythondev"
# print(s.index("pyd"))  o/p ubstring not found
# s="123pythondev"
# print(s.index("pyt")) o/p 3
# s="123pythondev"
# print(s.index("pyt", 0,6)) o/p 3

#   rfind() and rindex()--------------
# s="1234 python developer"
# print(s.rfind("pyt")) o/p 5
# s="1234 python developer"
# print(s.rfind(" pyt"))  o/p 4 kuki print me space di hai pvt ke pehele
# s="1234 python developer"
# print(s.rfind("pytd")) o/p -1

# s="123123"
# print(s.rindex('3')) o/p 5
# s="123123"
# print(s.rindex('1'))    left se check karega jaha 1 mila usse right se index dega
# s="123123" o/p 3
# print(s.rindex('2')) o/p 4
# s="123123"
# print(s.rindex('3',0,5)) o/p - 2 karan string same ghetli jevadhi aahe mhanun tyani 1la 3 ghetla
# s="123123"
# print(s.rindex('3', 0,6)) o/p 5

 #  count --------
# s=[1,2,3,4,5,6,5,1,1]
# print(s.count(1)) o/p 3   1 jo hai 3 bar aaya hai


# s="pythonpythonpython"
# print(s.count("python"))
# s="pythonpythonpython"
# print(s.count("pt")) o/p 0
# s="pythonpythondev"
# print(s.count("ve")) o/p 0
# s="pythonpythonpython"
# print(s.count("0",0,6)) o/p 0
# s="pythonpythonpython"
# print(s.count("py",0,7)) o/p 1
# s="pythonpythonpython"
# print(s.count("py", 0,8)) o/p 2

# s=[1,2,3,4,'akash']
# s1=s[4]  pehele naya varible leke search kiya string fir usmese jo bhi element chaiye use print kiya indexing se
# print(s1[1:])
# print(s[4] [0:]) o/p akash
# print(s[4] [1:4]) o/p kas
# for i in range(5):
#     if i==4:
#         break
#         print(i)

# s=[1,3,5,7,8,4,7,9]
# for i in s:
#     if i%2==0:
#         break
#         print(i)

# s=[1,2,3,4,5]
# for i in s:
#     print(float(i)) o/p 1.0 2.0 3.0 4.0 5.0
#

# replace -----------
# s='python developer'
# s1=s.replace("python", 'java')
# print(s1)   o/p java developer
# s='python developer'
# s1=s.replace("per", 'java')
# print(s1)  o/p python develojava
# s='&*()python 234developer'
# s1=s.replace("*()p", '234')
# print(s1)  o/p &234ython 234developer

# join ----------
# s=('nikhil','python','developer')
# s1=' ++ '.join(s)
# print(s1) o/p nikhil ++ python ++ developer
# s=('nikhil','python','developer')
# s1=' @@ '.join(s)
# print(s1)


# 1)upper() :PYTHON DEVELOPER
# 2)lower()  : python developer
# 3)swapcase() : lower to upper and upper to lower :   pYThoN dEveLOPEr
# 4)title(): Python  Developer
# 5capitalize(): Python developer

# s="PyTHon DeveLOpeR"
# print(s.lower())
# s="PyTHon DeveLOpeR"
# print(s.swapcase())
# s="PyTHon DeveLOpeR"
# print(s.title())
# s="PyTHon DeveLOpeR"
# print(s.capitalize())

# s= input('enter your number')
# print(s)
# if s.isdigit():
#     print('valid number')  o/p 14142525  and invalid number
# else:
#     print('invalid number')
# s= input('enter your number')
# print(s)
# if not s.isdigit():
#     print('valid number')    14142525  and invalid number
#
# else:
#     print('invalid number')

# s= input('enter your number')
# if s.isdigit() and s[0] not in ["7","8","9"]:
#     print ('valid number')
# else:
#     print('invalid number')


# s= input('enter your number')
# if s.isdigit() and s[0] in ["7","8","9"]:
#     print ('valid number')     o/p  enter your number1122334789 and valid number
#     yaha start s[0] 7 8 ya 9 se ho ya ye 7 8 9 kahi bhi lilkh diye to bhi vqlid dikha raha hai but yr 7 8 9 inme se koi bhi 1 s[0] per chiye to hi vlid rahega
# else:
#     print('invalid number')

# s= input('enter the number')
# if s.isdigit() and s[0] in ["7","8","9"] and len(s)==10:
#     print("valid number")    o/p yaha jo hai 7 8 ya 9 me se kio bhi s[0] per aayega to hi valid rehage
# else:
#     print("invalid number")

# s="python123"
# for i in s:
#     if i.isdigit():  o/p 123
#         print(i)

# s="pYThon1234@#$%"
# for i in s:
#     if i.isupper():
#         print(i)   o/p YT

# s= "nik     khil"
# if not s.isspace():
#     print('invalid name')    o/p invalid name


# s= "nik     khil"
# for i in s:
#     if not i.isspace():
#         print('invalid')
#     else:
#         print("valid")


# s="1,2,3,,4,5,6,7,,8,9,9"
# for i in s:
#     if i>str(6):   6 peksha mothe no print karel o/p 7899
#         print(i)

# formating in string_____

# name="nikhil"
# age= 27
# city = "nagpur"
# print("my name is {} and my age is {}".format(name,age))
# print("my name is {0} and my age is {1}".format(name,age))
# print("my name is{n} and my age is {a} and my city is {c}". format(n=name,a=age,c=city))
# s=f"{name},{age},{city}"
# print(s)




# s="ilovemyindia"
# print(s[0:11:2])
# print(s[::2])

# s=f"ilovemyindia {i},{o},{e},{y},{n},{i}"
# print(s)
# s="ilovemyindia"

#  interview questions---------
# s="1a2b3c"
# s1=s.replace("1a2b3c", "123abc")  o/p 123abc
# print(s1)
# s="1a2b3c"
# for i in s:
#     if i.isdigit():  o/p 123
#         print(i)

# s="1a2b3c"
# d=""
# l=""
# for i in s :
#     if i.isdigit():
#         d= d+i
# #          d+=i
#     else:
#          l+=i
# output=d+l
# print("output:",output)

# s = "1a2b3c"
# d = ""
# l = ""
# for i in s:
#     if i.isdigit():     o/p  output: a1  output: ab12  output: abc123
#         d += i
#     elif i.isalpha():
#         l += i           kuki elif conditon ke bad wo output and print line ko lag ke likhana hai
#         output = l+d
#         print("output:", output)

# s="a3b2c1"
# output=""
# l=""
# for i in s:
#     if i.isalpha():
#         l=i
#     elif i.isdigit():
#         output += l + i
#         print("output:", output)
#
#         o/p  --
# output: a3
# output: a3b2
# output: a3b2c1


# s="a3b2c1"
# output=""
# for i in range (0,2):
#     print(i)



# s ="1a2b3c"
# a = (s[0:5:2])  #123
# b = (s[1:6:2])  #abc
# c = a+b
# print(c)  #123abc
# print(s[1:6:2],s[0:5:2])  #abc 123
#print(s[0:5:2],s[1:6:2])  #123 abc

# s= "ilovemyindia"
# print(s[0:12:2])  o/p ioeyni

#  list ---- split()  append() insert() extend()

#  split()---
# s="pythom develper abcd 1234"     whenever we try to split() the string datatype it always converted into list datatype
# d=s.split()
# print(d)  o/p ['pythom', 'develper', 'abcd', '1234']  jaha jaha space hai waha waha seprate ho raha hai

# s="pythomdevelperabcd1234"
# d=s.split()
# print(d)     o/p ['pythomdevelperabcd1234']

# s=12345
# s1=s.split(
#     print(s1)  o/p 'int' object has no attribute 'split'

# s=nikhil123
# s1=s.split()
# print(s1)   o/p name 'nikhil123' is not defined
# s=[1,2,3,4,5,65,6,5]
# s1=[]   o/p [1, 2, 3, 4, 5, 65, 6, 5]
# print(s)
# s=[1,2,3,4,5,65,6,5]
# s1=[]
# print(s)
# s[1] = 200
# print(s)  o/p [1, 200, 3, 4, 5, 65, 6, 5]

#  append() -------
# a=[]  ----empty list aahe       to add the value in the end of the list
# a.append(1)  1 takla to end madhe yeil
# print(a)  o/p [1]
# a=[]
# a.append(2)
# a.append(4)
# a.append(6)
# a.append("nikhil")
# print(a)  o/p [2, 4, 6, 'nikhil']

# s= "nikhil 123456"
# s1=[]
# for i in s:
#     if i.isdigit():           o/p ['1', '2', '3', '4', '5', '6']
#         s1.append(i)
# print(s1)

#  insert()  ---- to insert the element  at the specific index number

# s=[1,2,3]
# s.insert(1,300)
# print(s)   o/p [1, 300, 2, 3]

# s=[1,2,3]
# s.insert(10,300)  10 index value hai jo ki present nahi hai to 300 last me print hogi
# print(s)  o/p [1, 2, 3, 300]

# s=[1,2,3]
# s.insert(1,300)
# print(s)  o/p [1, 300, 2, 3]

#   extend() --------
# to add all the items from one list to the another list
# a1=[1,2,3]
# a2=[4,5,6]
# a2.extend(a1)
# print(a2)   o/p [4, 5, 6, 1, 2, 3]
# a1=[1,2,3]
# a1.extend(a1)
# print(a1)  o/p [1, 2, 3, 1, 2, 3]

# a1=["saurabh", "mrunal", "nikhil"]
# a2=["minal", "parag"]
# a1.extend(a2)
# print(a1)   o/p ['saurabh', 'mrunal', 'nikhil', 'minal', 'parag']
# a1.extend("mrunal")
# print(a1)  o/p['saurabh', 'mrunal', 'nikhil', 'm', 'r', 'u', 'n', 'a', 'l']
# a1.extend("alka")
# print(a1)   o/p ['saurabh', 'mrunal', 'nikhil', 'a', 'l', 'k', 'a']
# a1.extend("123")
# print(a1)    o/p 'saurabh', 'mrunal', 'nikhil', '1', '2', '3']   string per loop lagta hai int per nahi cz int obj is not iterable but string is

# remove------
# s=[1,2,3,4,5,1,2]
# s.remove(5)
# print(s)  o/p [1, 2, 3, 4, 1, 2]
# s.remove(1)
# print(s)   o/p [2, 3, 4, 1, 2]  it only remove 1st occurance from the list

# pop -----
# s=[1,2,3,4,5]
# print(s.pop())
# print(s)  o/p 5   [1, 2, 3, 4]  last element will remove we can also remove specific element
# print(s.pop(3))
# print(s)   o/p [1, 2, 3, 5]
# s=[]
# print(s.pop())  o/p IndexError: pop from empty list

# reverse -----
# s=[3,2,4,5]
# s.reverse()
# print(s) o/p [5, 4, 2, 3]
# print(s.reverse())  o/p None  direct we can not print cz list is changing

# sort -----
# s=[1,24,5,67]
# s.sort()
# print(s)  o/p [1, 5, 24, 67]  by default ascending order it can take digit or string but not both together
# s.reverse()
# print(s)  o/p [67, 24, 5, 1]
# s=("suresh","nikhil","mrunal")
# s1=list(s)
# s1.sort()
# print(s1)  o/p ['mrunal', 'nikhil', 'suresh']

# s=[4,2,3,1]
# s.sort(reverse=True)
# print(s)  o/p [4, 3, 2, 1]

# alising and clonning  ---------

# s=[1,2,3,[4,5,6]]
# print(s[3])  o/p [4, 5, 6]
# print(s[3][1])  o/p 5

# alising ----  means equals to =
# s=[1,2,3]
# s1=s
# print(s) o/p [1, 2, 3]
# print(s1)  o/p [1, 2, 3]    same o/p aur same id aayega
# print(id(s)) o/p 4474472704
# print(id(s1))  o/p 4474472704

# s=[1,2,3]
# s1=[1,2,3]
# s1=s
# print(s)  o/p [1,2,3]
# print(s2)  o/p diff variable liye hai error aayega
# print(id(s))  4439247104
# print(id(s1)) 4439405760     different id aayegi

# s=[1,2,3,4]
# s[1]=900
# print(s)  o/p [1, 900, 3, 4]
# s[1]=50
# print(s)  o/p [1, 50, 3, 4]

#  cloning -----
# s=[1,2,3,4]
# s1=s[:]
# print(s1)  o/p[1, 2, 3, 4]
# s1[0]=40
# print(s1) [40, 2, 3, 4]

# list comprehension------

# s=[]
# for i in range[1,11]:
#     s.append(i)
#     print(s)  o/p  type 'range' is not subscriptable

# s=[i for i in range(1,11)]
# print(s)  o/p [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s=[i * i for i in range (1,8) ]  ---- 1*1 2*2 3*3
# print(s)  o/p [1, 4, 9, 16, 25, 36, 49]

# s=[i * 2 for i in range (1,8) ]
# print(s)  o/p  [2, 4, 6, 8, 10, 12, 14]

# s=[i ** 2 for i in range (1,8) ]
# print(s) o/p  [1, 4, 9, 16, 25, 36, 49]
# s=[x * 2 for x in range (1,6,2)]
# print(s)  o/p [2, 6, 10]

# s=[i*2 for i in range(1,6,2)]
# print(s)   o/p   [2, 6, 10]
# s2=[x if x%2==0 else None  for x in range(10)  ]
# print(s2)
# s= input("enter your full name")
# vowels="aeiou"
# s2 = [x for x in s if x in vowels]
# print("vowels inside the full name")
# print(s2)

# s=[6,7,8,9,1,2,3,4]      adittion of all element
# addition= sum([x for x in s])
# print(addition)

# s=[6,7,8,9,1,2,3,4]        sum of all even numbers
# output = sum([x for x in s if x%2==0])
# print(output)

# s=[6,7,8,9,1,2,3,4]     sum squares of all the element
# output= sum([x**2 for x in s])
# print(output)


# tuple -------------
# s=()
# s=(10)
# s= 10,20,30
# print(type(s))  o/p tuple


# list1=[1,2,3,4]
# t=print(tuple[list1])   o/p tuple[[1, 2, 3, 4]]
# print(t)     o/p none

# s=(1,2,3,4)
# print(s[1:1000])  o/p (2, 3, 4)


# s1=(1,2,3)
# s1[1]=100
# print(s1)  o/p TypeError: 'tuple' object does not support item assignment

# s=(1,2,3)
# s1=2
# print(s*s1)  o/p (1, 2, 3, 1, 2, 3)
# s=(1,2,3)
# print(len(s))  o/p 3
# s=(1,1,1,3,3,3)
# print(s.count(2)) o/p 0
# s=(1,12,1,33,3,3)
# print(s.count(1))  o/p 2

# s=[1,2,2,3,3]
# print(s.index(2)) o/p 2
# s=(4,1,3,2)

# t1= sorted(s)
# print(t1)   o/p  [1, 2, 3, 4]

# s=(4,1,3,2)
# t1= sorted(s)
# print(t1)
# s1=sorted(s,reverse=True)
# print(s1)


# s=[4,8,1,0,2,8,0,10,11,54]
# s.sort()
# print(s[-3])   o/p 10  we have to find out 3rd top

# s=[4,8,1,0,2,8,0,10,11,54]
# s.sort(reverse=True)
# print(s)   o/p[54, 11, 10, 8, 8, 4, 2, 1, 0, 0]
# print(s[2])  o/o 10

# s=[4,8,1,0,2,8,0,10,11,54]
# s1=sorted(s,reverse=True)
# print(s[2])    o/p 1

# f=(1,2,3,[2,3,4],89,"nikhil")
# s1=f[3]
# print(s1)  o/p [2, 3, 4]
# s1.append("nikhil")
# print(s1)  o/p [2, 3, 4, 'nikhil']
# print(f)  o/p (1, 2, 3, [2, 3, 4, 'nikhil'], 89, 'nikhil')
# print(f[5] [0:3]) o/p nik

#  min and max -------it works on list well as on tuple
# s=(10,20,34,56)
# print(min(s))
# print(max(s))

# packing & unpacking ---------

# a=20
# b=10 umpacked
# c=30
# s=a,b,c    packed
# print(s)  o/p  (20, 10, 30)
#
# s=(20,30,50)
# a,b,c=s
# print(a)
# print(b)   unpacked
# print(c)

# --- set ------
# s={}
# print(type(s))  o/p  <class 'dict'>  cz its empty
# s=set()
# print(type(s))  o/p <class 'set'>

# s=[1,2,3,5,6,1,2,3]
# s1=set(s) list me hai use typcast kiya set me
# print(s1)  o/p {1, 2, 3, 5, 6}

# s2= range(5)
# print(set(s2))  o/p {0, 1, 2, 3, 4}

#  ---- add---
# s={1,2,3,4}
# s.add(5)
# print(s)  o/p {1, 2, 3, 4, 5}

# ---- update ----
# s={1,2,3}
# s.update(5,6,7)
# print(s)   o/p TypeError: 'int' object is not iterable

# s={1,2,3}
# s.update(5,6,7,"nikhil")
# print(s)   o/p TypeError: 'int' object is not iterable

# s={1,2,3,4}
# s1=[10,20,30]
# s.update([10,20,30])
# print(s1)
# s.update(s1, range(11,15))
# print(s)   o/p {1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 30}

# --- copy ----
# s={1,2,3,4}
# s1=s.copy()
# s.add(6)
# print(s)  o/p {1, 2, 3, 4, 6}
# print(s1)  o/p  {1, 2, 3, 4}

#  ----- pop ----
# s={2,3,4,5}
# print(s.pop())
# print(s)  o/p 2      {3, 4, 5}

# s={2,3,4,5,"nikhil",2,3}
# print(s.pop())
# print(s)  o/p nikhil   {2, 3, 4, 5}

#  ---- remove ----
# s={1,2,2,4}
# s.remove(2)
# print(s)   o/p {1,4}
# s={12,3,4}
# s.remove(10)
# print(s)   o/p KeyError: 10

#  ---- discard------
# s={1,2,3,4}
# s.discard(3)
# print(s)  o/p  {1, 2, 4}

# ----- union (|) ---
# s={1,2,3,4}
# s1={3,4,2,5}
# print(s | s1)   o/p {1, 2, 3, 4, 5}
# print(s.union(s1))  o/p {1, 2, 3, 4, 5}

#  ---- intersection  (&) ---
# s={1,2,3,4,5}
# s1={3,4,5,6}
# print(s.intersection(s1))  o/p {3, 4, 5}
# print(s & s1)    o/p {3, 4, 5}

# ---- difference (-) -----
# s={1,2,3,4,5}
# s1={3,4,5,6}
# print(s - s1)   o/p  {1, 2}
# print(s1 - s)  o/p {6}
# print(s.difference(s1))
# print(s1.difference(s))

# ---- symmetrical difference   ----
# s={1,2,3,4}
# s1={3,4,5,6}
# print(s ^ s1)  o/p {1, 2, 5, 6}
# print(s1 ^ s)   o/p {1, 2, 5, 6}

# ----- set comprehension ----
# s={i*i for i in range (5)}
# print(s)

#  take a name through input and find out vowels without repetation--
# s="nikhil charmore"
# s1=set(s)
# print(s1)   o/p {'k', 'n', 'o', 'h', 'm', 'r', 'e', 'l', 'i', ' ', 'a', 'c'}

# s="nikhil charmore"
# s1=set(s)
# s2={"a","e","i","o","u"}
# f=s1.intersection(s)
# print(f)      o/p {'r', 'e', 'l', 'h', ' ', 'm', 'i', 'a', 'o', 'n', 'c', 'k'}

# s="nikhil charmore"
# s1=set(s)
# f=s1.intersection(s)
# print(f)     o/p {'c', 'k', 'l', 'n', 'm', 'o', 'a', 'r', ' ', 'e', 'h', 'i'}


# s="nikhil 234 charmore"
# s2="alka 245 charmore"
# s3=set(s)
# s4=set(s2)
# f=s4.difference(s3)
# print(f)   o/p  o/p set()

# s="nikhil"
# s1=set(s)
# f=s1.intersection(s)
# print(f)   o/p {'h', 'n', 'l', 'k', 'i'}


# --------dictionary------ {}


# d={(1,2,3,): "mrunal"}
# print(type(d))           tuplr me likh sakte hai but list allow nahi hain

# s={}  or
# d= dict()
# s['name'] = "nikhil"
# s['age']  = 30
# s['mo']  = 9730103904
# # print(s)     o/p {'name': 'nikhil', 'age': 30, 'mo': 9730103904}
#
# s['mo']  = 9960742298
# print(s)    o/p {'name': 'nikhil', 'age': 30, 'mo': 9960742298}

# s={'mn':5,'sw':4,'nc':3,'ns':5}
# del(s['nc'])
# print(s)    o/p {'mn': 5, 'sw': 4, 'ns': 5}
# print(s['nc'])   o/p 3 to see the product value

# d=dict()
# d[100]='nik'
# d[20]='may'
# print(d)    o/p {100: 'nik', 20: 'may'}
# d.clear()   o/p {}
# print(d)

# d={"a":1,"b":3,"c":4}
# print(d["z"])  o/p KeyError: 'z'
#  ---- get ----
# print(d.get("z"))    o/p None
# print(d.get("a"))  o/p 1

# ---- pop()---
# d={"a":1,"b":3,"c":4}
# print(d.pop("a"))  o/p 1 key remove hogi aur o/p me uski value print hogi
# print(d)   o/p 1  {'b': 3, 'c': 4}


# ---popitem()-----
# d={"a":1,"b":3,"c":4}
# print(d.popitem())
# print(d)   o/p ('c', 4)   {'a': 1, 'b': 3}

#   ----important ----
# keys()
# s={"sci":30,"math":30,"marathi":60}
# print(s.keys())  o/p dict_keys(['sci', 'math', 'marathi'])

#  to iterate each keys we use for
# s={"sci":30,"math":20,"marathi":60}
# for i in s.keys():
#     print(i)
#            o/p sci
#                math
#                marathi
# for i in s:
#     print(i)   o/p same hi aata hai

# print(s.values())   o/p dict_values([30, 20, 60])
# for i in s.values():
#     print(i)   o/p 30 20 60

# -----items()------ to show the key and value from the dict

# for a,b in s.items():
#     print(a,b)
# # o/p
# sci 30
# math 20
# marathi 60

# -----setdefault---
# s={'sci': 30,'math': 40,'marathi':60}
# s1=s.copy()
# s1['sci'] =50
# print(s1)    o/p {'sci': 50, 'math': 40, 'marathi': 60}
# print(s.setdefault('sci',70))   o/p 30

# -- update ----

# s={'sci': 30,'math': 40,'marathi':60}
# s.update({'java':80})
# print(s)  o/p {'sci': 30, 'math': 40, 'marathi': 60, 'java': 80}

# s=[1,1,2,3,4,5,6]
# d=set(s)
# print(list(d))


# --- dict comprehension -- imp coding interveiw

# d={k:v}
# d={x:x*x for x in  range (1,11)}
# print(d)   o/p 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# ---- function------
# def add(x,y):
'''here we are adding the 2 numbers '''
#     print(x+y)
# add(10,5)

# 2 digit division  make sure denominator is not zero---
# def div(a,b):
#     if b==0:
#         print("cant devide the number")
#     else:
#         output=a/b
#         print(output)
# div(10,0)
# div(4,3)
# div(6,2)

# --- print and return ----
# def wish():
#     print("hello")
# wish()  o/p hello

# def wish1(name):
#     return f"hello {name}"
# a = wish1("nikhil")
# print(a)

# def wish():
#     print("hello")
# print(wish())    o/p hello  None

# def wish1():
#     return " hello all"
# s= wish1()
# print(s,"nikhil")    o/p hello all nikhil
# s1 = wish1()
# print(s1,"developer")  o/p hello all developer

# def oddeven(a):
#     """ using print finding odd even """
#     if a%2==0:
#         print("the number is even")
#     else:
#         print("the number is odd")
# oddeven(10)
# oddeven(5)

# def oddeven(a):
#     """we are using here return and return always use with condition """
#     if a%2==0:
#         return("the number is even")
#     else:
#         return("the number is odd")
# b=oddeven(7)
# print(b)

# def operation(a,b):
#      add= a+b
#      sub=a-b
#      mul=a*b
#      div=a/b
#      print(add)
#      print(sub)
#      print(mul)
#      print(div)
# operation(10,4)

# def maths(a,b):
#     print(a+b)
#     print(a/b)
#     print(a*b)
#     print(a-b)
# maths(15,6)

# def operation(a,b):
#     return(a+b)
# a=operation(1,2)
# print(a)
# def operation1(a,b):
#     return(a-b)
# b=operation1(2,4)
# print(b)

# types of argument ---  ----- positional argument----
# def add(a,b,c): -- formal argument
#     print(a)
#     print(c)
#     print(b)
# add(3,4,6)   ---- actual argument

# ----- keyword argument  ---
# def keywordss(name,age):
#     print("my name is", name, "and my age is", age)
# keywordss(name="nikhil",age=31)   o/p my name is nikhil and my age is 31

# def keywordss(name,age):
#     print("my name is", name, "and my age is", age)
# keywordss(age=31,name="nikhil")      o/p same aayega cz here sequence is not matter but the count is matter while callling the function

# def keywordss(name,age):
#     print( name, age)
# keywordss(age=31,name="nikhil")   o/p nikhil 31

# def wish(name,age):
#     print("my name is", name, "and my age is", age)
# wish("nikhil",31)

# ---- default argument ---
# def wish(name="nikhil",age=31):
#     print(name,age)
# wish()     o/p nikhil 31   in default we already gets value while defining fuction so that we dont need to call it again it will leads to override
#          but we can also put values from our side

# def wish(name="nikhil",age=31):
#     print(name,age)
# wish()
# wish("mac",31)


# ------ variable length arguments -----

# ------ *args  ----- we can take any variable instead of arg * is imp ex. *a,*b
# def wish(*args):
#     for i in args:
#         print(i)
# wish(1,2,3,4)
# wish(2,3,4,5,)
#
# def wish1():
#     wish(55,6,7,3,4)
# wish1()

#  ----- **kwargs ----

# def wish(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"-",v)
# wish(name="nikhil",age=31,city="nagpur")
# print(" ")     # ye space ke liye 2no me
# wish(city="nagpur",age=31)

#  o/p --
# name - nikhil
# age - 31
# city - nagpur
#                                   print(" ")
# city - nagpur
# age - 31

# ----- global variable and local variable ---
# a=10       #we declare variable outside the function called global variable
# def add():
#     print(a)
# def add1():
#     print(a)
# add()
# add1()

# a=10
# def add():
#     b=20     #----- this is a local variable where we always declare witihn the fucntion
#     print(a)
#     print(b)
# add()

# a=10
# def add():
#     b=20
#     print(b)
#
# add()
# print(a)

# a=10
# def add():
#     b=20
#     print(b)       #after declaring global variable we can define multiple functions
# def add1():
#     print(a)
# add()
# add1()

# a=10
# def add():
#     a=20
#     print(a)    same variable decalre kiya hai to o/p me hamesha local variable ka hi aayega value
#
# add()    o/p 20

# --- global() ----
# a=10
# def add():
#     global a     #-- global variable ki value change karni hai to global keyword ka use hota hai
#     a=50
#     print(a)
# add()

# a=10
# def add():
#     global a
#     a=50
#     print(a)
# def add1():
#     b=34
#     print(b)
# add()
# add1()

# a=10
# def add():
#     global a
#     a=50
#
# def add1():
#     print(a)     #naya fuction bnake waha a ki value print ki hain
# add()
# add1()

# ----- globals() ---
# a=10
# def add(a):
#     a = 50
#     print(a)           # o/p 50
#     print(a+a)   # o/p 100
#     print(globals()['a'])    #to print local and global variable
#
# add(a)



#  ---- lambda function ----
# syntax : s= lambda n: n*n    -- we passed parameter always assign variable
# s= lambda n:n*n
# print(s(3))  0/p 9

# s= lambda a,b: a if a>b else b
# print(s(10,20))

# ---- filter function ----
# syntax: filter(function,sequence)

# d=[1,2,3,4,5,6]
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# s=filter(even,d)
# print(s)      #o/p <filter object at 0x1055491b0>  aisa o/p aaya matlab wo location dikha raha hai

# d=[1,2,3,4,5,6]
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# s=list(filter(even,d))     #list me type cast kiya hai o/p ke,liye
# print(s)   o/p [2, 4, 6]

# d=[1,2,3,4,5,6]
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# s=tuple(filter(even,d))  #tuple me aur set me bhi kar sakte hai except dictionary
# print(s)

# s=[1,3,4,6,7,11]
# odd= list(filter(lambda x:x%2!=0, s))
# print(odd)


# s=[2,3,4,5,6]
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# s1=list(filter(even,s))
# print(s1)
# s2=[3,4,5,6,7,8,9,3,4,5,6]
# s3=list(filter(even,s2))
# print(s3)



# s=[1,2,3,4,5,6,7,8,9,10]
# even= list(filter(lambda x : x%2==0,s))
# print(even)     o/p [2, 4, 6, 8, 10]

# --- Map ---
# syntax: map(function,sequence)
# d=[1,2,3,4,5]
# def double(x):
#     return x*2
# s=list(map(double,d))
# print(s)     o/p [2, 4, 6, 8, 10]

# d=[1,2,3,4,5,6]
# def square(a):
#     return a**2
# s= list(map(square,d))
# print(s)      o/p [1,4,9,16,25,36]

# d=[1,2,3,4,5,6]
# square=map(lambda a:a**2,d)
# print(list(square))

# a=[1,2,3]
# b=[4,5,6]
# sum=map(lambda a,b: a+b,a,b)
# print(list(sum))  o/p [5,7,9]

# s=[1,2,3,4,5,6]
# d=0
# for i in s:
#     # print(d+i) o/p 1 2 3 4 5 6
#     d=d+i
# print(d)   o/p 21   ADDITION OF ALL ELEMENT

# --- reduce() ---- it provide filename called functools inbuilt file from that we can import reduce()
# a=10
# b=20
# c=30
# def reduce():
#     from functools import reduce *
    #from functools import reduce,a,b,c



# from functools import *
# l=[1,2,3,4,5,6]
# s=reduce(lambda x,y : x+y,l)
# # reduce(function,sequence)
# print(s)   #o/p 21

#  using function
# from functools import *
# a=[1,2,3,4,5,6]
# def add(x,y):
#     return x+y
# a1=reduce(add,a)
# print(a1)
#
# def mul(x,y):
#     return x * y
# s=reduce(mul,a)
# print(s)  o/p 720

# --- function alising -----
# def wish():
#     print("hello")
# nikhil=wish
# nikhil()   o/p 2 no ke hello aayenge
# wish()

#   Nested function ----
# def wish():
#     print("this is a outer function")
#     def wish1():
#         print("this is inner function")
#     wish1()
# wish()


# --- decorator ----- most imp in terms of interview

# def wish1(wish):
#     def inner(name):
#         if name == "mac":
#             print("s/w developer")
#         elif name == "cici":
#             print("designer")
#         else:
#             wish(name)
#     return inner
#
# @wish1
# def wish(name):
#     print("hello",name)
# wish("nikhil")
# wish("cici")
# wish("mac")

# def wish1(wish):        ---- paramter wish liya hai wo hum kuch bhi le sakte hai but real time me #func lete hai
#     def inner(name):
#         if name == "mac":
#             print("s/w developer")
#         elif name == "cici":
#             print("designer")
#         else:
#             wish(name)
#     return inner
#
# @wish1
# def wish(name):
#     print("hello",name)
# wish("nikhil")
# wish("cici")
# wish("mac")

#   division of 2 no is value greater than 50 print value is not in range
# def decor(div):
#     def inner(a,b):
#         if a>= 50:
#             print("NR value is greater than 50")
#         else:
#             div(a,b)
#     return inner
#
# @decor
# def div(a,b):
#     print(a/b)
# div(10,2)
# div(10,60)
# div(60,20)

#     using decorator function we have to divide parameter if denominator value is 0 then print cant divide by 0
""" here we are doing division of 2 number """
# def decor(func):
#     def inner(a,b):
#         if b == 0:
#             print("cant divide by 0 ")
#         else:
#             func(a,b)
#     return inner
#
# @decor
# def div(a,b):
#     print(a/b)
# div(20,4)
# div(20,0)

# def decor(func):
#     def inner(a):
#         if a%2 == 0:
#             print("its an even number")
#         else:
#             print("odd number")
#
# #
# #     return inner
# #
# # @decor
# # def even(a):
# #     print(a%2)
# # even(10)
# # even(5)


# def decor(func):
#     def inner():
#         print("before main function")     o/p 1. before main function
#         func()
#         print("after main function")     o/p 3.after main function
#     return inner
#
# @decor
# def main():
#     print("main function")              o/p 2. main function
# main()

 # o/p
# before main function
# main function
# after main function


# s= "i love python"
# print(s[::-1])    o/p  nohtyp evol i
#  expected output -  python love i

# s = "I Love Python"
# """ expected output -  python love i"""
# reverse = " ".join(s.split()[::-1])
# print(reverse)

# """ using lambda function"""
# s= lambda s1: " ".join(s1.split()[::-1])
# print(s("I Love Python"))   o/p Python Love I


# ---- generator  ----
# def wish():
#     yield "abcd"
#     yield "1234"
# s=wish()
# # print(type(s))   o/p <class 'generator'>
# print(next(s))   o/p  abcd
# print(next(s))   o/p  1234

# def wish():
#     yield "a"
#     yield "b"
# s=wish()
# print(s)   o/p <generator object wish at 0x10b276350>
# print(list(s))  0/p ['a', 'b']
# print(tuple(s))  o/p  ('a', 'b')
# print(set(s))   o/p {'b', 'a'}

# def wish():
#     yield "a"
#     yield "b"
# s=wish()
# for i in s:
#     print(i)  #o/p a b

# def gen():
#     for i in range(1,6):
#         yield(i)
# s=gen()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

# def gen():
#         yield 1
#         yield 2
#         yield 3
#         yield 4
#         yield 5
# s=gen()
# for i in range(1,6):
#     print(next(s))  #o/p 1 2 3 4 5

# def number():
#     num = 1
#     while True:
#         yield num
#         num +=1
#
# s=number()
# for num in range(5):
#     print(next(s))       # o/p 1,2,3,4,5

# ---- fibonacci -------
# The next is the sum of previous 2 numbers
# Eg: 0,1,1,2,3,5,8,13,21,...

# def fib():
#     a,b= 0,1
#     while True:
#         yield a
#         a,b=b,a+b
# s=fib()
# for i in range(10):
#     print(next(s))   # o/p 0 1 1 2 3 5 8 13 21 34
         #or
# for i in fib():
#     if i>100:
#         break
#     print(i)  # o/p1 1 2 3 5 8 13 21 34 55 89

# def countdown(num):        -- interview que ---
#     while num > 0:
#         yield num
#         num = num - 1
# d=countdown(5)
# print(next(d)) o/p 5
# print(next(d)) o/p 4
# print(next(d)) o/p 3
# print(next(d)) o/p 2
# print(next(d)) o/p 1
# print(next(d))   o/p  StopIteration

# def countdown(num):
#     while num > 0:
#         yield num
#         num = num - 1
# d=countdown(5)
# # print(d)  o/p <generator object countdown at 0x10b9bdcc0>
# for i in d :
#     print(i)    0/p 5,4,3,2,1

# def countdown(num):
#     count=10
#     while count > 0:
#        yield count
#        count -=1
# d=countdown(5)
# for i in d:
#     print(i)


# def countup(num):
#     current = 1
#     while current <= num  :
#         yield current
#         current = current + 1
# d=countup(5)
# for i in d:
#     print(i)    o/p 1,2,3,4,5

# def countup(num):
#     count = 1
#     while count < 5 :
#         yield count
#         count = count + 1
#         # count += 1
# d=countup(5)
# for i in d:
#     print(i)


#  -- modules and package ----

# x=10
# y=20

# a=20
# def wish(name):
#     return f"{name} how are u metalhead"
# s=wish("nikhil")
# print(s)

# """ """   --> doc string hai ye

# class B:
#     """this is a doc string """
# print(B.__doc__)

# class C:
#     def __init__(self): -->this is constructor where we always define it once
#         self.a=10       --> we can write multiple variable (instance variable)
#         self.b=20
#     def In(self):               --> we can write multiple methods as well (instance method)
#         print(self.a + self.b)
# s=C()   --> refrence variable  also to create a class we have to create new variable
# s.In()   ---> to call instance method

# class C:
#     def __init__(add):
#         add.a=10
#         add.b=20
#     def im(add):
#         print(add.a + add.b)
# s=C()
# s.im()

# class C:
#     def __init__(add):
#         add.a=10
#         add.b=20
#     def e(self):
#         print(self.a + self.b)
# s=C()
# s.e()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"{self.name},{self.age}")
#         print(f"The Name is {self.name},the age is {self.age}")
# s=Student('nikhil',30)
# s.display()
# s1=Student('mac',40)
# s1.display()


# class Oddeven:
#     def __init__(self,a):
#         self.a=a
#     def output(self):
#        if self.a%2==0:
#            print("the number is even",self.a)
#        else:
#            print ("the number is odd",self.a)
#
# s=Oddeven(7)
# s.output()
# s1=Oddeven(10)
# s1.output()

# class Oddeven:
#     def __init__(self,a):
#         self.a = a
#     def output(self):
#         if self.a%2 !=0:
#             print("the number is odd",self.a)
#         else:
#             print("the number is even",self.a)
# s=Oddeven(12)
# s.output()

# class Exercise:
#     def __init__(self):
#         self.a=30
#     def wish(self):
#         self.b=35
# s=Exercise()
# s.wish()    o/p wish call kiya to b ki value bhi aayegi
# s.d=40
# print(s. __dict__)     o/p sirf ye print kiys to {'a': 30, 'd': 40}
#  o/p -- {'a': 30, 'b': 35, 'd': 40}


# class N:
#     def __init__(self):
#         self.a=10
#         self.b=33
# s=N()
# s.a=40
# s.b=90
# print(s. __dict__)   o/p {'a': 40, 'b': 90}
#
# s1=N()
# s1.a=1000
# print(s1.__dict__)   o/p {'a': 1000, 'b': 33}

# -- static variable ----

# """if the value of the variable is not vary from object to object """
# class N:
#     x=10    --> static variable inside the class outside the function
#     def __init__(self):
#         self.a=10
#     def wish(self):
#         self.b=30

#  ---- class method---
# class A:
#     x=10
#     y=20
#     @classmethod
#     def wish(cls):
#         # print(cls.x)
#         print(cls.x + cls.y)  o/p 30
#         print(cls.x,cls.y) o/p 10 20
# A.wish()

# class Animal:
#     legs=4
#     @classmethod
#     def wish(cls,name):
#         print(cls.legs)
#         print(f"{name} walk with {cls.legs} legs")
# Animal.wish('dog')

# ----static method -----
# class A:
#     @staticmethod
#     def wish(x,y):
#         print(x + y)
#
# A.wish(10,24)

# class A:
#     x=10
#     def __init__(self):
#         A.y=20
#         print(A.y)
#     def wish(self):
#         A.z=40
#     @classmethod
#     def wish2(cls):
#         A.q=70
#         cls.s=34
#     @staticmethod
#     def wish3():
#         A.l=24
# print(A.__dict__)
# s=A()
# s.wish()

# ---- inheritance ----

# class A:                               #this is single inheritance
#     def first(self):
#         print("this is my parent property")
# class B(A):
#     def second(self):
#         print("this is my base property")
#         super().first()
# s=B()
# s.second()

# -----multiple inheritance-----
# class Parent:
#     def func_parent1(self):
#         print("this is myy p1 property")
# class Child1:
#     def func_child1(self):
#         print("this is my  c1 property")
# class child2(Parent,Child1):
#     def func_child2(self):
#         print("this is my child class")
# s=child2()
# s.func_parent1()
# s.func_child1()
# s.func_child2()

# class Parent:
#     def func_parent1(self):
#         print("this is myy p1 property")
# class Child1:
#     def func_child1(self):
#         print("this is my  c1 property")
# class child2(Parent,Child1):
#     def func_child2(self):
#         print("this is my child class")
#         super().func_parent1()
#         super().func_child1()
# s=child2()
# s.func_child2()

# ---- multilevel inheritance-----
# class A:
#     def a(self):
#         print("this is my a property")
# class B(A):
#     def b(self):
#         print("this is my b property")
# class C(B):
#     def c(self):
#         print("this is my c property")
# s=C()
# s.a()
# s.b()
# s.c()


# class A:
#     def a(self):
#         print("this is my a property")
# class B(A):
#     def b(self):
#         print("this is my b property")
# class C(B):
#     def c(self):
#         print("this is my c property")
#         super().a()
#         super().b()
#
# s=C()
# s.c()


# s="my name is nikhil"
# """expected output  ym eman si lihkin"""
# # result= "" .join[s[::-1] for i in s]
# s = "my name is nikhil"
# result = " ".join([a[::-1] for a in s.split()])
# print(result)

# ---- polymorphism --
"""poly-many morphism-forms    """

# operator overloading
# method - ----- it does not support in python
# constructor ---it does not support in python

# -- overriding ---
# method overriding
# constructor ----

# class P:
#     def c1(self):
#         print("this is parent class property")
# class Q(P):
#     def c2(self):
#         print("this is child class property")
# s=Q()
# s1=Q()
# s.c1()
# s.c2()
# print("-------")
# s1.c1()
# s1.c2()

"""whatever member present in parent class by default tha member avaialble in child class using inheritance 
if the child class is not satisfied with parent class implementation then child class can allow to redefine
that same method to the child class"""

# class P:
#     def c1(self):      # c1
#         print("this is parent property")
# class Q(P):
#     def c1(self):       # we are redefining the same method using overriding
#         print("this is child property")
#
# s=Q()
# s.c1()

# ----- constructor overriding ----

# class P:
#     def __init__(self):
#         print("ABCDEF")
# class C(P):
#     def __init__(self):
#         print("GHIJKL")
#         super().__init__()
# s=C()

# ---- Encapsulation -----
# class A:
#     def wish(self):
#         print("abcd")
#         a=10+20
#         print(a)
# s=A()      #o/p 30 and abcd
# s.wish()

# class A:
#     def __wish(self):
#         print("abcd")
#         a=10+20
#         print(a)
# s=A()
# s.__wish()  # o/p AttributeError: 'A' object has no attribute '__wish'. Did you mean: '_A__wish'?
# s._A__wish()  #o/p 30 and abcd but in real time ye usee nahi karte hai

# class A:
#     def __wish(self):
#         print("abcd")
#         a=10+20
#         print(a)
#     def b(self):      # new simple methode we have created
#         self.__wish()   # and call the strongly private __wish()
# s=A()
# s.b()    #o/p abcd and 30

# class A:
#     def __wish(self):
#         print("abcd")
#         a=10+20
#         print(a)
#
#     def b(self):
#         super()
# s=A()
# s.b()


































# ---- Regular Expression (regex)-----

# import re
# s="abcd111abcd111abcdef111"
# s1=re.compile("111")  # to search the pattern
# s1.finditer(s)   # to search the pattern by index no and  group  1. start() 2. end() 3. group()




# import re
# s="abcd111abcd111abcdef111"
# s1=re.compile("111")  # to search the pattern
# d=s1.finditer(s)
# for i in d:
#     print(i.start(), i.end(),i.group())        #end () --- end +1

# o/p
# 4 7 111
# 11 14 111
# 20 23 111

#  ---- without compile ----
# s="1234###1234####1345###"
# # a=re.finditer("###",s)   # variable leke bhi kar sakte hai
# a=re.finditer("###","1234###1234####1345###")
# for i in a:
#     print(i.start(),i.end(),i.group())

# o/p
# 4 7 ###
# 11 14 ###
# 19 22 ###





