class LedgerTransaction():
    def __init__(self,info):
        self.info = info
        self.date = ""
        self.issue = ""
        self.account = ""
        self.amount = ""
        self.accountSecondary = ""
        self.amountSecondary = ""
        self.setInfo()

    def setInfo(self):
        for i,line in enumerate(self.info):
            if i == 0:
                self.date = line.split(" ")[0]
                self.issue = " ".join(line.split(" ")[1:])
            elif i == 1:
                l = list(line)
                l[0] = ""
                line = ''.join(l)

                line = " ".join("".join("".join(line.split(" ")).split("\t")).split(" "))

                for i,l in enumerate(line):
                    if l == "$"  or l.isdigit() or l == "-":
                        aux = list(line)
                        aux[i-1] += " "
                        line = ''.join(aux)

                flag = False
                for i,l in enumerate(line):
                    if l == "-" or l == "$":
                        flag = True
                    if l == " " and flag:
                        aux = list(line)
                        aux[i] = ""
                        line = ''.join(aux)

                line = line.split(" ")
                line = [l for l in line if l != '']

                line = " ".join(line)

                self.account = line.split(" ")[0]
                self.amount = line.split(" ")[1]

            elif i == 2:
                l = list(line)
                l[0] = ""
                line = ''.join(l)

                line = " ".join("".join("".join(line.split(" ")).split("\t")).split(" "))

                if not self.num_there(line):
                    self.accountSecondary = line
                    self.amountSecondary = "0"
                else:
                    for i, l in enumerate(line):
                        if l == "$" or l.isdigit() or l == "-":
                            aux = list(line)
                            aux[i - 1] += " "
                            line = ''.join(aux)

                    flag = False
                    for i, l in enumerate(line):
                        if l == "-":
                            flag = True
                        if l == " " and flag:
                            aux = list(line)
                            aux[i] = ""
                            line = ''.join(aux)

                    line = line.split(" ")
                    line = [l for l in line if l != '']

                    line = " ".join(line)
                    self.accountSecondary = line.split(" ")[0]
                    self.amountSecondary = line.split(" ")[-1]
        self.accounts = [self.account, self.accountSecondary]

    def num_there(self,s):
        return any(i.isdigit() for i in s)

    def haveAccount(self,account):
        if account in self.account or account in self.accountSecondary:
            return True
        return False





