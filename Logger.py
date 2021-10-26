import logging

def GetLogger():
    # Configure logger for INFO for console and file logging
    logger = logging.getLogger('dev')
    logger.setLevel(logging.INFO)

    f_format = logging.Formatter('%(asctime)s - %(message)s')
    fileHandler = logging.FileHandler('logs/app.log')
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(f_format)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)

    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger

