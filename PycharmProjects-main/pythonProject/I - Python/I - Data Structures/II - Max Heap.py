# MAX HEAP:  a complete binary tree in which the value in each internal node is greater than or equal to the values
#            in the children of that node. Mapping the elements of a heap into an array is trivial: if a node is stored
#            an index k, then its left child is stored at index 2k + 1 and its right child at index 2k + 2.

# A Max Heap is a Complete Binary Tree typically represented as an array: The root element will be at Arr[0]
# Arr[(i-1)/2] Returns the parent node.
# Arr[(2*i)+1] Returns the left child node.
# Arr[(2*i)+2] Returns the right child node.

# Max Heap methods:
# getMax():     It returns the root element of Max Heap. Time Complexity of this operation is O(1).
# extractMax(): Removes the maximum element from MaxHeap. Time Complexity of this Operation is O(log n) as this
#               operation needs to maintain the heap property (by calling heapify()) after removing the root.
# insert():     Inserting a new key takes O(log n) time. We add a new key at the end of the tree. If the new
#               key is smaller than its parent, then we don't need to do anything. Otherwise, we need to
#               traverse up to fix the violated heap property.

print("MAX HEAP:\n")
# Python3 implementation of Max Heap
import sys

class MaxHeap:

    def __init__(self, maxsize):

        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):

        return pos // 2

    # Function to return the position of the left child for the node currently at pos
    def leftChild(self, pos):

        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    def rightChild(self, pos):

        return (2 * pos) + 1

    # Function that returns true if the passed node is a leaf node
    def isLeaf(self, pos):

        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):

        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],
                                            self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):

        # If the node is a non-leaf node and smaller than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify the left child
                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):

        for i in range(1, (self.size // 2) + 1):
            print("PARENT : " + str(self.Heap[i]) +
                  "LEFT CHILD : " + str(self.Heap[2 * i]) +
                  "RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    # Function to remove and return the maximum element from the heap
    def extractMax(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


# Driver Code
if __name__ == "__main__":
    print('The Max Heap is ')

    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.Print()

    print("The Max value is " + str(maxHeap.extractMax()))

#---------------------------------------------------------
print()

#  heapq class to implement Heap in I - Python.
#  By default, Min Heap is implemented by this class.
#  But we multiply each value by -1 so that we can use it as MaxHeap.

print("HEAPQ CLASS:")
# Python3 program to demonstrate working of heapq

from heapq import heappop, heappush, heapify

# Creating empty heap
heap = []
heapify(heap)

# Adding items to the heap using heappush
# function by multiplying them with -1
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)

# printing the value of maximum element
print("Head value of heap : " + str(-1 * heap[0]))

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
	print((-1*i), end=" ")
print("\n")

print(f"Popping head heap: {str(-1*heap[0])}")
element = heappop(heap)

# printing the elements of the heap
print("The heap elements left : ")
for i in heap:
	print(-1 * i, end = ' ')

#---------------------------------------------------------
print("")

# Using Library functions with dunder method for Numbers, Strings, Tuples, Objects
# Create a Wrapper class for the item in the list.
# Override the __lt__ dunder method to give inverse result.

"""
Python3 program to implement MaxHeap Operation
with built-in module heapq
for String, Numbers, Objects
"""
print()

from functools import total_ordering
import heapq

# why total_ordering: https://www.geeksforgeeks.org/python-functools-total_ordering/

@total_ordering
class Wrapper:
	def __init__(self, val):
		self.val = val

	def __lt__(self, other):
		return self.val > other.val

	def __eq__(self, other):
		return self.val == other.val


# Working on existing list of int
heap = [10, 20, 400, 30]
wrapper_heap = list(map(lambda item: Wrapper(item), heap))

heapq.heapify(wrapper_heap)
max_item = heapq.heappop(wrapper_heap)

# This will give the max value
print(f"Top of numbers are: {max_item.val}\n")

# Working on existing list of str
heap = ["this", "code", "is", "wonderful"]
wrapper_heap = list(map(lambda item: Wrapper(item), heap))
heapq.heapify(wrapper_heap)

print("The string heap elements in order: ")
while wrapper_heap:
	top_item = heapq.heappop(wrapper_heap)
	print(top_item.val, end=" ")

#---------------------------------------------------------
print()
print("\n\nHeap Push Max:")
from heapq import _heapify_max, _heappop_max, _siftdown_max


# Implementing heappush for max_heap
# Time Complexity = Θ(1 + logn)
def heappush_max(max_heap, item):
    max_heap.append(item)
    _siftdown_max(max_heap, 0, len(max_heap) - 1)


def max_heap(arr):
    copy = arr.copy()  # Just maintaining a copy for later use

    # Time Complexity = Θ(n); n = no of elements in array
    _heapify_max(arr)  # Converts array to max_heap

    # Time Complexity = Θ(logk); k = no of elements in heap
    while len(arr) != 0:  # popping items from max_heap
        print(_heappop_max(arr))  # ... unless its empty

    arr = copy  # since len(arr) = 0
    max_heap = []
    # Time Complexity = Θ(nlogk) - since inserting item one by one
    for item in arr:
        heappush_max(max_heap, item)
    print("\nMax Heap is Ready!")
    # Time Complexity = Θ(logk); k = no of elements in heap
    while len(max_heap) != 0:  # popping items from max_heap
        print(_heappop_max(max_heap))  # ... unless its empty


arr = [6, 8, 9, 2, 1, 5]
max_heap(arr)



