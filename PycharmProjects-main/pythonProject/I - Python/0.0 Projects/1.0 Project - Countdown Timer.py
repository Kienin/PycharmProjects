# COUNTDOWN TIMER
import time

for seconds in range(10, 0, -1):          # "-1" means it counts down
    print(seconds)
    time.sleep(1)                         # time.sleep(1) means the countdown will lag by 1 second
print("HAPPY NEW YEAR!!!")