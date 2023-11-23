# Counter Function: increases count by n every time function is called

def counter():
    global count
    if 'count' not in globals():
        count = 0
    count += 1
    return count

print(counter())
print(counter())
print(counter())
