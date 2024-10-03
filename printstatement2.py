# -> # is used to comment the line
# -> it is also used to define the code meaning
# -> it can also comment and uncomment multiple lines using ctrl +/

# comments example
# write a program to print your name
print("My name is Harshika Tyagi") #print function to display statement

#variables can store the value and it can change at any time
name= "Harshika Tyagi"
#Pass the variables in the print function 
print("My name is "+ name) # + is  used to concatenate the strings

#declare and initialize the multiple variables
age=19
gender= "female"
email="harshikat33@gamil.com"
#pass the multiple variable in print function
#this line give the type error
#Reason for erroe str can't be concatenate with integer
print(f"My name is {name} my age is {age} and gender is {gender} my email is {email}")

#solution 3- using typecasting
ageInString =  str(age)
print("My name  is"+ name +
      "my age is"+ ageInString + "and gender is"+ gender)
#Data types in python 
print(type(name)) # type function return datatype of variable
print(type(age))
#1. str- it can store the string data 
#2. int- it can store the numeric data e.g. age=19
#3. float- it can store the decimal noo e.g. percentage= 75.43

#Typecasting in python:-convert one datatype to aonther datatypes
#e.g. Sometime when we purchase item in float we paid in integer
purchaseItemPrice = 99.32
paidItemPrice = int(purchaseItemPrice)
print("Paid amount is", paidItemPrice)

#Note-> string can't be converted into reason string not ascii

#To get the input from user input() function
collegeName = input("Enter your college name")
collegeFee = int(input("Enter your college fee"))
print("My college name is"+ collegeName)
#Note:- the input function has default return type str
#Add scholarship of 25000 in fees
collegeFee = collegeFee - 25000
print("After scholarship my fee", collegeFee)

#Find the age in year when bornYear and currentYear is given by user
bornYearAge = int(input("Enter your bornYear age "))
currentAge = int(input("Enter your currentAge year "))
presentAge=currentAge-bornYearAge
print("My current age is ",presentAge)


