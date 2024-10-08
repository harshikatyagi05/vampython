#error 1
#print(x)

#error handling
try:
    print(x)
except NameError:
    print("'x'is not defined")   

#error 2
#y=1/0
try:
    y=1/0
except ZeroDivisionError:
    print("divide by zero error")         

#error 3 
name = "harshika"
#no = int(name)
try:
    no = int(name)
except ValueError:
    print("string can't convert into integer")    

#error 4
friends = ["ivan","anshu","vani"]
#friends[4]
try:
    friends[4]
except IndexError:
    print("You are calling wrong index")

#error 5
amount = 500
email = "h@gmail.com"
#total = amount + email
try:
    total = amount + email
except TypeError:
    print("string can't convert into integer")     



