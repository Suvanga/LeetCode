
s= "abc"

print(s[0:2])  # prints 'ab'
print("")

#we can not modify the string as strings are immutable
s += "d"  # this creates a new string
print(s)
print("")

#looping through a string
for char in s:
    print(char)
print("")

# we can change the type of string to a list to modify it
print(int("123") + 1)  # converts string to integer and adds 1
print(str(123) + "4")  # converts integer to string and concatenates "4"
print("")

# we can also get the ascii value of a character using ord() and chr() functions
print(ord('a'))  # prints 97
print(chr(97))   # prints 'a'
print("")

# we can alsoo append a list of strings using join function
str_list = ["Hello", "World", "from", "Python"]

joined_str = " ".join(str_list)

print(joined_str)  # prints "Hello World from Python"
print("")


