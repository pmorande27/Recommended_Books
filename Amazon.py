import urllib.request
from Book import Book
from bs4 import BeautifulSoup


def load_amazon():
    URL = "https://www.amazon.es/gp/bestsellers/books"
    data = urllib.request.urlopen(URL).read().decode()
    soup = BeautifulSoup(data, "html.parser")
    links = soup('a')
    result = []
    for link in links:
        a = (str(link.get('href')))
        if "psc=1" in a:
            headers = headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
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


