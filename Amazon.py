import urllib.request
from Book import Book
from bs4 import BeautifulSoup


def load_amazon():
    print("Loading Amazon")
    URL = "https://www.amazon.es/gp/bestsellers/books"
    data = urllib.request.urlopen(URL).read().decode()
    soup = BeautifulSoup(data, "html.parser")
    links = soup('a')
    result = []
    for link in links:
        a = (str(link.get('href')))
        if "psc=1" in a:
            content = a.split("/")
            t = content[1].split("-")
            title = ""
            for i in t:
                title += i.upper()+" "
            title += "\b"
            author = ["Amazon"]
            splited_content = a.split('/')
            isbn = splited_content[len(splited_content)-1] .split('?')[0]
            result.append(Book(title,author,isbn))

    return result


