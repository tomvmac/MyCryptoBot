import smtplib
from configparser import ConfigParser

# Open config file
config = ConfigParser()
config.read('../config/sms-local.properties')

# Properties
email = config["default"]["email"]
password = config["default"]["password"]
gateway = config["default"]["gateway"]
smtp = config["default"]["smtp"]
port = config["default"]["port"]

def sendMsg(message):
    try:
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, gateway, message)
        server.close()
    except Exception:
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, gateway, message)
        server.close()

