data = True

with open("new.txt", "r") as f:
    while data:
        data = f.readline()
        if ("Python" in data):
            print("The word has been found")
            break
        print(data)