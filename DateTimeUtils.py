import time
from datetime import datetime

def getCurrentDate():
    return time.strftime("%m/%d/%Y")

def getCurrentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

