#strings are immutable

word = "python"
word1 = "I love"

#Concatenation
print(word1+ " "+word)

#Indexing
for ch in word:
    print(ch)

#Slicing
print(word[2: 4])
print(word[-4: -2])

#String formatting: dynamic strings
print("language is {}".format("python"))
a = 10
b = 5
print(f"Sum of {a} and {b} is {a + b}")