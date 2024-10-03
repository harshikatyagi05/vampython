#list can store multiple data, data can be different types int str
#list can store the duplicate data
#list is an ordered data set - sorting ascending descending

#create list and store the your friends name
friendList = ["ivan","anshu","anjali","vani"]

#print the list of friend names
print(friendList)

#add the age of your friend into list
#append will add the data into end of the list
friendList.append(36)
friendList.append(26)
friendList.append(29)
friendList.append(5)
print(friendList)

#Add the data into list using index no
friendList.insert(0,"Harshika")
print(friendList)

#to access the data using index no
#print(friendList[2])
#print(friendList[0])

#to delete the data from list
#remove will delete the data using value
friendList.remove("ivan")
print(friendList)
friendList.remove("Harshika")
print(friendList)

#pop will delete the data using index
friendList.pop(3)
print(friendList)
friendList.pop(1)
print(friendList)

#access the complete list
#for name in friendList:
#   print(name)

#add the 5 favt city name in list
#add my favt city kasol in first index 0
#remove the last city in list - using pop
#sorting the lsit data
#print the list data

favCity = ["delhi","bhopal","jaipur","indore","lucknow"]
print(favCity)
favCity.insert(0,"kasol")
print(favCity)
favCity.pop(4)
print(favCity)
favCity.sort()
print(favCity)

