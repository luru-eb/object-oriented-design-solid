from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass


class RegularAccount(Account):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        self.amount -= amount

    def deposit(self, amount: float) -> None:
        self.amount += amount


class SavingsAccount(Account):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def withdraw(self, amount: float) -> None:
        raise Exception('Withdrawals are no supported by savings account.')
    
    def deposit(self, amount: float) -> None:
        self.amount += amount


class BankWithdrawalService:
    def __init__(self, account: Account) -> None:
        self.account = account

    def withdraw(self, amount: float) -> None:
        self.account.withdraw(amount)


def main():
    savings_account = SavingsAccount(amount=10000)
    bank_service = BankWithdrawalService(savings_account)
    bank_service.withdraw(amount=1000)

if __name__ == 'main':
    main()