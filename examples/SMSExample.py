import smtplib # sms

botProperties = open("../config/sms-local.properties", "r+")

botProperties.seek(0)
first_char = botProperties.read(1)

botProperties.seek(0)
email = botProperties.readline().split('=')[1].strip()
password = botProperties.readline().split('=')[1].strip()
sms_gateway = botProperties.readline().split('=')[1].strip()
smtp = botProperties.readline().split('=')[1].strip()
port = botProperties.readline().split('=')[1].strip()

server = smtplib.SMTP(smtp, port)
server.starttls()
server.login(email, password)

text = "Hello Tom"
server.sendmail(email, sms_gateway, text)