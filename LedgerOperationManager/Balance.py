from .IOperations import IOperations

class Balance(IOperations):
    def __init__(self,bookParsed):
        self.bookParsed = bookParsed
        self.accounts = []
        pass

    def calculate(self,books):

        if "prices_db" in books.keys():
            del books['prices_db']

        books = self.cleanPrices(books)

        printable = ""
        sumas = []
        suma = 0
        sumaTotal = 0
        sumaBTC = ""


        for k,v in books.items():
            printable += "\t"
            for item in v:
                if("BTC" in str(item.amount) and "BTC" not in str(item.amountSecondary)):
                    suma+=float(item.amountSecondary)
                elif "BTC" not in str(item.amount) and "BTC" in str(item.amountSecondary):
                    suma+=float(item.amount)
                else:
                    suma += float(item.amount)
                    suma += float(item.amountSecondary)

            sumaTotal = suma
            printable += str(suma)
            if k in self.accounts:
                printable += "\t" + k
            else:
                printable += "\t " + k
            printable += "\n"
            suma = 0

        printable += "--------------------"
        printable += "\n"
        printable += "\t" + str(sumaTotal)
        print(printable)

        return printable

    #Return the Specific transactions to calculate
    def getSpecificInfo(self,toExecute,keys):
        accounts, files = self.getFilesAccount(toExecute,keys)
        transactions = []

        if "".join(files) == "all" or "".join(accounts) == "all":
            files = []
            accounts = []


        self.accounts = accounts

        #General operation
        if len(accounts) == 0 and len(files) == 0:
            self.calculate(self.bookParsed)

        #Files only operation
        elif len(accounts) == 0 and len(files) > 0:
            books = self.getFilesOnly(files)
            self.calculate(books)

        #Accounts only operation
        elif len(accounts) > 0 and len(files) == 0:
            books = self.getAccountsOnly(accounts)
            self.calculate(books)

        #Accounts and Files operation
        elif len(accounts) > 0 and len(files) > 0:
            books = self.getAccountsOnly(accounts)
            books.update(self.getFilesOnly(files))
            self.calculate(books)


    def getFilesAccount(self,toExecute,keys):
        accounts = []
        files = []

        for v in toExecute.values():
            for item in v:
                if item in keys:
                    files.append(item)
                else:
                    accounts.append(item)
        return accounts,files


    def getFilesOnly(self,files):
        books = {}
        for k, v in self.bookParsed.items():
            if k in files:
                books[k] = v
        return books

    def getAccountsOnly(self,accounts):
        books = {}
        transactions=[]
        aux = []
        current = ""

        del self.bookParsed["prices_db"]

        for k,v in self.bookParsed.items():
            for transaction in v:
                transactions.append(transaction)

        for a in accounts:
            for t in transactions:
                if t.haveAccount(a):
                    aux.append(t)
                    current = a
            if current != "":
                books[current] = aux
                aux = []

        return books

    def cleanPrices(self,books):
        for k,v in books.items():
            for item in v:
                index = v.index(item)
                if "$" in str(item.amount):
                    item.amount = float(item.amount.replace('$',''))
                if "$" in str(item.amountSecondary):
                    item.amountSecondary = float(item.amountSecondary.replace('$',''))

                v[index] = item
                books[k] = v

        return books


    def addBTC(self,number1,number2):
        number1 = float(number1.replace('BTC',''))
        number2 = float(number2.replace('BTC', ''))
        number3 = str(number1+number2) + 'BTC'
        return number3




