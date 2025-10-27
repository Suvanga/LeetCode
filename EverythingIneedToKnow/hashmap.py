#hashmap is aka dictionary in python which is simiar to json in javascript

myMap ={}

myMap["alice"] = 88
myMap["bob"] = 95
print(myMap)

print(len(myMap))  # prints 2
print("")

print("alice" in myMap)  # prints True
print("charlie" in myMap)  # prints False
print("")

# we can also directly write a hashmap with values
myMap = {"alice": 88, "bob": 95}
print(myMap)
print("")

# we can also use dict comprehension to create a hashmap

myMap = {i: i*i for i in range (5)} #this means we can use the key as i and value as i squared from the range of 0 to 4 
print(myMap)  # prints {0: 0, 1: 1,

print("")
#Looping throught the hashmap
for key in myMap:
    print(key, myMap[key])
print("")

#if we dont need the keys we can just loop through the values
for val in myMap.values():
    print(val)

    #last;y of we neec to tdo some sort of unpacking then we can use items()
print("")
for key, val in myMap.items():
    print(key,val)

