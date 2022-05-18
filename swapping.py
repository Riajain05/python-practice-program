#program to swap two data variable using third temporary variable....

"""a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("before swapping number are:")
print("a=",a)
print("b=",b)
print("after swapping number are:")
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)"""


# 2nd method

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("before swapping number are:")
print("a=",a)
print("b=",b)
print("after swapping number are:")
a=a+b
b=a-b
a=a-b
print("a=",a)
print("b=",b)

#3rd method

a=int(input("enter first number: "))
b=int(input("enter second number: "))
print("before swapping number are:")
print("a=",a)
print("b=",b)
print("after swapping number are:")
a,b=b,a
print("a=",a)
print("b=",b)
