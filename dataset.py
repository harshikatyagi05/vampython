#list in pyhton
#list store multiple data
myList =["pawan","ivan","deepanshu"]
#tuple store multiple data
myTuple = ("pawan","ivan","deepanshu")
#set store multiple data
mySet = {"pawan","ivan","deepanshu"}
#dictionary store multiple data in key value pair
myDict = {"name":"pawan","email":"p@gami.com"}

#to check the data types of all above set
print("list:",type(myList),"tuple:",type(myTuple))
print("set:",type(mySet),"dict:",type(myDict))

#how to identify list,set,tuple,dictionary
#list -> [] , tuple -> () , set -> {} , dict -> {:}

#example of data set
mySet = {"pawan","deepanshu","mahi","pawan"}
myTuple = ("pawan","deepanshu","mahi","pawan")
myList = ["pawan","deepanshu","mahi","pawan"]
myDict = {"name":"pawan","age":33,"name":"pawan"}

#access specific data from data set
print("list:",myList[0])
print("tuple:",myTuple[0],"dict:",myDict["name"])

#access complete data from data set
for data in myList:
    print("list",data)
for item in mySet:
    print("set",item)
for value in myTuple:
    print("tuple",value)
for x in myDict.values():
    print("dict",x)            

#to check which data set support duplicate data
print("list",myList,"tuple",myTuple,"dict",myDict,"set",mySet)

#to update the data in all data set
myList[0] = "Tripti"
print(myList)
myDict["name"] = "Tripti"
#print(myDict)
#print(mySet)
#myTuple[0] = "Tripti"
#print(myTuple)
#tuple and set is unchangeable and list and dict is changeable
#list,tuple duplicate item
#set, dict no duplicate item

#add new value in data set
myList.append("saloni")
mySet.add("saloni")
myDict.update({"name":"saloni"})
print("list",myList,"tuple",myTuple,"dict",myDict,
      "set",mySet)

#to remove the data from data set
myDict.pop("name")
myList.pop(0)
mySet.remove("pawan")
print("list",myList,"tuple",myTuple,"dict",myDict,
      "set",mySet)

#to convert tuple to list
convertList = list(myTuple)
print(type(convertList))

convertList.append("rohan")
convertList.pop(2)
print(convertList)
myTuple = tuple(convertList)
print(myTuple) 
