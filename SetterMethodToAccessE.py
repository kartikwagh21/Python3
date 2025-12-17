class Bank:
    def __init__(self,balance):
        self._balance = balance
    def get_balance(self):
        return self._balance
    def set_balance(self,amount):
        if amount > 0:
            self._balance = amount
        else:
            print("Invalid Amount")
b = Bank(5000)
b.set_balance(9000)
print(b.get_balance())