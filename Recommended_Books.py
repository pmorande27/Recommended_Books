import smtplib
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
import urllib.request

from Book import Book
import os
import getpass


def CreateBook(title):
    list_of_elements = title.split("|")
    name = list_of_elements[0].replace("[<title>", "").strip()
    author = list_of_elements[1].strip()
    ISBN = list_of_elements[2].replace("</title>]", "").replace("Comprar libro ", "").strip()
    return Book(name, author, ISBN)


class Library(object):
    def __init__(self, URL):
        self.URL = URL
        self.recommended_books = []
        self.__preLoadedBooks()

    def load(self):
        data = urllib.request.urlopen(self.URL).read().decode()
        soup = BeautifulSoup(data)
        links = soup('a')
        result = []
        for link in links:
            a = (str(link.get('href')))
            if ("/libro-" in a) & (not "https://www.casadellibro.com" in a) & (not "/libro-y-pelicula" in a):
                b = "https://www.casadellibro.com" + a
                data = urllib.request.urlopen(b).read().decode()
                soups = BeautifulSoup(data)
                result.append(str(soups('title')))
        count = 0
        for i in result:
            if not i in self.recommended_books:
                count += 1
                self.recommended_books.append(CreateBook(i))
        self.recommended_books = list(set(self.recommended_books))

    def display(self):
        if len(self.recommended_books) == 0:
            print("No books added to the Library")
        else:
            for book in self.recommended_books:
                print(book.toString())

    def getText(self):
        resutl = ""
        if len(self.recommended_books) == 0:
            resutl = "No books added to the Library"
        else:
            for book in self.recommended_books:
                resutl += book.toString() + "\n"
        return resutl

    def save_Books(self):
        textFile = open('recommendedbooks.txt', 'w')
        for b in self.recommended_books:
            textFile.write(b.formatUpload() + "\n")
        textFile.close()

    def send_email(self):
        os.environ['MAIL_PASSWORD'] = 'Elvatera2'

        message = self.getText()
        gmail_user = input("User: ")
        gmail_password = getpass.getpass()
        text_type = 'plain'  # or 'html'
        msg = MIMEText(message, text_type, 'utf-8')
        msg['Subject'] = 'Recommended books'
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()

    def __preLoadedBooks(self):
        textFile = open('recommendedbooks.txt', 'r')
        books = textFile.read().split("\n")
        for b in books:
            content = b.split(",")
            if len(content) == 3:
                self.recommended_books.append(Book(content[0], content[1].strip(), content[2].strip()))
