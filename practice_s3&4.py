print("Hello World")

#CHECKING FOR TYPE
print(type(2))
print(type(2.3))
print(type(None))
print(type(4*2))
print(type(4/2))
print(type(4//2)) #this returns the value in integer and its rounded
print(type(4**2))
print(type(False)) #false must be typed in lower case
print(type(3.0*1.0))
print(type(~3))
print(type(3| 2))
    #print(type(3 | 2.0)) #This is an error because bitwise operator only work on integers
print(type(print("xx"))) #NoneType

#Operations
    #Remember to always add print if you want to see it in console

print(5+2-9)
print(2+3*5)
print(--5)
    #print(None+7) #Type error: not all types support all operations
print(None)
print(not None) #True
print(4/2)
print(4//2)
print(3.0*1.0)
print(2<3<1)
print(3>(0**0*4))
print(2>1 and 5) #returns 5 because 2>1 is True

#Operations & Variables
a = 6
print(a+2.0)
a/=2 #a becomes 3
print(a)
b = 3
print(a**b)
b -= a #b becomes 0
print(b)
print(b+2)
c = a > b #c is true
print(c)
print(c and a)
print(c)
print(c and a)
print(a+b+c) #In Python Booleans are integers where True=1 and False=0

