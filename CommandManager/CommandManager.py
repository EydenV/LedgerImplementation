from .CommandSyntaxChecker import CommandSyntaxChecker
import sys
from collections import OrderedDict
class CommandManager:

    def __init__(self,command):
        self.command = command

    def getInfo(self):
        if type(CommandSyntaxChecker.syntaxCheck(self.command)).__name__ == "tuple" :
            return CommandSyntaxChecker.syntaxCheck(self.command)
        else:
            sys.exit("Error: Unrecognized command '" + CommandSyntaxChecker.syntaxCheck(self.command) + "'")

    def generateOperations(self,commands = None, arguments = None):
        operation = []
        operations = []

        if commands == None or arguments == None:
            commands,arguments = self.getInfo()

        arguments = list(OrderedDict.fromkeys(arguments))
        oneCommmand = False

        for command in commands:
            operation.append(command)
            for argument in arguments:
                if command in ["balance","bal","register","reg","print"]:
                    oneCommmand = True
                    operation.append(argument)
                else:
                    operation.append(argument)
                    arguments.remove(argument)
                    break


            operations.append(operation)
            operation = []

            if oneCommmand:
                break

        return operations



