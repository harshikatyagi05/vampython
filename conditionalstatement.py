#condtional statement will check the condition is true or not
#to check the condition we use if else

#WAP to check user eligible for voting
userAge = int(input("Enter your age"))
#Note the default input function return type is string
#for vote userAge must be greater than 18
if userAge > 18:
    print("You'r eligible for voting")
else:
    print("You'r not eligible for voting")

    #Wap to check the gender for metro first compartment 

userGender = input("Enter your gender")
    #to cheeck user is male or female
if userGender == "male":
        print("You can't sit in first compartment")
elif userGender == "female":
        print("You are eligible for sitting in first metro compartment")
else:
        print("You can sit in the first compartment")

        #WAP if gender is female and age greater than 18 -> govt job apply
        #else male age greater than ->18 private job apply

userGender = input("Enter your gender")
userAge = int(input("Enter your age"))
        
if userGender == "female" and userAge > 18:
    print("You are eligible for apply in government job")
elif userGender == "male" and userAge > 18:
    print("You are eligible for apply in private job")
else:
    print("You are not eligible for apply in any job")


