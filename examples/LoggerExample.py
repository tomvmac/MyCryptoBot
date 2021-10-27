import logging
import time

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

f_format = logging.Formatter('%(asctime)s - %(message)s')
fileHandler = logging.FileHandler('files/info.log')
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(f_format)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

price = 4.99
isStupid = False

logger.info('Hello Tom ' + str(price))

logger.info('Hello Again ' + str(isStupid))

time.sleep(5)
logger.info('Bye')


