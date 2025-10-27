tup = (1,2,3)
print(tup)
print(tup[0])  # prints 1

#tuples are immutable we cannot change the values once assigned
# we can index them, but we can noit modify them
print("")

myMap = {(1,2):3}
print(myMap)
print((1,2) in myMap)  # prints True

# we can do the same thing for the has sets as well 

hashset = set()
hashset.add((1,2))
print((1,2) in hashset)  # prints True

#lists cant be used as keys in hashmap or hashset as they are mutable