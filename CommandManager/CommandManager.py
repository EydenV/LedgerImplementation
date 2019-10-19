from .CommandSyntaxChecker import CommandSyntaxChecker

class CommandManager:

    def __init__(self,command):
        self.command = command

    def getInfo(self):
        return CommandSyntaxChecker.syntaxCheck(self.command)

    def generateOperations(self,commands = None, arguments = None):
        operation = []
        operations = []

        if commands == None or arguments == None:
            commands,arguments = self.getInfo()

        for command in commands:
            operation.append(command)
            for argument in arguments:
                if command in ["balance","bal","register","reg","print"]:
                    operation.append(argument)
                else:
                    operation.append(argument)
                    arguments.remove(argument)
                    break

            operations.append(operation)
            operation = []

        return operations



