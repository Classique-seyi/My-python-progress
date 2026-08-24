
name = input("What is your name? ")

if name == "Ben" or name == "Patricia" or name == "Loki": 
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You're not welcome here, " + name + " please leave")
        exit()
    else:
        print("You can come on in")
else:
    print(name + " You're welcome")


menu = "latte , black coffee, espresso, cappuccino, frappuccino"

print(name + ", what would you like from our menu. \n" + menu)

order = input( )
if order == "frappuccino":
    price = 100
elif order == "blackcoffee":
    price = 50
elif order == "latte":
    order_latte = input("Do you want whipped cream?\n")
    if order_latte == "Yes":
        price = 85
    else:
        price = 80
    
elif order == "espresso":
    price = 70
elif order == "cappuccino":
    price = 90
else:
    print("Sorry we don't have that here")
    price = 0
    exit()

print("That would cost you " + str(price))
# print(type(price))
Quantity = input("How many " + order + " will you like? ")
Total = price * int(Quantity)
print("Thank you, Your total is: " + str(Total))
print("Sounds good " + name + " we'll have your " + Quantity + " " + order + " ready for you in a moment")


