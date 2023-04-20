#This code will give the fibonnaci value you input 
x = 1
y = 1
a = int(input("Input sequence value"))
z = 3
#The value of z must be three since the loop, after being completedonce, must have 3 digits to keep the pattern going
while z < a:
	y = x+y
	x = y-x
	z = (z+1)
else:
    print(x+y)