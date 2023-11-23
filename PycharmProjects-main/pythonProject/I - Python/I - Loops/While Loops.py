# WHILE LOOPS: can execute a set of statements as long as a condition is true.
print("While Loops:")
i = 1
while i < 6:
  print(i)
  i += 1

# The while loop requires relevant variables to be ready. We need to define an indexing variable i
print()

print("Break Statements:")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

print()
print("Continue Statements:")
while i < 6:
  i += 1
  if i == 3:
    # when i == 3, program jumps directly to the next iteration
    continue
  print(i)

print()
print("Else Statements:")
i = 1
while i < 6:
  print(i)
  i += 1
# else: once the condition is false/met, do command:
else:
  print("i is no longer less than 6")