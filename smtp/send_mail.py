import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

address = open("contact/address.txt", "r")
password = open("contact/password.txt", "r")

MY_ADDRESS = address.read()
PASSWORD = password.read()


def send_mail(subject, message, client_mail):
    # TODO: Check why the email is sent twice.
    print(MY_ADDRESS)
    print(PASSWORD)
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = client_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()


def get_lines(filename):
    table = pd.read_csv(filename)
    first_line = 0
    for index, row in table.iterrows():
        if row["Name"] == "$@$":
            first_line = index + 2
    return first_line


def prepare_mail(row):
    subject = message = ""
    if row["Nationality"] == "French":
        subject = "Badkan: le nouveau correcteur"
        message += "Bonjour " + row["Title"] + ", \n"
        if row["University or website"] == "School":
            f = open("messages/french_school.txt", "r")
            message += f.read()
        elif row["University or website"] == "website e-learning":
            f = open("messages/french_learning.txt", "r")
            message += f.read()
    elif row["Nationality"] == "American":
        message += "Hello " + row["Title"] + ", \n"
        subject = "Badkan: the new corrector"
        if row["University or website"] == "School":
            f = open("messages/american_school.txt", "r")
            message += f.read()
        elif row["University or website"] == "website e-learning":
            f = open("messages/american_learning.txt", "r")
            message += f.read()
    return subject, message


def read_csv(filename):
    first_line = get_lines(filename)
    table = pd.read_csv(filename, skiprows=range(1, first_line))
    for index, row in table.iterrows():
        subject, message = prepare_mail(row)
        client_mail = row["Email"]
        if "@" in client_mail:
            send_mail(subject, message, client_mail)


read_csv("emails.csv")
