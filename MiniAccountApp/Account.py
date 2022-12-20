from MiniAccountApp.MyCustomException import MyCustomException


class Account:
    balance = 0

    def __init__(self, name, pin):
        self.name = name
        self.pin = name


    def deposit(self, amount):
        if amount < 0:
            raise MyCustomException("Invalid Amount")
        self.balance += amount


    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise MyCustomException("Invalid Amount")
        self.balance -= amount


