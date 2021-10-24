import sched
import time
from datetime import datetime

def print_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

mySched = sched.scheduler(time.time, time.sleep)

while True:
    mySched.enter(10, 1,print_time)
    mySched.run()