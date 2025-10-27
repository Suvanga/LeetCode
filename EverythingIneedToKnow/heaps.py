#Heaps are fenerally iused to find the min and max values of the data strucutre in O(1) time and also to insert and delete in O(log n) time
import heapq
minHeap = []    
heapq.heappush (minHeap, 3)
heapq.heappush (minHeap, 1)
heapq.heappush (minHeap, 2)

#min is always at the root of the heap so index 0
print("Min element:", minHeap[0])  # prints 1

print("Min Heap:", minHeap)  # prints [1, 3, 2]

print("")

# we can also use while loop 
while len(minHeap) > 0:
    print(heapq.heappop(minHeap))  # prints 1, 2, 3 in order

print("")

# python does not have max heap so we can use negative values to simulate max heap

maxHeap = []
heapq.heappush (maxHeap, -3)
heapq.heappush (maxHeap, -1)
heapq.heappush (maxHeap, -2)

#Max is always be at 0 
print (-1*maxHeap[0])  # prints 3

while len(maxHeap):
    print (-1*heapq.heappop(maxHeap))  # prints 3, 2, 1 in order

    # Build heap from initial array
print("")
arr = [5, 3, 8, 1, 2]
heapq.heapify(arr)
print("Heapified array:", arr)  # prints a valid min-heap

while arr:
    print(heapq.heappop(arr))  # prints 1, 2, 3, 5, 8 in order