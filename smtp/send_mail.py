import smtplib
import pandas as pd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

address = open("contact/address.txt", "r")
password = open("contact/password.txt", "r")

MY_ADDRESS = address.read()
PASSWORD = password.read()


def create_html_gmail_message(message):
    return "<html>" + message + """\
        <br><br>
        <div id="m_-651538905657960953Signature">
            <div id="m_-651538905657960953divtagdefaultwrapper" dir="ltr"
                style="font-size:12pt;color:#000000;font-family:Calibri,Helvetica,sans-serif">
                <p style="margin-top:0px;margin-bottom:0px;margin-top:0;margin-bottom:0"><span
                        id="m_-651538905657960953ms-rterangepaste-start"></span></p>
                <div
                    style="margin-bottom:30px;border:1px solid rgb(153,153,153);border-radius:10px;padding:20px;margin-right:20px;background-color:transparent;font-family:Trebuchet MS,Calibri,Arial,sans-serif;font-size:13px">
                    <div>
                        <div><img alt="horizontal bar" id="m_-651538905657960953OWAPstImg423488" style="max-width:100%"
                                src="http://www.bad-kan.com/images/horizontal_bar.png" data-image-whitelisted="" class="CToWUd">
                            <div class="yj6qo ajU">
                                <div id=":1w" class="ajR" role="button" tabindex="0" aria-label="Hide expanded content"
                                    aria-expanded="true" data-tooltip="Hide expanded content"><img class="ajT"
                                        src="//ssl.gstatic.com/ui/v1/icons/mail/images/cleardot.gif"></div>
                            </div><span class="HOEnZb adL">
                                <font color="#888888">
                                    <h3 style="margin-bottom:0px">Support Bad-kan</h3>
                                    <span>Badkan, Team support<br>
                                    </span><span><img alt="Badkan" id="m_-651538905657960953OWAPstImg607439"
                                            src="http://www.bad-kan.com/logo/favicon.png" data-image-whitelisted=""
                                            class="CToWUd" width="70" height="70"><br>
                                    </span><span>+972 53 708 4835<br>
                                    </span><a href="http://www.bad-kan.com" target="_blank"
                                        data-saferedirecturl="https://www.google.com/url?q=http://www.bad-kan.com&amp;source=gmail&amp;ust=1571834661701000&amp;usg=AFQjCNH6Cxsw5U0gfNYKzd-ID33gW6tbhw">http://www.bad-kan.com</a>
                                </font>
                            </span>
                        </div>
                        <div class="adL">
                        </div>
                    </div>
                    <div class="adL">
                    </div>
                </div>
                <div class="adL">
                    <span id="m_-651538905657960953ms-rterangepaste-end"></span><br>
                    <p style="margin-top:0px;margin-bottom:0px"></p>
                </div>
            </div>
            <div class="adL">
            </div>
        </div>
        </html>
        """


def send_mail(subject, message, client_mail):
    print(MY_ADDRESS)
    print(PASSWORD)
    print(client_mail)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = MY_ADDRESS
    msg['To'] = client_mail
    msg.attach(MIMEText(create_html_gmail_message(message), 'html'))
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    s.sendmail(MY_ADDRESS, client_mail, msg.as_string())
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
        message += "<h1>Bonjour " + row["Title"] + ", </h1>"
        if row["University or website"] == "School":
            f = open("messages/french_school.txt", "r")
            message += f.read()
        elif row["University or website"] == "website e-learning":
            f = open("messages/french_learning.txt", "r")
            message += f.read()
    elif row["Nationality"] == "American":
        message += "<h1>Hello " + row["Title"] + ",  </h1>"
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
