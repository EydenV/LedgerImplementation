import os
import re
from . import ledgerparse

PRICE_DB_REGEX = re.compile('^[A-Z] \d{4}\/(0[1-9]|1[0-2])\/([0-2]\d|3[0-1]) ([01]\d|2[0-4]):[0-5]\d:[0-5]\d [A-Z]{2} (\$|BTC)\d+.\d+$')

class LedgerFileParser:
    def __init__(self):
        pass


    def getContent(self,filePath):
        f = open(filePath)
        contentString = f.read()
        f.close()

        return contentString

    def parseBook(self,filePath):

        contentString = self.getContent(filePath)

        isTransaction = self.checkTransaction(contentString)

        if isTransaction == "include":
            return "include"
        elif isTransaction == "price":
            journal = ledgerparse.string_to_non_transactions(contentString)
        else:
            journal = ledgerparse.string_to_ledger(contentString)

        return journal

    def checkTransaction(self,contentString):
        content = contentString.split("\n")

        for line in content:
            if "include" in line:
                return "include"
            elif PRICE_DB_REGEX.findall(line):
                return "price"

        return "transaction"


