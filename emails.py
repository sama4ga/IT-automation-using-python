#!/usr/bin/env python3
from email.message import EmailMessage
from fileinput import filename
import smtplib, mimetypes, os

def generate_email(sender, recipient, subject, body, attachment_path=""):
  message = EmailMessage()
  message['To'] = recipient
  message['From'] = sender
  message['Subject'] = subject
  message.set_content(body)

  if attachment_path != "":
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)
    with open(attachment_path, 'rb') as f:
      message.add_attachment(f.read(),
                              maintype=mime_type,
                              subtype=mime_subtype,
                              filename=attachment_filename )
  return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()