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

    def __str__(self):
        return "THE BOOK " + self.name + " WAS WRITTEN BY: " + self.author + " AND HAS A ISBN NUMBER OF: " + self.isbn

    def formatUpload(self):
        return self.name + "," + self.author + "," + self.isbn
