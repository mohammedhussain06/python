#if, elif, else
age = int(input(print("Enter your age: ")))
if (age >= 18):
    print("You can drive")
if (age >= 21):
    print("You can drink and drive")
else:
    print("You can't drink nor drive")

#Odd or even 
a = int(input(print("Enter a number: ")))
if (a % 2 == 0):
    print("It is an even number")
else:
    print("Odd number")
            
#elif condition
color = input(print("Enter a colour: "))
if (color == "red"):
    print("Stop")
elif (color == "yellow"):
    print("Slow down")
elif (color == "green"):
    print("Go")

#Nesting 
username = input(print("Enter username: "))
password = input(print("Enter password: "))
if (username == "admin" and password == "pass"):
    print("success")
else :
    if (username != "admin"):
        print("Wrong username")
    else:
        print("password is wrong")

