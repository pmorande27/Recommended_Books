class Book(object):
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

    def __eq__(self, obj):
        return isinstance(obj, Book) and obj.name == self.name

    def __hash__(self):
        return hash((
                     'isbn', self.isbn))

    def __str__(self):
        return "THE BOOK " + self.name + " WAS WRITTEN BY: " + self.print_author() + " AND HAS A ISBN NUMBER OF: " + self.isbn

    def print_author(self):
        result = ""
        for i in self.author:
            result+= i+", "
        result += "\b\b"
        return result

    def formatUpload(self):
        return self.name + "," + self.author_upload() + "," + self.isbn

    def author_upload(self):
        result = ""
        for i in range(len(self.author)):
            if i == len(self.author)-1:
                result += self.author[i]
            else:
                result += self.author[i]+"&"
        return result
