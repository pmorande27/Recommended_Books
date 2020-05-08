class Book(object):
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __eq__(self, obj):
        return isinstance(obj, Book) and obj.name == self.name

    def __hash__(self):
        return hash(('title', self.name,
                     'author_name', self.author, 'ISBN', self.isbn))

    def toString(self):
        return "the book " + self.name + " was written by: " + self.author + " and Has a ISBN number of:" + self.isbn

    def formatUpload(self):
        return self.name + "," + self.author + "," + self.isbn