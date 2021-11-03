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

# print(email)
# print(password)
# print(gateway)
# print(smtp)
# print(port)

#
server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, password)

text = "Hello Tom using configparser"
server.sendmail(email, gateway, text)