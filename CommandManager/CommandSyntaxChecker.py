class CommandSyntaxChecker:

    __supportedKeyWords = ["--price-db","--file","-f","--sort","-s",
                           "bal","balance","register","reg","print"]

    __commandFlagsMap = {
        "bal": __supportedKeyWords[3:5],
        "balance": __supportedKeyWords[3:5],
        "reg": __supportedKeyWords[3:5],
        "register": __supportedKeyWords[3:5],
        "print": __supportedKeyWords[3:5]
    }

    def __init__(self,command):
        pass

    @classmethod
    def syntaxCheck(cls,command):

        commands = []
        arguments = []

        if command[0] not in cls.__supportedKeyWords: return False

        for c in command:
            if c not in cls.__supportedKeyWords:
                arguments.append(c)
            else:
                commands.append(c)

        return commands,arguments


