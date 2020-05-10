import urllib.request
from bs4 import BeautifulSoup
from Book import Book


def isBookLink(link):
    reference = (str(link.get('href')))
    return ("/book/show/" in reference) & ("/popular_by_date/" not in reference)


def getReference(link):
    return str(link.get('href'))


def load_GoodReads():
    print("Loading GoodReads")
    URL = "https://www.goodreads.com/book/popular_by_date/2020"
    data = urllib.request.urlopen(URL).read().decode()
    soup = BeautifulSoup(data, "html.parser")
    links = soup('a')
    links = list(filter(isBookLink, links))
    references = list(map(getReference, links))
    references = list(set(references))
    result = []
    for reference in references:
        new_link = "https://www.goodreads.com" + reference
        request = urllib.request.urlopen(new_link).read().decode()
        data = BeautifulSoup(request, "html.parser")
        title = str(data('title'))
        content = title.split(" by ")
        name = content[0].replace("[<title>", "").strip()
        author = content[1].replace("</title>]", "").strip()
        split_link = new_link.split("/")
        isbn = split_link[len(split_link) - 1].split("-")[0].strip()
        result.append(Book(name, [author], isbn))

    return result


