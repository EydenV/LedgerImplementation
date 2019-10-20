import sys
from CommandManager.CommandManager import CommandManager
from LedgerFileManager.LedgerFileManager import LedgerFileManager
from LedgerOperationManager.LedgerOperationManager import LedgerOperationManager

def main():

    commandManager = CommandManager(sys.argv[1::])
    commands,arguments = commandManager.getInfo()

    fileManager = LedgerFileManager(arguments)

    if fileManager.booksExists():

        fileManager.parseAllBooks()

        operationManager = LedgerOperationManager(fileManager.bookParsed)

        operationManager.executeOperations(
            commandManager.generateOperations(commands,arguments),fileManager.bookParsed.keys())




if __name__ == "__main__":
    main()