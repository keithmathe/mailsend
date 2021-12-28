#! /Users/keithmathe/opt/anaconda3/envs/gmailsend/bin/python
# Simple Gmail client for sending mail from the command line

import Mail
import Email
import fileinput

#TODO: Handle exceptions more responsibly

def send_mail(username, mailbox):
    """Main function responsible for generating email and sending it"""

    # generate email
    email = Email.Email()

    # get to addresses
    print("")
    addrs = input("Enter recepients' addresses separated by a space character:\n> ")
    email.set_addresses(username, addrs.split())

    # get email subject
    print("")
    sub = input("Subject:\n> ")
    email.set_subject(sub)

    # get email body
    print("")
    print("Type in email body then hit Control-C:")
    body = ""
    try:
        for line in fileinput.input(encoding="utf-8"):
            body += line
    except KeyboardInterrupt:
        email.set_body(body)

    # attempt to send email
    print("")
    print("Confirm email:")
    print(email)
    confirm = input("Proceed to send [y/n]?: ")
    if confirm == 'y' or 'Y':
        mailbox.send(email)
        
    # send more mail or quit? 
    try:
        input("Hit any key to send more mail or Control-C to quit")
    except KeyboardInterrupt:
        print("")
        mailbox.logout()
        exit(0)
    else:
        send_mail(username, mailbox)

# get user login credentials
print("")
username = input("Email:\n> ")
password = input("Password:\n> ")
print("")

# login to mailbox
mailbox = Mail.Mailbox('smtp.gmail.com', 587)
mailbox.login(username, password)

# generate and send email
send_mail(username, mailbox)

