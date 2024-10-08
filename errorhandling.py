# error handling or exception handling
#control over the error in programs

#error in program 
#print(x)

#solution
try:
    print(x)
except NameError:
    print("x is not defined")

#2 error type in python
x = "harshika"
y = 8
c = x+y
print(c)       