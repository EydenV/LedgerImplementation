from abc import ABCMeta, abstractmethod

class IOperations():
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self,books):
        raise NotImplementedError

    @abstractmethod
    def getSpecificInfo(self,toExecute,keys):
        raise NotImplementedError

    @abstractmethod
    def getFilesAccount(self,toExecute,keys):
        raise NotImplementedError

