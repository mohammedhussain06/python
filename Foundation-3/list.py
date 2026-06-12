#heterogenous mutable sequences of values

marks = [99, 97, 96, 99, 98]
print(len(marks))

#Indexing
print(marks[4])

#Mutability
marks[2] = 78
print(marks)

#slicing
print(marks[2: 5])

#Methods
#Append: Adds one element at the end
marks.append(100)
print(marks)

#Insert(idx, val): insert element at idx
marks.insert(2, 89)
print(marks)

#Sort: Arranges in increasing order
marks.sort()
print(marks)
marks.sort(reverse= True)
print(marks)

#Reverse: reverses the complete order
marks.reverse()
print(marks)

#Using loops with lists 
for val in marks:
    print(val)

x = 98
idx = 0
for val in marks:
    if (val == x):
        print(idx)
        break
    idx += 1
