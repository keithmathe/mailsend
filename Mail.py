#! /Users/keithmathe/opt/anaconda3/envs/gmailsend/bin/python
# The Mailbox class represents a Mailbox, that manages the Email object

import smtplib

class Mailbox(object):
    

    def __init__(self, smtp_server, port, tls='on'):
        self.smtp_server = smtp_server
        self.port = port
        self.tls = tls
        
    
    def login(self, username, password):
        self.username = username
        print(f"***Connecting to server [{self.smtp_server}]...")
        self.mail = smtplib.SMTP(self.smtp_server, self.port)
        print(self.mail.ehlo())
        if self.port != 465 and self.tls == 'on':
            print(self.mail.starttls())
        print(self.mail.login(username, password))
        print("***Log in successful")


    def send(self, email):
        resp = self.mail.sendmail(self.username, email.addresses, email.get_content())
        #TODO: Use logging instead of print statements
        print("Sending email...")
        for key in resp:
            print(f"Error sending email to {key}")
            print("\tError Code:", resp[key[0]] )
            print("\tDetails:", resp[key][1])
            print("\tMake sure you're connected to the internet and verify email addresses")
        sent = set(email.addresses) - resp.keys()
        if sent:
            print(f"Sent to [{', '.join(email.addresses)}]")


    def logout(self):
        print(self.mail.quit())