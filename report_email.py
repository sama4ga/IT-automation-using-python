#!/usr/bin/env python3
import os, datetime, reports, emails

def process_data():
  path = os.getcwd() + "/supplier_data/descriptions"
  # summary = []
  summary = ""
  for file in os.listdir(path):
    with open(os.path.join(path, file), 'r') as opened:
      f = opened.readlines()
      # summary.append("name: {}<br/>weight: {}".format(f[0].rstrip("\n"),f[1].rstrip("\n")))
      summary += "name: {}<br/>weight: {}".format(f[0].rstrip("\n"),f[1])
  return summary

if __name__ == "__main__":
  paragraph = process_data()
  title = "Processed Update on {}".format(datetime.datetime.date)
  attachment_path = "/tmp/processed.pdf"
  reports.generate_report(attachment_path, title, paragraph)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  message = emails.generate_email(sender, receiver, subject, body, attachment_path)
  emails.send_email(message)