menu = ["Big Mac", "Coke Float", "French Fries"]
price = [120, 70, 100]

total_price = 0

while True:
        print("Choose the number of the item you want to order. Enter 0 to finish.")
        def display_menu(menu, price):
            a = 0
            while a < len(menu):
                print(f"{a+1}. {menu[a]}: ₱{price[a]}")
                a += 1

        display_menu(menu, price)

        choice = int(input("\nEnter your choice: "))

        if choice == 0:
            break
        
        elif 1 <= choice <= len(menu):
            total_price += price[choice - 1]
            print(f"\nAdded {menu[choice - 1]} to your order. Total: ₱{total_price}")

        else:
            print("Invalid choice. Please select a valid menu item.")

print(f"\nYour total bill is: {total_price}")

while True:
    fee = int(input("Enter your fee: "))
    change = fee - total_price

    if fee >= total_price:
        print(f"\nChange: {change}")
        break
    else:
        print(f"\nYour fee is not enough. Please pay higher than {total_price}")

print("Thank you for your order. Come Again.")