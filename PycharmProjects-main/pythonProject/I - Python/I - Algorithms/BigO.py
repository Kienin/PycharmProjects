# SORT ALGORITHMS:

# LINEAR SEARCH:
def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
        return -1

# BINARY SEARCH:
def binary_search(array, x):
    low = 0
    high = len(array) -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < x:
            low = mid + 1
        elif array[mid] < x:
            high = mid - 1
        else:
            return mid
        return -1

# BUBBLE SORT:
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] == array[j+1], array[j]

# QUICK SORT:
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quick_sort(left) + middle + quick_sort(right)

# MERGE SORT:
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

# INSERTION SORT:
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

# PARTITION SORT:
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

# SELECTION SORT:
def selection_sort(numbers):
  for i in range(len(numbers)):
    index_smallest = i
    for j in range(i + 1, len(numbers)):
      if numbers[j] < numbers[index_smallest]:
        index_smallest = j

    temp = numbers[i]
    numbers[i] = numbers[index_smallest]
    numbers[index_smallest] = temp

# FIBONACCI SEQUENCE:
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  pass

# CREATE MATRIX:
def create_matrix(n):
  matrix = []
  for i in range(n):
    matrix.append([0] * n)
  return matrix

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


