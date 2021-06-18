# Sending emails with Python.
# Python has the inbuilt email modules.

import smtplib
from email.message import EmailMessage

# For email we need to address from address, Subject and content
# First we need to create email object

email = EmailMessage()
email['from'] = 'Manish AWS Freelancer'
email['to'] = 'manishawsfreelancer@gmail.com'
email['subject'] = 'This email is testing as a python learning course'

# In the content we are going to write the actual message.

email.set_content(
    'Heyyyyy You have received this as a part of python learning')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('manishawsdevops@gmail.com', 'Mummydaddy@1994')
    smtp.send_message(email)
    print('All Good')
