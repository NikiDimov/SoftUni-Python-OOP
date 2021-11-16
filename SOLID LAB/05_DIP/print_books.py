class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    @staticmethod
    def format(book: Book):
        return book.content


class Printer:
    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book
