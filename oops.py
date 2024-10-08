#OOPS in python

#Object oriented programming -> objects

#class -> it is a container which collects variable, functions
#example -> harshika class
#harshika.fullname = "harshikatyagi"
#harshika.age = 19
#harshika.sleeping()
#harshika.eating()
#harshika.watching()
#class synatx
class ClassName:
    print("this is my class")

class Harshika:
    age = 19
    fullName = "Harshika Tyagi"
    email = "harshikat3@gmail.com"
    def pocketMoney(this,amount):
        print("My pocket money is",amount)    
    def monthlySalary(this , daySalary):
        totalSalary = 31* daySalary
        print("Your monthly salary is",totalSalary)    

#create class object
#object:className= ClassName()
harshika:Harshika = Harshika()
harshika.pocketMoney(15000)
harshika.monthlySalary(int(input("Enter your one day salary")))
print(harshika.fullName, harshika.age, harshika.email) 
