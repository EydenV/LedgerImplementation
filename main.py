import sys
from CommandManager.CommandManager import CommandManager
from LedgerFileManager.LedgerFileManager import LedgerFileManager

def main():

    commandManager = CommandManager(sys.argv[1::])
    commands,arguments = commandManager.getInfo()

    fileManager = LedgerFileManager(arguments)

    if fileManager.booksExists():
        #Hacer lo siguiente en el parseo
        fileManager.parseAllBooks()



if __name__ == "__main__":
    main()