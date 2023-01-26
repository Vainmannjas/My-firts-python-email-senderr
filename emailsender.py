from email.message import EmailMessage
import ssl 
import smtplib

email_sender = 'myemail'
email_password = 'mypassword'
email_receiver = 'first email', 'second'

subject = "it's my first thing on Python. I still can't choose what's better for me Python or Javascript. I've been practicing on Javascript for a month(6 month ago) and I've got results but I don't think what I like it. Problem is that's many things what I should include in there and It's king of borring and annoying. I think I like Python more."

body = """
I want to be python backend web developer. I will put all my results in GitHub. I'm talking in English good but I'm still learning. 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())