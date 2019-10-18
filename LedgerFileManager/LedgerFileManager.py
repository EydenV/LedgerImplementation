from .LedgerFileParser import LedgerFileParser
import os
class LedgerFileManager:

    def __init__(self,arguments):
        self.arguments =    arguments
        self.books =        []
        self.filePaths =    []
        self.bookParsed =   {}

    def booksExists(self):

        bookNames = []

        for book in self.arguments:
            if len(book) > 1:
                bookNames.append(book)

        result = self.checkBooks(bookNames)

        if type(result) == "str": return False
        else:
            self.books = bookNames
            return True

    def checkBooks(self,bookNames):
        actualPath = os.getcwd()

        for book in bookNames:
            if not os.path.isfile(actualPath + "/" + book):
                return book

        return True

    def getFilePaths(self):
        for book in self.books:
            self.filePaths.append(os.getcwd() + "/" + book)

        return self.filePaths

    def parseAllBooks(self):

        self.getFilePaths()
        fileParser = LedgerFileParser()

        for i,file in enumerate(self.filePaths):
            self.bookParsed[self.books[i]] = fileParser.parseBook(file)

        print(self.bookParsed)

