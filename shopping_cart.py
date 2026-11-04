# SHOPPING CART
# You are building a text-based online store.
# The program prints your list of 20 items, 
# lets the user type IDs to drop items into a digital cart, 
# and then adds up the total price to print a final receipt when they checkout.

# The store's available inventory
store_items = [
    {"id": 1, "name": "Wireless Mouse", "price": 25.99},
    {"id": 2, "name": "Mechanical Keyboard", "price": 79.99},
    {"id": 3, "name": "Gaming Headset", "price": 45.50},
    {"id": 4, "name": "USB-C Cable (6ft)", "price": 8.99},
    {"id": 5, "name": "Laptop Stand", "price": 34.00},
    {"id": 6, "name": "HDMI Switcher", "price": 19.95},
    {"id": 7, "name": "1080p Webcam", "price": 49.99},
    {"id": 8, "name": "Desk Pad Mat", "price": 15.50},
    {"id": 9, "name": "Bluetooth Speaker", "price": 39.99},
    {"id": 10, "name": "128GB USB Flash Drive", "price": 14.99},
    {"id": 11, "name": "Ergonomic Wrist Rest", "price": 12.00},
    {"id": 12, "name": "Dual Monitor Arm", "price": 64.95},
    {"id": 13, "name": "Ring Light with Stand", "price": 29.99},
    {"id": 14, "name": "External 1TB HDD", "price": 54.99},
    {"id": 15, "name": "Screen Cleaning Kit", "price": 7.50},
    {"id": 16, "name": "RGB LED Strip Lights", "price": 11.99},
    {"id": 17, "name": "Wireless Charger Pad", "price": 18.50},
    {"id": 18, "name": "Noise Cancelling Earbuds", "price": 89.99},
    {"id": 19, "name": "Cable Management Clips", "price": 6.99},
    {"id": 20, "name": "Laptop Sleeve Case", "price": 21.50}
]

my_cart = []

while True:
    print("Do you wish to add or remove an item to cart? Yes/No")
    customer_response = input("Enter your response: ")
    if customer_response == "Yes" or "yes":
        for item in store_items:
            print(f"id: {item["id"]}")
            print(f"name:  {item["name"]}")
            print(f"price: {item["price"]}")
            print()
            print()
        selected_item = input("Enter your choice item id: ")
        item_selected = int(selected_item)
        for choice in store_items:
            if choice["id"] == item_selected:
                my_cart.append(choice)
                print(my_cart)
                continue
    
    else:
        if len(my_cart) >0:
            print("Which item do you wish to remove from cart: ")
            print(my_cart)
            item_to_remove = input("Please remove the item with this id: ")
            item_removed = int(item_to_remove)
            for item in store_items:
                if item["id"] == item_removed:
                    index = my_cart.index(item)
                    my_cart.pop(index)
                    print()
                    print(my_cart)
                    print()
                    break
                elif item["id"]  != item_removed:
                    print()
                    print("Error, the item id entered is not in your cart")
                    break
        else:
            print()
            print("Thanks you for visiting the store today")
    
                

    
    


