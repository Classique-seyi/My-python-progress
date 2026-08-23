balance = 50000

print("Welcome to the ATM Simulator!")
while True:   #this loop will keep the program running until the user chooses to exit
    print('Menu:')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    option = input('Please select an option (1-4): ')


    if option == '1':
        print(f'Your current balance is: ₦{round(balance, 2)}')
    elif option == '2':
        deposit_amount = float(input('Enter the amount to deposit: '))
        if deposit_amount <= 0:    #this condition checks if the deposit amount is less than or equal to zero, which is invalid for a deposit 
            print('Invalid deposit amount')
        else:
            balance += deposit_amount
            print(f'You have successfully deposited ₦{round(deposit_amount, 2)}\nYour new balance is: ₦{round(balance, 2)}')
    elif option == '3':
        withdraw_amount = float(input('Enter the amount to withdraw: '))
        if withdraw_amount <= 0:
            print('Invalid withdrawal amount')
        elif withdraw_amount > balance:
            print('Insufficient funds')
        else:
            balance -= withdraw_amount
            print(f'You have successfully withdrawn ₦{round(withdraw_amount, 2)}\nYour new balance is: ₦{round(balance, 2)}')
    elif option == '4':
        print('Thank you for using our AtM')
        break  #this exits the while loop and ends the program
    else:
        print(f'Invalid option.\nPlease select a valid option (1-4).')