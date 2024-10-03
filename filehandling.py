#create file for saving my laptop password
#open function will create the file when file is not exists and write the file
myPassword = open("password.txt","w")

#write my laptop password in file
myPassword.write("harshika")

#overwrite the new password using user input
#myPassword.write(input("enter new password"))

#read the password from file 
myPassword = open("password.txt","r")
mydata = myPassword.read()
if "macbook" in mydata:
    print("yes")
else:
    print("no") 
#to close file    
myPassword.close()    

#delete the file
import os
os.remove("password.txt")        

#create read write delete csv, excel, json, txt
#create csv file
myCsv = open("myfie.csv","w")
myCsv.write("harshika, payal, anjali, saloni, mahi")

myexcel = open("myexcel.excel.xlsx","w")
myexcel.write("name, pawan, raman, anjali")