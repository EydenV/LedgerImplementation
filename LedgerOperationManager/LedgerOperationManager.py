class LedgerOperationManager:
    def __init__(self,operations):
        self.operations =     operations


    def executeOperations(self):
        for operation in self.operations:
            command = self.checkOperation(operation)

    def checkOperation(self,operation):
        pass