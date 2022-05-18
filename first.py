# program to find a given number id odd or even....

a=int(input("enter a number:"))
print(type(a))
b=a%2
print(b)
if a==0:
    print("number is zero")
elif a%2==0:
    print("number is even")
else:
    print("number is odd")
    





"""if we give float valu then value error is arise
if we take ....a=float(input("enter a number:"))
then it will oly give result as odd number"""

