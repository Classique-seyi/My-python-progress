def filter_expenses(expenses, category):
    category_list = []
    
    for expense in expenses:
        if expense['category'] == category:
            category_list.append(expense)
    return category_list

def calculate_total(expenses): 
    total = 0
    for expense in expenses:
        amount = expense['amount']
        total += amount
    return(total)

def calculate_category_total(expenses, category):
    filtered = filter_expenses(expenses, category)
    return calculate_total(filtered)

def find_most_expensive(expenses):
    most_expensive = expenses[0]

    for expense in expenses:
        amount = expense['amount']

        if amount > most_expensive['amount']:
            most_expensive = expense

    return most_expensive

def count_expenses_by_category(expenses, category):
    count = 0
    for expense in expenses:
        if expense['category'] == category:
            count += 1
    return count



expenses = [
    {"description": "Rice", "category": "Food", "amount": 5000},
    {"description": "Bus fare", "category": "Transport", "amount": 1500},
    {"description": "Chicken", "category": "Food", "amount": 4000},
    {"description": "Fuel", "category": "Transport", "amount": 8000}
]

# print(filter_expenses(expenses, "Food"))
# print(filter_expenses(expenses, "Transport"))

# print(calculate_total(expenses))
# print(calculate_category_total(expenses, "Food"))
# print(calculate_category_total(expenses, "Shopping"))

print(find_most_expensive(expenses))

print(count_expenses_by_category(expenses, "Transport"))