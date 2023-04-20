import math
z = str(input("add, subtract, multiply, or divide?"))
a = float(input("a=?"))
b = float(input("b=?"))

x = "multiply"
y = "divide"
c = "add"
d = "subtract"

if z == x:
    p = (a*b)
    print(p)    
if z == y:
    p = (a/b)
    print(p)
if z == c:
    p = (a+b)
    print(p)
if z == d:
    p = (a-b)
    print(a-b)


if p%2 == 0:
    print("The number is even")
else:
	print("the number is odd")
