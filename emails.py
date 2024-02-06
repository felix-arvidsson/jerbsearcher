import smtplib
from email.mime.text import MIMEText

import config

class EmailSender:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.sender = config.sender
        self.recipients = config.recipients
        self.password = config.password

    def send_email(self):
        msg = MIMEText(self.body, 'html')
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
           smtp_server.login(self.sender, self.password)
           smtp_server.sendmail(self.sender, self.recipients, msg.as_string())
        print("Email sent!")

