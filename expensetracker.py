expenses_list = []


while True:
    print('''=======MENU=======
1. Add expense
2. View expenses
3. View summary
4. Quit
==================
''')

    while True:
        choice = input("What would you like to do: ")
        if not choice:
            print("Choice can't be empty")
            continue
        break
    
    if choice == "1":        
        while True:
            description = input("Enter description: ").strip().capitalize()
            if not description:
                print("Description can not be empty")
                continue
            break

        while True :
            category = input("Enter category: ").strip().title()
            if not category:
                print("Description and category can not be empty")
                continue
            break

        while True:
            try:
                amount = float(input("Enter amount spent: "))
            except ValueError:
                print("Enter a valid amount")
                continue
            break

        if amount <= 0:
            print("Invalid amount")
        else:
            expense = {
            "Description": description,
            "Category": category,
            "Amount": amount
            }
            expenses_list.append(expense)
            print("Expense added successfuly")
    elif choice == "2":
        if not expenses_list:
            print("You have no expenses")
        else:
            for index, expense in enumerate(expenses_list, 1):
                print(index, expense)
                # print(f"Description: {description}\nCategory: {category}\nAmount: {amount}")
    elif choice == "3":
        if not expenses_list:
            print("You have no expenses to summarize")
        else:
            total = 0
            expensive = expenses_list[0]
            category_totals = {}

            for expense in expenses_list:
                category = expense["Category"]
                amount = expense["Amount"]

                #Calculating the overall spending
                total += amount

                #Calculating spending by category
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

                #Finding the most expensive expense
                if amount > expensive["Amount"]:
                    expensive = expense

            print(f"Total spent: {total:.2f}")

            print("\nSpending Total by category")
            for category, total_amount in category_totals.items():
                print(f"{category}: {total_amount:.2f}")
                # print(f"Total spent: {total:.2f}\n{category}: {category_totals}\nMost expensive expense: {amount:.2f}")

            print(f"\nMost expensive expense: {expensive["Category"]}- {expensive["Amount"]:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, pick a number in the menu")


        
    