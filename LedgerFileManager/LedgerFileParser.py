import os
import re
from . import ledgerparse
from .Ledger import LedgerTransaction

PRICE_DB_REGEX = re.compile('^[A-Z] \d{4}\/(0[1-9]|1[0-2])\/([0-2]\d|3[0-1]) ([01]\d|2[0-4]):[0-5]\d:[0-5]\d [A-Z]{2} (\$|BTC)\d+.\d+$')

class LedgerFileParser:
    def __init__(self):
        pass

    def getTransaction(self,contentString):

        files = contentString.splitlines(0)

        transactions = []
        transaction = []
        ledgerTransactions = []

        for file in files:
            if file == '' or ";" in file:
                files.remove(file)

        for i,f in enumerate(files,1):
            transaction.append(f)
            if i%3 == 0:
                transactions.append(transaction)
                transaction = []

        for t in transactions:
            ledgerTransactions.append(
                LedgerTransaction(t)
            )

        return ledgerTransactions

    def getContent(self,filePath):
        f = open(filePath)
        contentString = f.read()
        f.close()
        return contentString

    def parseBook(self,filePath):

        count = 0

        contentString = self.getContent(filePath)

        isTransaction = self.checkTransaction(contentString)

        if isTransaction == "include":
            return "include"
        elif isTransaction == "price":
            journal = ledgerparse.string_to_non_transactions(contentString)
        else:

            journal = self.getTransaction(contentString)

        return journal

    def checkTransaction(self,contentString):
        content = contentString.split("\n")

        for line in content:
            if "include" in line:
                return "include"
            elif PRICE_DB_REGEX.findall(line):
                return "price"

        return "transaction"


