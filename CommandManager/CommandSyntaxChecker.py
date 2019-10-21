import sys

class CommandSyntaxChecker:

    __supportedKeyWords = ["--price-db","--file","-f","--sort","-s",
                           "bal","balance","register","reg","print"]

    def __init__(self):
        pass


    def syntaxCheck(self,command):

        commands = []
        arguments = []

        if command[0] not in self.__supportedKeyWords: return False

        for c in command:
            if c not in self.__supportedKeyWords:
                arguments.append(c)
            else:
                commands.append(c)


        self.checkFalseFlags(arguments)
        return commands,arguments

    def checkFalseFlags(self,arguments):
        for argument in arguments:
            if "-" in argument:
                sys.exit("Error: Unrecognized flag '" + argument + "'")



