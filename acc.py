class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance  = self.balance-amount

    def deposit(self,amount):
        self.balance = self.balance+amount   
    
    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    type = "checking"
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath) ## inheritence class ##
        self.fee = fee
    def transfer(self,amount):
        self.balance = self.balance-amount-self.fee

jack_checking = Checking("jack.txt",1)
jack_checking.deposit(100)
print(jack_checking.balance)
jack_checking.transfer(50)
print(jack_checking.balance)
jack_checking.commit()
print(jack_checking.type)

joe_checking = Checking("joe.txt",1)
joe_checking.deposit(100)
print(joe_checking.balance)
joe_checking.transfer(50)
print(joe_checking.balance)
joe_checking.commit()
print(joe_checking.type)