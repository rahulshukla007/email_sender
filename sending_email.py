#a simple python code for sending an email
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

sender_email    = "rahuladhyatm@gmail.com"
receiver_email  = "rahuladhyatm@gmail.com"
subject         = "this is for testing purpose"
body            = "Hi my name is rahul, hope you are doing well"
password        = input("please enter your password: ")

msg = EmailMessage()
msg['Subject']  = subject
msg['From']     = sender_email
msg['To']       = receiver_email
msg.set_content(body)

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.close()

print('Email sent!')