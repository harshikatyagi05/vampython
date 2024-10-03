#while loop is used to perform iteration
# until condirion will false

#print the no from 1 to 10
x=1
while x <11 :
    print(x)
    x=x+1

#WAP to print the number from 10 to 1

x=10
while x>0:
    print(x)
    x=x-1

#WAP to print table number
no = int(input("Enter the no of table"))
a = 1
while a < 11:
    print(a * no)
    a = a + 1

#Print the table no    
no = int(input("Enter the number for table"))
a=10
while a > 0:
    print(a * no)
    a=a-1

#WAP to print the pattern using while loop
# 1 4 7 10 14 17
# c=1, operation c = c+3, end point 17
c = 1
while c < 17:
    print(c)
    c = c + 3

#WAP print this pattern 21 16 11 6 1
#logic c=21 operation c=c-5 endpoint 1
c=21
while c > 0:
    print(c)
    c = c-5    

#WAP to print the pattern 1 7 19 25 
#logic e=1 endpoint 26 and operation e=e+6
e=1
while e < 26:
    if e != 13:
        print(e)
    e = e + 6