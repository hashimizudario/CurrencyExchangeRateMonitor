import smtplib
from email.mime.text import MIMEText
import argparse
import sys

parser = argparse.ArgumentParser(description='Send currency exchange rates notification.')
parser.add_argument('-r', type=str, help='currency exchange rate')
parser.add_argument('-s', type=str, help='source currency, default CNY', default="CNY")
parser.add_argument('-t', type=str, help='target currency, default CAD', default="CAD")
parser.add_argument('--sender', type=str, help='sender email')
parser.add_argument('--recipient', type=str, help='recipient email')
parser.add_argument('--url', type=str, help='email url')
parser.add_argument('--password', type=str, help='email password')


args = parser.parse_args()
source_currency = args.s
target_currency = args.t
exchange_rate = args.r
sender = args.sender
recipient = args.recipient
url = args.url
password = args.password

msg_str = "Now 1 " + target_currency + " = " + exchange_rate + " "  + source_currency + "!"

msg = MIMEText(msg_str)
msg['Subject'] = source_currency + " to " +target_currency + " Great deal!"
msg['From'] = sender

print("Start sending!")
try:
    s = smtplib.SMTP(url, 587)
    s.set_debuglevel(0)
    s.ehlo()
    s.starttls()
    print("Trying Login!")
    s.ehlo()
    s.login(sender, password)
    print("Done Login!")
    try:
        s.sendmail(sender, recipient, msg.as_string())
    finally:
        s.quit()
except:
    sys.exit( "Mail failed" ) # give an error message