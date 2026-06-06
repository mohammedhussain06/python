print("Hello world")

#Variables in python 
name = "Tony";
age = 35
PI = 3.14

print(name)
print(age)
print(PI)
print(name, age)

#Data types in python 
print(type(name))
print(type(age))
print(type(PI))

#Operators: 
#Arithmetic operators 
print(2+2)
print(2-2)
print(2*2)
print(2/2)
print(2%2)
print(2**2)

#Relational operator 
print(2 == 2)
print(2 != 3)
print(2 <= 4)
print(2 >= 1)
print(2 < 4)
print(2 > 5)

#Assignment operator 
marks = 98
print(marks)
marks += 2
print(marks)
marks -= 2
print(marks)
marks *= 2
print(marks)
marks /= 2
print(marks)

#Logical operator 
var = False
print(not var)
print(5 > 3 and 5 < 10)
print(5 > 3 or 5 < 10)

#Operator precedence
# () > ** > (*, /, %) > (+, -) > (==, !=, >, >=, <, <=) > not, and, or 

#Type conversion and casting
#int -> float, float -> int, int -> bool
ans = int(10 + 5.5)
ans1 = 10 + 14
ans2 = 12 + 13.2
print(type(ans))
print(type(ans1))
print(type(ans2))

#User input
a = input(print("Enter your name"))
print(a)

#Sum of two numbers
a = int(input(("Enter value of a")))
b = int(input(("Enter value of b")))
print("Value of a + b: ", a + b)

#Avvg of two numbers
x = int(input(("Enter value of x")))
y = int(input(("Enter value of y")))
avg = x + y / 2
print("The average of two numbers: ",avg)