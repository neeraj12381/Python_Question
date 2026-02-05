num=int(input("enter the number"))
if num > 0:
    print("Positive number")
    if num % 2== 0:
        print("even")
    else:
        print("odd")
else:
    print(num,"is not positive number") 

# Check if a person is eligible for vote:

age=int(input("enter the age : "))
if age>= 18:
    print("eligible")
else:
    print("not eligible ")    

# take a number as input and check if it is even or odd :
num=int(input("enter the number"))
if num%2==0:
    print(num ," is even number")
else:
    print(num ," is odd number")  


# greater number
num1=int(input("enter the first number  :"))
num2=int(input("enter the second number  :"))
if num1 > num2:
    print(num1 ,"is greater than", num2)
else:
    print(num2,"is greater than ",num1)  


# grade
grade=int(input("enter the marks  :"))
if grade>=90:
    print(grade,"grade A")
elif grade>=75:
    print(grade, "grade B")
elif grade>=50:
    print(grade, "grade C")
else:
    print("fail")     


# leap year
year=int(input("enter the year"))
if year%4==0:
    print(year,"is leap year")
else:
    print("not leap year")

# digit of the number
num=int(input("enter the number"))
if num<10:
    print("single digit")
elif num<100:
    print("double digit")
else:
    print("more than two digit")    

# week
day=int(input("enter the number :"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wensday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("enter a valid day number")


# temperature
celsius=int(input("enter the number :"))
if celsius<0:
    print("Freezing")
elif celsius<=20:
    print("cold")
elif celsius<=35:
    print("Warm")
else:
    print("Hot")     

# positive number
num=int(input("enter the number :"))
if num > 0:
    print("Positive number")
    if num % 2== 0:
        print("even")
    else:
        print("odd")
else:
    print(num,"is not positive number") 

     