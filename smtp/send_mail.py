import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

address = open("contact/address.txt", "r")
password = open("contact/password.txt", "r")

MY_ADDRESS = address.read()
PASSWORD = password.read()

def create_html_message(title):
    f = open("messages/message_gmail_french.html", "r")
    message = f.read()
    message = message.replace("$@$SWITCH ME$@$", title, 1)
    return message

def send_mail(subject, title, client_mail):
    print(MY_ADDRESS)
    print(PASSWORD)
    print(client_mail)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = MY_ADDRESS
    msg['To'] = client_mail
    msg.attach(MIMEText(create_html_message(title), 'html'))
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
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
    subject = ""
    if row["Nationality"] == "French":
        subject = "Badkan : le nouveau logiciel étudiant - professeur"
        
    elif row["Nationality"] == "American":
        subject = "Badkan : the new software student - instructor"
    return subject


def read_csv(filename):
    first_line = get_lines(filename)
    table = pd.read_csv(filename, skiprows=range(1, first_line))
    for index, row in table.iterrows():
        subject = prepare_mail(row)
        client_mail = row["Email"]
        if "@" in client_mail:
            send_mail(subject, row["Title"], client_mail)


read_csv("emails.csv")
