from .LedgerFileParser import LedgerFileParser
import os
import sys

class LedgerFileManager:

    def __init__(self,arguments):
        self.arguments =        arguments
        self.books =            []
        self.bookParsed =       {}
        self.includeFiles =     []

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

    def getFilePaths(self,files):

        filePaths = []
        for book in files:
            filePaths.append(os.getcwd() + "/" + book)

        return filePaths

    def parse(self,filePaths,fileParser,books):
        for i,file in enumerate(filePaths):
            if os.path.isfile(file):
                self.bookParsed[books[i]] = fileParser.parseBook(file)

    def parseAllBooks(self):

        filePaths = self.getFilePaths(self.books)
        fileParser = LedgerFileParser()

        self.parse(filePaths,fileParser,self.books)

        if "include" in self.bookParsed.values():
            for key, value in self.bookParsed.items():
                if value == "include":
                    self.includeFiles.append(key)

            self.parseIncludeFile()


    def parseIncludeFile(self):

        filePaths = self.getFilePaths(self.includeFiles)
        fileParser = LedgerFileParser()

        fileNames = []

        for f in filePaths:
            content = fileParser.getContent(f).replace("!include","").strip()
            for fileName in content.split("\n"):
                fileNames.append(fileName.strip())


        for f in self.includeFiles:
            del self.bookParsed[f]

        filePaths = self.getFilePaths(fileNames)
        self.parse(filePaths,fileParser,fileNames)