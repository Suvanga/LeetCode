arr = [1,2,3,4,5]
print(arr)

arr.append(6)

arr.pop(0)

arr.insert(1,7) #insert 7 at index 1, insering in to the middle is a O(n) operation

print(arr)

print("")

#initialize arr of size n with all values of 1
n= 5
arr = [1]  * n
print(arr)

print("")

arr = [1,2,3]

print(arr[-1]) #print last element
print("The last element is:", arr[-1]) #print last element

print("")

# we can also slice the arrays 
arr = [1,2,3,4,5]
print(arr[1:4]) #prints elements from index 1 to index 3

print("")

#unpacking

a,b,c = [1,2,3] #number of variables must be equal to number of elements in the array
print(a)

#looping
nums = [1,2,3,4,5,6,7,8,9,10]

print("we can directly loop through an array")
for num in nums:
    print(num)

print("we can uise index to loop through an array")
for i in range(len(nums)):
    print(nums[i])


print("we can also use enumerate to get index and value both")
for index, value in enumerate (nums):
    print("index:", index, "value:", value)


#we acn also zip two arrays together
nums1 = [1,2,3]
nums2 = ['a','b','c']
for n1, n2 in zip (nums1, nums2):
    print(n1, n2)
    print("")
    # we can also do sortin gwith this 
print("we acn also sort an array by simply using the sort function")

arr = [5,2,9,1,5,6]
arr.sort()
print(arr) # if we want to sort in descending order we can use arr.sort(reverse=True)
print("")
# we can Alaso sort a list of strings
strs = ["banana", "apple", "cherry"]    

#if we want to sort in the basis of length of string
strs.sort(key=lambda x: len(x))
print(strs)

print("")

arr = [i for i in range(10)] #array comprehension
print(arr)