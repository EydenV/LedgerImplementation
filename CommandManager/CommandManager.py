from .CommandSyntaxChecker import CommandSyntaxChecker

class CommandManager:

    def __init__(self,command):
        self.command = command

    def getInfo(self):
        return CommandSyntaxChecker.syntaxCheck(self.command)

    def generateOperations(self,commands = None, arguments = None):
        operations = []

        if commands == None or arguments == None:
            commands,arguments = self.getInfo()



        return operations



