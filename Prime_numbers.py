#This is my second attempt at writing a program to check any value for being prime or composite
#Currently, this program will not work for the value of 1 since it is included in the writing of a
i = int(input("Input any integer:"))
a = 1
x = 1
while a < i:
        a = a+1
        if i%a == 0:
            print("Factor", x)
            print(a)
            int(x)
            x = x+1
if x > 2:
    print("The integer is composite")
if x == 2:
     print("The integer is prime")
