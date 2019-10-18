import os
import re
from . import ledgerparse

class LedgerFileParser:
    def __init__(self):
        pass

    def parseBook(self,filePath):
        f = open(filePath)
        contentString = f.read()
        f.close()

        self.checkTransaction(contentString)

        journal = ledgerparse.string_to_non_transactions(contentString)

        return journal

    #Comprobar si el string tiene o no transacciones.
    def checkTransaction(self,contentString):

        pass


