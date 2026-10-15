
from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, owner, balance):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balans manfiy bo'lmasligi kerak!")
        self.__balance = value

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Kiritiladigan pul musbat bo'lishi kerak!")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Yechiladigan pul musbat bo'lishi kerak!")
        if amount > self.__balance:
            raise ValueError("Mablag' yetarli emas!")
        self.__balance -= amount
        return self.__balance

    def __str__(self):
        return (
            f"Hisob raqami: {self.__account_number}, "
            f"Ega: {self.__owner}, "
            f"Balans: {self.__balance}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.__account_number!r}, "
            f"{self.__owner!r}, {self.__balance!r})"
        )

    def __bool__(self):
        return self.__balance > 0

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance == other.balance

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance < other.balance

    def __gt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.balance > other.balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def account_type(self):
        return "Jamg'arma hisobi"

    def add_interest(self):
        if self.interest_rate < 0:
            raise ValueError("Foiz manfiy bo'lmasligi kerak!")
        self.balance = self.balance * (1 + self.interest_rate / 100)


class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, balance, fee=0):
        super().__init__(account_number, owner, balance)
        self.fee = fee

    def account_type(self):
        return "Joriy hisob"

    def withdraw(self, amount):
        total = amount + self.fee
        return super().withdraw(total)


# Sinab ko'rish
hisob1 = SavingsAccount("1001", "Ali", 100000, 10)
hisob2 = CheckingAccount("1002", "Vali", 50000, 1000)

print(hisob1)
print(hisob2)

hisob1.deposit(20000)
hisob2.withdraw(5000)

print("Ali hisobi:", hisob1.balance)
print("Vali hisobi:", hisob2.balance)

hisob1.add_interest()
print("Foiz qo'shilgandan keyin:", hisob1.balance)

print("Hisob turi:", hisob1.account_type())
print("Balanslar tengmi?", hisob1 == hisob2)
print("Ali hisobida pul bormi?", bool(hisob1))
print("Ali hisobi:", repr(hisob1))
print("Ali hisobida ko'proq pulmi?", hisob1 > hisob2)
