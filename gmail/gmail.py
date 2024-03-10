import smtplib

email = "<insert gmail>"
receiver_email = "<insert gmail>"
subject = "<insert subject>"
message = "<insert message>"

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email, "<insert app password>")

server.sendmail (email, receiver_email, text)

print("Email has been sent to " + receiver_email)