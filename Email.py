#! /Users/keithmathe/opt/anaconda3/envs/gmailsend/bin/python
# The Email class represents an email, to be used by the Mailbox

class Email(object):


    def __init__(self):
        self.addresses = []
        self.subject = ''
        self.body = ''
    

    def set_addresses(self, from_addr, addresses):
        self.from_addr = from_addr
        self.addresses = addresses
        # TODO: Check for valid email address
    
    
    def set_subject(self, subject):
        self.subject = f"Subject: {subject}\n"


    def set_body(self, body):
        self.body = body

    def get_content(self):
        return self.subject + self.body

    def __str__(self):
        return f"""
From: {self.from_addr}
To: {", ".join(self.addresses)}
{self.subject}
{self.body}"""

    
    