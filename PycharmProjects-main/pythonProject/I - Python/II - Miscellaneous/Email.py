import smtplib

sender = "dacanaykevin8@gmail.com"
reciever = "kevin.dacanay27@gmail.com"
password = "brian1227"
subject = "I - Python Email Test"
body = "Testing. Email sending program ! Hello Email!!!"

# header:
message = f"""From: Kevin{sender},
To: {reciever}
Subject: {subject}
{body}

"""

# server object:
server = smtplib.SMTP("smtp.gmail.com", 587)                              # 587 = default mail submission port
server.starttls()

try:
    # log in:
    server.login(sender,password)
    print("Logged in...")

    # send email:
    server.sendmail(sender, reciever, message)
    print("Email sent!")
     
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
