import smtplib
import random
from email.message import EmailMessage

#Email and app password from google, can change later on for better email address
email = "acmaitest@gmail.com"
password = "qmjf hqql xnww rusu"

#sends verification email and returns the verification code, takes student's username without domain
def send_verification_email(to):
    code = str(random.randint(100000, 999999))
    msg = EmailMessage()
    msg.set_content(f"Your verification code is: {code}")
    msg['Subject'] = "Your Verification Code"
    msg['From'] = email
    msg['To'] = to + "@mst.edu"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()
    return code

if __name__ == "__main__":
    to = input("Enter your MST username: ")
    while len(to) != 6:
        to = input("Enter your MST username (without domain): ")
    code = send_verification_email(to)
    if input("Enter your verification code (check spam folder): ") == code:
        print("Verification successful!")
    else:
        print("Verification failed.")



    


