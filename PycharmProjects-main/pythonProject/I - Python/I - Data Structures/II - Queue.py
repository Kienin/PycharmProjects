# QUEUE: First In First Out linear data structure
# Deque is preferred over a list in the cases where we need quicker append and pop operations from both the ends of
# the container, as deque provides an O(1) time complexity for append and pop operations as compared to a list that
# provides O(n) time complexity.

from collections import deque

my_queue = deque()

# .append() to add items to the queue
my_queue.append(5)
my_queue.append(10)
print(my_queue)

# .popleft() removes the first item in the queue
print(my_queue.popleft())

print("------------------------------")
print()

# APPEND():
print("APPEND():")
# initializing deque
de = deque([1, 2, 3])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

print("------------------------------")
print()

# POP():
print("POP():")
# initializing deque
de = deque([6, 1, 2, 3, 4])
print("deque: ", de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print("\nThe deque after deleting from left is : ")
print(de)

print("------------------------------")
print()
"""
METHODS:
index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
insert(i, a)        :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.
remove()            :- This function removes the first occurrence of the value mentioned in arguments.
count()             :- This function counts the number of occurrences of value mentioned in arguments.
extend(iterable)    :- This function is used to add multiple values at the right end of the deque. The argument passed is iterable.
extendleft(iterable):- This function is used to add multiple values at the left end of the deque. The argument passed is iterable. Order is reversed as a result of left appends.
reverse()           :- This function is used to reverse the order of deque elements.
rotate()            :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to the left. Else rotation is to right.
"""

# INDEX(element, beginning, ending):
print("INDEX:")
# initializing deque
de = deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print("The number 4 first occurs at a position : ")
print(de.index(4, 2, 5))

# using insert() to insert the value 3 at 5th position
de.insert(4, 3)

# printing modified deque
print("The deque after inserting 3 at 5th position is : ")
print(de)
print()

# using count() to count the occurrences of 3
print("The count of 3 in deque is : ")
print(de.count(3))
print()

# using remove() to remove the first occurrence of 3
de.remove(3)
print()

# printing modified deque
print("The deque after deleting first occurrence of 3 is : ")
print(de)

print("------------------------------")
print()


# Size:
print("SIZE:")
# initializing deque
de = deque([1, 2, 3, 4, 5, 6])
print("Current Deque: ", de)

# printing current size of deque
print(f"Size of Deque: {len(de)}")

# using pop() to delete element from right end
# deletes 6 from the right end of deque
de.pop()

# printing modified deque
print("\nThe deque after deleting from right is: ", end='')
print(de)

# printing current size of deque
print(f"Size of Deque: {len(de)}")
print()

# Accessing the front element of the deque
print("Front element of the deque:", de[0])

# Accessing the back element of the deque
print("Back element of the deque:", de[-1])

print("------------------------------")
print()


# Different Operations:
print("DIFFERENT OPERATIONS:")
# initializing deque
de = deque([1, 2, 3, ])

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4, 5, 6])

# printing modified deque
print("The deque after extending deque at end is : ")
print(de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([7, 8, 9])

# printing modified deque
print("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print("The deque after rotating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reversing deque is : ")
print(de)