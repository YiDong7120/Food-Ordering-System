import classMeals as c

layout = "{0:<10}{1:<10}{2:<30}"
current_order = []

# the main function of the food ordering system
def main_menu():
    while True:
        print()
        print("=" * 40)
        print(layout.format("", "Food Ordering System", ""))
        print("=" * 40)
        main_lis = ["1. Order", "2. View order summary", "3. Payment", "4. Exit"]
        for i in main_lis:
            print(layout.format("", i, ""))

        key = input("\n" + "Enter your choice: ")

        if (key == '1'):
            food_drink_order()
            break

        elif (key == '2'):
            view_order()
            break

        elif (key == '3'):
            pay_order()
            break

        elif (key == '4'):
            print("\n" + "Exiting the food ordering system...")
            print("Thank you. Have a nice day!")
            break

        else:
            print()
            print("Invalid input! Please try again ")
            continue

# show the food menu and drink menu to let the customer to order
def food_drink_order():
    while True:
        print(layout.format("", "", "-" * 21))
        print(layout.format("", "", "| FOOD & DRINK MENU |"))
        print(layout.format("", "", "-" * 21))

        partFood = read_menu_file("food-menu.txt")
        food = c.Food(partFood[0], partFood[1], partFood[2])
        foodInfo, foodPrice = food.show_food()
        print()
        partDrink = read_menu_file("drink-menu.txt")
        drink = c.Drink(partDrink[0], partDrink[1], partDrink[2])
        drinkInfo, drinkPrice = drink.show_drink()

        print("{0:<20}{1:<20}{2:<20}".format("\n" + "(U). Update", "(M). Main Menu", "(P). Payment"))
        print()

        key = str(input("Please select your choice: ")).upper()

        if (key == 'U'):
            while True:
                print("\n" + "Update for: ")
                print("\n" + "(F). Food \t (D). Drink \t (E). Exit" + "\n")
                keyUpdate = str(input("Choice: ")).upper()
                if keyUpdate == 'F':
                    update(foodInfo, foodPrice)
                    break

                elif keyUpdate == 'D':
                    update(drinkInfo, drinkPrice)
                    break

                elif keyUpdate == 'E':
                    break

                else:
                    print("Invalid input! Please try again!")
                    continue

        if (key == 'M'):
            main_menu()
            break

        if (key == 'P'):
            pay_order()
            break

        if (key != 'U' and key != 'M' and key != 'P'):
            flag1 = get_order(key, foodInfo, foodPrice)
            flag2 = get_order(key, drinkInfo, drinkPrice)

            if flag1 is not flag2:
                pass
            else:
                print("Sorry, we didn't serve that. Please choose again!")
                continue

        keyContinue = str(input("\n" + "Continue order? (y/n) ")).upper()

        if (keyContinue == 'Y'):
            continue
        elif (keyContinue == 'N'):
            main_menu()
            break
        else:
            print("Invalid input!")
            continue

# append the customer's order list if customer order for either food or drink
def get_order(key, lisInfo, dicPrice):
    flag = 0
    for code, name in lisInfo:
        if (key == code):
            price = dicPrice[name]
            print(layout.format("", "-" * 10, "-" * 30 ))
            print(layout.format("", "Item " , "| " + name))
            print(layout.format("", "Price", "| RM " + str(price)))
            print(layout.format("", "-" * 10, "-" * 30 ))
            print("(Q). Quantity \t (R). Return")

            while True:
                key2 = str(input("\n" + "Choice: ")).upper()
                if (key2 == 'Q'):
                    keyQuantity = int(input("Enter quantity: "))
                    totalEachPrice = round(keyQuantity* price, 2)
                    current_order.append(dicOrder(Name=name, Num=keyQuantity, Price=totalEachPrice))
                    delete()
                    print("\n" + "You have chosen:")
                    for item in current_order:
                        print (item)
                    flag = 1
                    break
                elif (key2 == 'R'):
                    break
                else:
                    print("Invalid choice! Please choose again....")
                    continue
        else:
            continue
    return flag

# delete the order item in which the quantity equals to zero
def delete():
    for i in range(len(current_order)):
        if current_order[i]['Num'] == 0:
            del current_order[i]
            break

# change the quantity of order item
def update(lisInfo, dicPrice):
    keyItem = str(input("Enter code you wish to change the quantity: ")).upper()
    for code, name in lisInfo:
        if keyItem == code:
            for i in current_order:
                if i['Name'] == name:
                    keyQuantity = int(input("Enter quantity: "))

                    # update the item's quantity
                    i['Num'] = keyQuantity

                    # update the item's total price
                    i['Price'] = round(keyQuantity * dicPrice[name], 2)

                    # if the item's quantity is equal to zero, delete the item from list
                    delete()

                    print("\n" + "You have chosen:")
                    for item in current_order:
                        print (item)
                    print("\n" + "Update success." + "\n")
                    flag = 1
                    break

                else:
                    continue
            break
    else:
        print("The item you choose is not in the order list. \n")

# view what that customer has order
def view_order():
    print(layout.format("", "", "-" * 17))
    print(layout.format("", "", "| ORDER SUMMARY |"))
    print(layout.format("", "", "-" * 17))
    layout2 = "{0:<5}{1:<25}{2:<15}{3:<10}"
    print('─' * 60)
    print(layout2.format("", "-Name-", "-Quantity-", "-Price-"))
    print('─' * 60)
    i = 1
    for item in current_order:
        print(layout2.format(i, item['Name'], " " * 4 + str(item['Num']), " " + str(item['Price'])))
        i += 1
    while True:
        print("\n" + "(R). Return")
        keyReturn = input("Enter: ").upper()
        if (keyReturn == 'R'):
            main_menu()
            break
        else:
            print("Invalid input! Please enter again.")
            continue

# calculate the total amount of customer's order items and printing receipt
def pay_order():
    print("\n" + "Printing receipt....")
    total = 0
    layout1 = "{0:<30}{1:<10}{2:<10}"
    receipt = open("Receipt.txt", "w")
    receipt.write(layout.format("\n" + "", "", " " * 4 + "RECEIPT"))
    receipt.write(layout.format("\n" + "", " " * 2 + "RESTAURANT BENR2822 ASSIGNMENT (G6)", ""))
    receipt.write('\n' + '=' * 52 + '\n')
    receipt.write(layout1.format("-ITEM-", "-QTY-", "-AMT (RM)-"))
    receipt.write('\n' + '=' * 52 + '\n')

    for item in current_order:
        receipt.write(layout1.format(item['Name'] , " " * 2 + str(item['Num']) , " " * 3 + str(item['Price'])))
        receipt.write("\n")
        total =  round(total + item['Price'], 2)

    receipt.write('\n' + '─' * 52)
    receipt.write(layout1.format("\n", " Total  :", " " * 4 + str(total)))
    receipt.write('\n' + '─' * 52)
    receipt.write(layout.format("\n" + "", "", " " * 3 + "THANK YOU!"))
    receipt.close()
    print("\n" + "Thank you for using this system!")

# read the food and drink menu
def read_menu_file(fileRead):
    item_code = []
    item_name = []
    item_price = []
    file = open(fileRead, "r")
    for line in file:
        data = line.split(";")
        item_code.append(data[0])
        item_name.append(data[1])
        item_price.append(float(data[2]))
    file.close()
    return item_code, item_name, item_price

# return in the form of dictionary (variable length keyword arguement)
def dicOrder(**order):
    return order