class Bank:
    def __init__(self,balance):
        self._balance = balance
    def get_balance(self):
        return self._balance
b = Bank(5000)
print(b.get_balance())