#!/usr/bin/env python3
import shutil, psutil, emails, os, socket


def send_email(subject):
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "Please check your system and resolve the issue as soon as possible"
  message = emails.generate_email(sender, receiver, subject, body)
  # print(message)
  emails.send_email(message)


cpu_percent = psutil.cpu_percent(interval=1)
disk_usage = shutil.disk_usage("/")
memory_usage = psutil.virtual_memory()
ip = socket.gethostbyname('localhost')

disk_percent_free = (disk_usage.free/disk_usage.total)*100

if ip != "127.0.0.1":
  send_email("Error - localhost cannot be resolved to 127.0.0.1")

if disk_percent_free < 20:
  send_email("Error - Available disk space is less than 20%")

if memory_usage.free/1000000 < 500:
  send_email("Error - Available memory is less than 500MB")

if cpu_percent > 80:
  send_email("Error - CPU usage is over 80%")

