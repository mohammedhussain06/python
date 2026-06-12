# It is a key:value pairs
info = {
    "name": "Human",
    "cgpa": 8.91,
    "subjects": ["Maths", "English"]
}
print(info)

#Here keys are the index
print(info["name"])

#Mutablility
info["cgpa"] = 8.95
print(info)

#They are unordered: No order of printing

#Methods
#.keys(): return all the keys
dict = list(info.keys())
print(dict)

#d.values: return all the values
print(info.values())

#d.items: returns key: value pairs
print(info.items())

#d.get(): get value
#d.update(new_item): inserts new item
info.update({"city" : "Mumbai"})
print(info)