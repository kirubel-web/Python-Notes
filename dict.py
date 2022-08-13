
mydict = {"name" : "max", "age" : 23, "city" : "Newyork"}
print(mydict)

mydict2 = dict(name = "will", age = "24", city = "Boston")
print(mydict2)

value = mydict["name"]
print(value)
#dictionaries are mutable unlike tuples
mydict["email"] = "max@xyz.com"
print(mydict)

del mydict["email"]
print(mydict)

mydict.popitem()
print(mydict)

#to check a key in dictionary
#if "name" in mydict:
   # print(mydict["lastname"])

try:
    print(mydict["name"])
except:
    print("error")
#to loop through keys
for key, value in mydict.items():
    print(key, value)


#used to merge to dictionaries together
mydict.update(mydict2)
print(mydict)