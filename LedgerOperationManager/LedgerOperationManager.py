import sys
import os
from .IOperations import IOperations
from .Balance import Balance
from .Print import Print
from .Register import Register

__supportedKeyWords = ["--price-db", "--file", "-f", "--sort", "-s",
                       "bal", "balance", "register", "reg", "print"]

class LedgerOperationManager:
    def __init__(self,bookParsed):
        self.bookParsed =            bookParsed
        self.cleanOperations =      []
        self.sort =                 False

    #Perfoms all the operations in the operations parameter
    def executeOperations(self,operations,files):
        self.cleanBookDict(operations,files)

        if len(self.cleanOperations) > 1:
            self.sort = True
            operation = self.cleanOperations[1]
        else:
            operation = self.cleanOperations[0]


        myObject = None

        if operation[0] in ["bal","balance"]:
            myObject = Balance(self.bookParsed)
        if operation[0] in ["reg", "register"]:
            myObject = Register(self.bookParsed)
        if operation[0] == 'print':
            myObject = Print(self.bookParsed)

        execute = self.prepareToExecute(operation)
        self.executeOperation(execute,myObject)


    #Will execute all the operation for every transaction and will return printable list
    def executeOperation(self,execute,myObject):
        keys = self.bookParsed.keys()
        printable = myObject.getSpecificInfo(execute,keys)

        return printable

    #Will return the sorted transactions given
    def sortTransactions(self,argument,transactions):
        pass

    #clean the operations already performed in the matrix
    def cleanBookDict(self,operations,files):
        for op in operations:
            if len(op) > 1:
                if op[1] not in files and ".ledger" not in op[1]:
                    self.cleanOperations.append(op)
            else:
                self.cleanOperations.append(op)

        self.cleanKeys()

    #delete que .ledger extension from the keys
    def cleanKeys(self):
        for key in self.bookParsed.keys():
            if ".ledger" in key:
                new_key = key.split('.')[0]
                self.bookParsed[new_key] = self.bookParsed.pop(key)

    #Separate the command from the arguments
    def prepareToExecute(self,operation):
        if len(operation) > 1:
            return {operation[0]: operation[1:]}
        else:
            return {operation[0] : "all"}