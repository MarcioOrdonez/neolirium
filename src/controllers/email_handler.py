import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys, os

class email_handler():

    def __init__(self, user_list, latest_post):
        self.user_list = user_list
        self.latest_post = latest_post
        self.password = os.getenv('EMAIL_PASSWORD') or 'senha'
        self.login = os.getenv('EMAIL_LOGIN') or 'email'
        self.sender = os.getenv('SENDER') or 'naoresponda@neolirium.com'


    def message(self):
        mail_content = 'Confira a ultima noticia postada em '+ os.getenv('HOST')+'/post/'+str(self.latest_post.id)
        message = MIMEText(mail_content)
        message['From'] = self.sender
        # message['To'] = self.email_list
        message['Subject'] = self.latest_post.title
        # message.attach(MIMEText(mail_content, 'plain'))
        self.message = message

    def getEmails(self):
        self.email_list = []
        for user in self.user_list:
            if not user.admin:
                self.email_list.append(user.email)
        return self.email_list

    def session(self):
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(self.login, self.password)
        text = self.message.as_string()
        session.sendmail(self.sender, self.email_list, text)
        session.quit()

    def send(self):
        if self.getEmails() == []:
            return
        self.message()
        self.session()