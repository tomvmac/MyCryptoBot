import time
from datetime import datetime
import pytz
from core.util import Constants

def getCurrentDate():
    return time.strftime(Constants.DATE_FORMAT)

def getCurrentTime():
    now = datetime.now(pytz.timezone(Constants.TIME_ZONE_EDT)).strftime(Constants.TIME_FORMAT)
    return now

