# mailsend

# Description
Lightweight command line interface for sending email using SMTP. Default configuration is set for Gmail (smtp.gmail.com at port 587). Script provides a minimal interactive interface that logs user in[^1], queries for recipents' addresses, email subject and body before requesting confirmation to send. 

# Usage

## 1. Using Gmail
- Clone repo or download zip and run from driver script from terminal `<_location of cloned files_>/mailsend.py`

## 2. Using another email client
- Clone repo or download zip
- Edit mailsend.py by changing `Mail.Mailbox('smtp.gmail.com', 587)` to `Mail.Mailbox('_your smpt server_', _port number_)`
- Run driver script from terminal `_location of cloned files_/mailsend.py`

# Features to add
- [ ] Highlight text in color
- [ ] Provide detailed error messages and suggest possible solutions
- [ ] Provide CC and BCC options
- [ ] Remember user credentials securely 


 # Licenses
 MIT Licence (see [LICENSE.txt](https://github.com/keithmathe/mailsend/blob/master/LICENSE.txt))
 
 [^1]: For help with Gmail Application Specific Passwords click [here](https://support.google.com/mail/answer/185833?hl=en)
