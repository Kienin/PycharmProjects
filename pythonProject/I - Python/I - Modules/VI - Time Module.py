import time

# how to find pc epoch(when your computer think times began):

print(time.ctime(0))                              # convert a time expressed in seconds since epoch to a readable string

print(time.time())                                # return current seconds since epoch

print(time.ctime(time.time()))                    # return current date and time

time_object = time.localtime()                    # return all detail regarding time
print(time_object)

# time.strftime(format, time_object)           -> to convert time_object into readable string
                                                  # there are a lot of format; search it up online
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_object = time.gmtime()                       # UTC time
print(time_object)


time_string = "27 December, 2004"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)


time_tuple = (2023, 10, 4, 5, 6,20, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)


time_tuple = (2023, 10, 4, 5, 6,20, 0, 0, 0)
time_string = time.mktime(time_tuple)           # convert to seconds since epoch
print(time_string)

