"""n=int(input("enter the number: "))
i=0
while(i<n):
    print(i)
    i=i+1"""

#write a script to find out given year is a leap year or not
year=int(input("enter a year: "))

if year%400==0 and year%100==0:
    print(year,"is a leap year")
elif year%4==0 and year%100!=0:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")
