class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: ₦{self.balance}"
    
    def deposit(self, amount):
            if amount <= 0:
                return "Invalid deposit amount"
            else:
                self.balance += amount
                return "Deposit successful"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return "Withdrawal successful"
    def check_balance(self):
        return f"{self.owner}'s balance is ₦{self.balance}"
    
    def get_owner(self):
            return f"{self.owner} is the account's name"

    def has_sufficient_funds(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def transfer(self, amount, other_account):
        if amount <= 0:
            return "Invalid amount"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            other_account.balance += amount
            return "Transfer successful"


class SavingsAccount(BankAccount):
    pass

savings = SavingsAccount("Precious", 100000)
# account1 = BankAccount("Precious", 80000)
# account2 = BankAccount("David", 25000)
# result = account1.transfer(20000, account2)


# print(account1)
print(savings)
print(savings.check_balance())
# print(account1.withdraw(10000))
# print(account1.check_balance())

# print(result)

# print(account1.get_owner())

# print(account1.has_sufficient_funds(50000))
# print(account1.has_sufficient_funds(100000))

# print(account1.balance)
# print(account2.balance)



try:
    value = int('This will raise an error')
except ValueError as me:
    print(f'Caught an error: {me}')