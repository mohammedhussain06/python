#Immutable sequence of values

tup = (1, 2, 3, 4, 5, 6)
print(tup)
print(len(tup))

#indexing
print(tup[4])

#Single values can't be created in tuples
t = (1, )
print(t)

#slicing 
print(tup[0:2]) 

#Looping
for val in tup:
    print(val)

sum = 0
for val in tup:
    sum += val

print(sum)

#Methods
#.index(val): returns 1st occurence
print(tup.index(4)) 

#.val: count total occurences
print(tup.count(5))