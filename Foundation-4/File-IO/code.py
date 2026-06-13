#f = open("sample.txt", "r")
#data = f.readline()
#print(data)

# f = open("sample.txt", "w")
# f.write("We are overwriting \n the complete data")

# f = open("sample.txt", "a")
# f.write("\nSome new text \n being appended")

# f = open("sample1.txt", "x")
# f.write("\nSome new text \n being appended")

# f = open("sample.txt", "r+")
# f.write("123")
# print(f.read())

# f = open("sample.txt", "a+")
# f.write("123")
# print(f.read())

# f = open("sample.txt", "w+")
# f.write("123")
# print(f.read())

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

f.close()