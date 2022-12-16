import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg=MIMEMultipart()
email_sender=input('Sender email')
email_reciever=input('Reciever email')

msg['From']=email_sender
msg['To']=email_reciever
msg['Subject']='Sending the DEM file you requested'
body = "Please find the attachment of the DEM file"

msg.attach(MIMEText(body,'plain'))

part=MIMEBase('application','octet-stream')

attachment=open('raster2.tif','rb')
part.set_payload(attachment.read())
encoders.encode_base64(part)

msg.attach(part)
context=ssl.create_default_context()

print("_______________Email Sending Portal______________________")
email_sender=input('Sender email')
email_sender_password=input('Sender password')

with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(email_sender,email_sender_password)    
    server.send_message(email_sender,'reciver@gmail.com',msg)