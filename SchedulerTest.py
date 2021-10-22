import sched
import time

def show_name():
    print("Hello Tom")

mySched = sched.scheduler(time.time, time.sleep)

while True:
    mySched.enter(3, 1,show_name)
    mySched.run()