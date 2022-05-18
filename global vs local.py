"""def user_input():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    return a,b    # In python we can return more than one value

def add(a,b):
    return a+b

a,b=user_input()
#add(a,b)        # if we comment this function than the code will also run
print(a,"+",b,"=",add(a,b))"""

# global variable
#local variable is given more reference than global variable
count=9
def plus():
    global count
    count+=1
def minus():
    global count
    count-=1
print("count=",count)
plus()
plus()
minus()
minus()
print("count=",count)
