import sys
from CommandManager.CommandManager import CommandManager
from LedgerFileManager.LedgerFileManager import LedgerFileManager
from LedgerOperationManager.LedgerOperationManager import LedgerOperationManager

def main():

    commandManager = CommandManager(sys.argv[1::])
    commands,arguments = commandManager.getInfo()

    fileManager = LedgerFileManager(arguments)

    if fileManager.booksExists():
        #Hacer lo siguiente en el parseo
        fileManager.parseAllBooks()

        operationManager = LedgerOperationManager(commandManager.generateOperations(commands,arguments))






if __name__ == "__main__":
    main()