"""
utils/email.py – Validazione email, invio SMTP base, template.
"""
import re
import smtplib
from email.mime.text import MIMEText

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

def is_valid_email(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None

def send_email(to: str, subject: str, body: str, from_addr: str, smtp_server: str, smtp_user: str, smtp_pass: str):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to

    with smtplib.SMTP_SSL(smtp_server) as server:
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, [to], msg.as_string())
