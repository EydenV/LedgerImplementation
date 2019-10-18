from .CommandSyntaxChecker import CommandSyntaxChecker

class CommandManager:

    def __init__(self,command):
        self.command = command

    def getInfo(self):
        return CommandSyntaxChecker.syntaxCheck(self.command)



