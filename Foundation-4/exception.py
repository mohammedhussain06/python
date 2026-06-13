#try, except, else, finally
try:
    x = int(input("Enter number x: "))
    ans = 10 / x

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Divide by 0 is not allowed")

else:
    print(f"ans: {ans}")

finally:
    print("End of the program")