
mylist = ["banana", "cherry", "apple"]
print(mylist)
print("***************************************")
mylist.append("lemon")
print(mylist)
print("***************************************")
mylist.insert(0, "blueberry")
print(mylist)
print("***************************************")
mylist.pop()
print(mylist)
print("***************************************")
mylist.remove("cherry")
print(mylist)
print("***************************************")
mylist.reverse()
print(mylist)
print("***************************************")
mylist.sort()
print(mylist)
print("***************************************")
list = [2, 42, -32, 0, -12, 90]
newlist = sorted(list)
print(list)
print(newlist)
print("***************************************")
list2 = [0] * 5
print(list2)
print("***************************************")
#slicing
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list3[1:5]
print(a)
print("***************************************")
b= list3[::-3]
print(b)
print("***************************************")
#more on lists
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()
list_cpy.append("lemon")
print(list_org)
print(list_cpy)
print("***************************************")
#more onlist 2(code comprehension)
mylist1 = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist1]
print(mylist1)
print(b)
print("***************************************")
#tuples
mytuple = ("Max", 23, "boston")
print(mytuple)

item = mytuple[2]
print(item)
print("***************************************")
#more on tuples
mytuple1 = "max", 25, "boston"

name, age, city = mytuple1
print(name)
print(age)
print(city)
print("***************************************")