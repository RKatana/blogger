from .import mail
from flask_mail import Message
from flask import render_template

def mail_message(subject,template,to,**kwargs):
    sender_email='roduor52@gmail.com'
    email=Message(subject,sender=sender_email,recipients=[to])
    email.body=render_template(template + '.txt',**kwargs)