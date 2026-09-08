# def divide(a, b):
#     result = a / b
#     return result

# print(divide(10, 2))
# print(divide(15, 3))



# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         self.balance = balance
#         self.amount = amount
#         super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError(balance, amount)
#     return balance - amount

# try:
#     new_balance = withdraw(100, 150)
# except InsufficientFundsError as e:
#     print(f'Transaction failed: {e}')

def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')
