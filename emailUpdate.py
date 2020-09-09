#! /usr/local/bin/python3

import smtplib
import berkeley

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = berkeley.execute()

#The mail addresses and password
sender_address = '####'
sender_pass = '####'
receiver_addresses = ['#######', '#######']
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = ", ".join(receiver_addresses)
message['Subject'] = 'Daily Berkeley Update: ' + mail_content   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_addresses, text)
session.quit()
print('Mail Sent')