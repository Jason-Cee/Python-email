import smtplib

# Creates  SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# My email
sender_email_id = 'jasoncee017@gmail.com'
# Receiver email
receiver_email_id = 'brentleejohnson73@gmail.com'
# Password
password = input('Enter senders email password: ')
# Security purposes
s.starttls()
# Message to be sent
s.login(sender_email_id, password)
# Message
message = "Hi, How are you? I am find thanks\n"
message = message + "How was your task yesterday?"
# Sending mail
s.sendmail(sender_email_id, receiver_email_id, message)
# Terminating session
s.quit()
