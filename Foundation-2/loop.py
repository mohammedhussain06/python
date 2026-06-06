#while loop 
n = int(input(print("Enter a number")))
i = 1
while (i <= n):
    print("Hello world")
    i += 1

#Multiplication of number
n = int(input(print("Enter a number: ")))
i = 1
while (i <= 10):
    print(n * (i + 1))
    i += 1

#Break and Continue 
i = 1
while (i <= 10):
    if (i % 2 == 0):
        break
    print(i)
    i += 1

print("Outaside the loop")

j = 1
while(i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += i
print("Outside the loop")

#for loop 
#in: membership operator, used to traverse or to check presence in conditional statements
string = "hello"
for var in string:
    print(var)

for i in range(1, 5, 2):
    print(i)

#Sum of N numbers:
n = int(input("Enter the number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum is: ", sum)