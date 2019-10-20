import sys
import os

class LedgerOperationManager:
    def __init__(self,bookParsed):
        self.bookParsed =            bookParsed
        self.cleanOperations =      []
        self.sort =                 False

    def executeOperations(self,operations,files):
        self.cleanBookDict(operations,files)

        operation = self.cleanOperations[0]
        print(operation)


    def cleanBookDict(self,operations,files):
        for op in operations:
            if len(op) > 1:
                if op[1] not in files and ".ledger" not in op[1]: self.cleanOperations.append(op)
            else:
                self.cleanOperations.append(op)

        self.cleanKeys()
        self.cleanOperations = self.cleanOperations[0]

    def checkOperation(self):
        pass

    def sort(self,argument,transactions):
        pass

    def cleanKeys(self):
        for key in self.bookParsed.keys():
            if ".ledger" in key:
                new_key = key.split('.')[0]
                self.bookParsed[new_key] = self.bookParsed.pop(key)