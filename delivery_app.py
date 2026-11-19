# Delivery and Logistics System

items = []
items_delivered = []
max_weight_kg = 100
total_item_weight = 0
price_per_kg = 1000



def calculate_price(weight, price_per_kg):
    price = weight * price_per_kg
    return price


while True:
    print("**************")
    print("Welcome to Codents logistics.")
    print("**************")
    print()
    while total_item_weight < max_weight_kg:
        print("What item would you want to deliver today?")
        print()
        item_name = input("Please enter the name of the item:   ")
        item_weight = int(input("Please enter the weight of the item:   ").strip())
        total_item_weight += item_weight
        item_dict = {
            "item_name": item_name,
            "item_weight": item_weight
        }
        items.append(item_dict)
        response = input("Would you like to add more items? yes/no:  ")
        if response == "yes":
            continue
        elif response == "no":
            break
        else:
            break
    price = calculate_price(total_item_weight, price_per_kg)
    print(f"Your total price for your delivery is {price}")
    print("Your goods are being delivered now")
    print()
    print("**************")
    print("Thank you for trusting codnets with your deliveries..")
    print("**************")
    break