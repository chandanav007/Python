#go over to our gmail account and setup 2 factor authetication
#generate app password
#create  function to send the mail
from email.message import EmailMessage
import ssl 
import smtplib

email_sender = 'killyben64@gmail.com'
email_password = "ajbh leus bgib rhox"

email_reciever='chandanav007@gmail.com'


subject='Letter to my futureself '
body = """
Hi, I am chandana.How are You?
"""

em= EmailMessage()
em['From']= email_sender
em['TO']= email_reciever
em['subject']=subject
em.set_content(body)

context= ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())






















