#The hashsets are really usefull as we can add and check for existence in O(1) time on average
hashset = set()

#there wont be any duplicate values in a hashset ublike the lists where we can have duplicate values

hashset.add(1)
hashset.add(2)

print(len(hashset))  # prints 2
print(hashset)
print("")


print(1 in hashset)  # prints True
print(3 in hashset)  # prints False
hashset.add(2)  # adding duplicate value, will have no effect

hashset.remove(1)

print(2 in hashset)  # prints True
print(1 in hashset)  # prints False

print("")

# to initialize a hashset with values we can also set a lisys



#list to set conversion
print(set([1,2,3]))  # prints {1, 2, 3}
mySet = {i for i in range (5)} # set comprehension
print(mySet)  # prints {0, 1, 2, 3, 4}
