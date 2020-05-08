from Recommended_Books import Library
import smtplib
from email.mime.text import MIMEText


def main():
    lib = Library("https://www.casadellibro.com/libros-recomendados")

    lib.send_email()



main()
