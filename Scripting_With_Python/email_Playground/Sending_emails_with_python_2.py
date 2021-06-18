# Sending emails with Python.
# Python has the inbuilt email modules.

# We can also send content using the HTML document, where we will be using the Template method in the
# String class and we can dynamically include the name while sending the emails using the index.html
# page as shown below.

# We have another module to read this html files is by using pathlib module and function Path

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# For email we need to address from address, Subject and content
# First we need to create email object

email = EmailMessage()
email['from'] = 'Manish AWS Freelancer'
email['to'] = 'manishawsfreelancer@gmail.com'
email['subject'] = 'This email is testing as a python learning course'

html = Template(Path('index.html').read_text())

# In the content we are going to write the actual message.

email.set_content(html.substitute(name='Baahubali'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('manishawsdevops@gmail.com', 'Mummydaddy@1994')
    smtp.send_message(email)
    print('All Good')
