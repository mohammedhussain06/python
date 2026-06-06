#Functions:
def hello_world():
    print("Hello woeld")

print(hello_world())
hello_world()

#Sum of two numbers
def sum(a, b):
    sum = a + b
    return sum

a = int(input("Enter two numbers: ",)) 
b = int(input("Enter two numbers: ",))
ans = sum(a, b) 
print(ans)

#avg of numbers
def avg(a, b, c):
    avg = (a + b + c) / 3
    return avg

x = int(input("Enter two numbers: ",)) 
y = int(input("Enter two numbers: ",))
z = int(input("Enter two numbers: ",))
result = avg(x, y, z)
print(avg)

#factorial of a number
def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

p = int(input("Enter number: ",)) 
factorial = fact(p)
print(factorial)