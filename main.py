import smtplib

# Creates  SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# My email
sender_email_id = 'jasoncee017@gmail.com'
# Receiver email
receiver_email_id = ['brentleejohnson73@gmail.com', 'jaydenmay040@gmail.com', 'jasoncee017@gmail.com']
# Password
password = input('Please enter email password: ')
# Security purposes
s.starttls()
# Message to be sent
s.login(sender_email_id, password)
# Message
message = "Hi\n"
message = message + "Python email tester, Thank You"
# Sending mail
s.sendmail(sender_email_id, receiver_email_id, message)
# Terminating session
s.quit()
