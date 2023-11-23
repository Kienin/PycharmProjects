# BIG O NOTATION =  a way of expressing the time (or space) complexity of an algorithm.
#                   It provides a rough estimate of how long an algorithm takes to run
#                   (or how much memory it uses), based on the size of the input.

# O(1):     Constant time. The running time is independent of the size of the input.
# O(n):     Linear time. The running time increases linearly with the size of the input.
# O(n)²:    Quadratic time. The running time is proportional to the square of the size of the input.
# O(log n): Logarithmic time. The running time increases logarithmically with the size of the input.
# O(2^n):   Exponential time. The running time increases exponentially in the size of the input.


# LINEAR SEARCH: O(n)
def linear_search(arr, x):
  for i in range(len(arr)):
    if arr[i] == x:
      return i
  return -1

print("Linear Search:")
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', end=' ')
for num in numbers:
    print(num, end=' ')
print()

key = int(input('Enter a value: '))
key_index = linear_search(numbers, key)

if key_index == -1:
    print(f'{key} was not found.')
else:
    print(f'Found {key} at index {key_index}.')
print("")
# This linear search algorithm has a time complexity of ,
# since the running time is directly proportional to the size of the input.
# If the input size is , the linear search will take n steps to complete.


# BINARY-SEARCH: O(log n)
def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      return mid
  return -1

print("Binary Search:")
numbers = [2, 4, 7, 10, 11, 32, 45, 87]
print('NUMBERS:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

key = int(input('Enter a value: '))
key_index = binary_search(numbers, key)

if key_index == -1:
  print(f'{key} was not found.')
else:
  print(f'Found {key} at index {key_index}.')
print("")
# This binary search algorithm has a time complexity of O(log n)
# since the running time increases logarithmically with the size of the input.
# If the input size is n, it will take approximately log(n) steps to complete the binary search.


# BUBBLE SORT: O(n^2)
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  pass

# This bubble sort algorithm has a time complexity of O(n²)
# since the running time is quadratic in the size of the input.
# If the input size is n, it will take approximately n² steps to complete the bubble sort.


# QUICK SORT: O(n*log n)
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quick_sort(left) + middle + quick_sort(right)

# This implementation of quick sort has a time complexity of O(n log n), on average.
# In the worst case, the time complexity is O(n²), if the pivot is always the smallest or largest element in the array.


# FIBONACCI SEQUENCE: O(2^n)
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  pass

# This implementation of the Fibonacci sequence has a time complexity of O(2^n),
# which is exponential in the size of the input. This is because each call to fibonacci(n)
# results in two additional recursive calls to fibonacci(n-1) and fibonacci(n-2).


# MERGE SORT: O(n)
def merge(numbers, i, j, k):
  merged_size = k - i + 1  # Size of merged partition
  merged_numbers = []  # Temporary list for merged numbers
  for l in range(merged_size):
    merged_numbers.append(0)

  merge_pos = 0  # Position to insert merged number

  left_pos = i  # Initialize left partition position
  right_pos = j + 1  # Initialize right partition position

  #  Add smallest element from left or right partition to merged numbers
  while left_pos <= j and right_pos <= k:
    if numbers[left_pos] < numbers[right_pos]:
      merged_numbers[merge_pos] = numbers[left_pos]
      left_pos = left_pos + 1
    else:
      merged_numbers[merge_pos] = numbers[right_pos]
      right_pos = right_pos + 1
    merge_pos = merge_pos + 1

  #  If left partition is not empty, add remaining elements to merged numbers
  while left_pos <= j:
    merged_numbers[merge_pos] = numbers[left_pos]
    left_pos = left_pos + 1
    merge_pos = merge_pos + 1

  #  If right partition is not empty, add remaining elements to merged numbers
  while right_pos <= k:
    merged_numbers[merge_pos] = numbers[right_pos]
    right_pos = right_pos + 1
    merge_pos = merge_pos + 1

  #  Copy merge number back to numbers
  merge_pos = 0
  while merge_pos < merged_size:
    numbers[i + merge_pos] = merged_numbers[merge_pos]
    merge_pos = merge_pos + 1


def merge_sort(numbers, i, k):
  j = 0
  if i < k:
    j = (i + k) // 2  # Find the midpoint in the partition

    #  Recursively sort left and right partitions
    merge_sort(numbers, i, j)
    merge_sort(numbers, j + 1, k)

    #  Merge left and right partition in sorted order
    merge(numbers, i, j, k)

print("Merge Sort:")
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

#  initial call to merge_sort with index
merge_sort(numbers, 0, len(numbers) - 1)
print('SORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()
# This merge sort algorithm has a space complexity of O(n), since it creates two additional arrays (left and right)
# to store the left and right halves of the input during each recursive call.
# The memory required to store these arrays increases linearly with the size of the input.

print("")
# INSERTION SEARCH:
def insertion_sort(numbers):
  for i in range(1, len(numbers)):
    j = i
    # Insert numbers[i] into sorted part
    # stopping once numbers[i] in correct position
    while j > 0 and numbers[j] < numbers[j - 1]:
      # Swap numbers[j] and numbers[j - 1]
      temp = numbers[j]
      numbers[j] = numbers[j - 1]
      numbers[j - 1] = temp
      j = j - 1

print("Insertion Search:")
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

insertion_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

# QUICK SORT:
def partition(numbers, i, k):
  #  Pick middle element as pivot
  midpoint = i + (k - i) // 2
  pivot = numbers[midpoint]

  #  Initialize variables
  done = False
  l = i
  h = k
  while not done:
    #  Increment l while numbers[l] < pivot
    while numbers[l] < pivot:
      l = l + 1
    #  Decrement h while pivot < numbers[h]
    while pivot < numbers[h]:
      h = h - 1
    """  If there are zero or one items remaining,
          all numbers are partitioned. Return h """
    if l >= h:
      done = True
    else:
      """  Swap numbers[l] and numbers[h],
            update l and h """
      temp = numbers[l]
      numbers[l] = numbers[h]
      numbers[h] = temp
      l = l + 1
      h = h - 1
  return h

# QUICK SORT:
def quicksort(numbers, i, k):
  j = 0
  """  Base case: If there are one or zero entries to sort,
        partition is already sorted  """
  if i >= k:
    return
  """  Partition the data within the array. Value j returned
        from partitioning is location of last item in low partition. """
  j = partition(numbers, i, k)
  """  Recursively sort low partition (i to j) and
        high partition (j + 1 to k) """
  quicksort(numbers, i, j)
  quicksort(numbers, j + 1, k)
  return

print("")
print("Quick Sort:")
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

#  Initial call to quicksort
quicksort(numbers, 0, len(numbers) - 1)
print('SORTED:', end=' ')
for num in numbers:
  print(num, end=' ')
print()

#---------------------------------------------------------------------------------------------------------------------#

# O(1): Constant
def find_min(x, y):
  if x < y:
    return x
  else:
    return y

# O(log N): Logarithmic
def binary_search(numbers, key):
  low = 0
  high = len(numbers) - 1

  while high >= low:
    mid = (high + low) // 2
    if numbers[mid] < key:
      low = mid + 1
    elif numbers[mid] > key:
      high = mid - 1
    else:
      return mid
  return -1  # not found

# O(N): Linear
def linear_search(numbers, key):
  for i in range(len(numbers)):
    if numbers[i] == key:
      return i
  return -1  # not found

# O(N^2): Quadratic
def selection_sort(numbers):
  for i in range(len(numbers)):
    index_smallest = i
    for j in range(i + 1, len(numbers)):
      if numbers[j] < numbers[index_smallest]:
        index_smallest = j

    temp = numbers[i]
    numbers[i] = numbers[index_smallest]
    numbers[index_smallest] = temp

# SELECTION SORT:
print("")
print("Selection Sort:")
numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()

selection_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()

# O(c^N): Exponential
def fibonacci(N):
  if (1 == N) or (2 == N):
    return N
  return fibonacci(N - 1) + fibonacci(N - 2)

print("")


# MAX HEAP:
class MaxHeap:
  def __init__(self, items=[]):
    super().__init__()
    self.heap = [0]
    for i in items:
      self.heap.append(i)
      self.__floatUp(len(self.heap)-1)

  def push(self, data):
    self.heap.append(data)
    self.__floatUp(len(self.heap) -1)

  def peek(self):
    if self.heap[1]:
      return self.heap[1]
    else:
      return False

  def pop(self):
    if len(self.heap) > 2:
      self.__swap(1, len(self.heap) -1)
      max = self.heap.pop()
      self.__bubbleDown(1)
    elif len(self.heap) == 2:
      max = self.heap.pop()
    else:
      max = False
    return max

  def __swap(self, i, j):
    # swap i and j
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def __floatUp(self, index):
    parent = index//2
    if index <= 1:
      return
    elif self.heap[index] > self.heap[parent]:
      self.__swap(index, parent)
      self.__floatUp(parent)

  def __bubbleDown(self, index):
    left = index * 2
    right = index * 2 + 1
    largest = index
    if len(self.heap) > left and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
      largest = right
    if largest != index:
      self.__swap(index, largest)
      self.__bubbleDown(largest)

print("MAX HEAP:\n")
m = MaxHeap([95, 3, 21,])
print("Adding 10 to the max heap:")
m.push(10)
print(str(m.heap[0:len(m.heap)]))
print(str(m.pop))
#---------------------------------------------------------------------------------------------------------------------#

print()
# CREATE MATRIX: O(n^2)
def create_matrix(n):
  matrix = []
  for i in range(n):
    matrix.append([0] * n)
  return matrix

# This algorithm creates an n x n matrix filled with zeros. It does this by creating a new list of n zeros for each row
# of the matrix, and appending each row to the matrix. The space complexity of this algorithm is O(n^2),
# since the size of the matrix grows with the square of the size of the input ().
# The memory required to store the matrix increases proportionally to the size of the input.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original matrix:")
for row in matrix:
    print(row)

matrix[0][1] = 42

print("\nMatrix after changing the element at position (0, 1):")
for row in matrix:
    print(row)

# Counter Function: increases by 1 everytime function is called
def counter():
  global count
  if 'count' not in globals():
    count = 0
  count += 1
  return count