# thread = a flow of execution; like a separate order of instructions.
#          However, each thread takes a turn running to achieve concurrency

# GIL = global interpreter lock; allows only one thread to hold the control of I - Python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing
# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#             use multithreading

import threading
import time

# sequential list:
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffe():
    time.sleep(4)
    print("You drank coffee")

def shower():
    time.sleep(5)
    print("You showered")



# concurrent list/multithreading:
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=shower, args=())
z.start()

print(threading.active_count())                                     # prints how many threads are running
print(threading.enumerate())                                        # print list of all threads running
print(time.perf_counter())                                          # returns how long for main thread to finish

# thread synchronization (MOVE THIS)
x.join()                                                            # main thread will wait for thread x before execute
y.join()                                                            # main thread will wait for thread y before execute
z.join()                                                            # main thread will wait for thread z before execute

print("-------------------------------------------------")






# DAEMON THREADS = a thread that runs in the background, not important for program to run
#                  your program will not wait for the daemon threads to complete before exiting
#                  non-daemon threads cannot normally be killed; stays alive until task is complete
#              ex. background tasks, garbage collection, waiting for input, long-running processes

import threading
import time

# background:
def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count,"seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

'''
x.setDaemon(True)
print(x.isDaemon())                                                  # check if thread is a daemon thread
'''

answer = input("Do you wish to exit? \n")
