# Write cart_builder.py using while True and break :

# 1.Repeatedly ask for an item name and price. Typing done as the item name finishes the shopping.
# 2.Reject a blank item name using continue
# 3.Validate the price in its own inner loop — keep asking until it is a proper number
# 4.Store each item in a list of dictionaries
# 5.At the end, print a full receipt with a for loop, plus subtotal, 7.5% VAT and grand total
# 6.Handle the case where nothing was bought

# Cart Builder App

konga_shop = {'Television': 75000, 'Cupboard' : 45300, 'Table' : 49000, 'Chair' : 23500, 'Bulb' : 93200, 'Machine' : 83000, 'Laptop' : 127500, 'Decoder' : 66500, 'Socket' : 17700, 'Router' : 51000, 'Speakers' : 205000, 'Fan' : 52500, 'Stabilizer' : 96400}

available_items = 0

for items in konga_shop:
    shopers_choice = input()
    if shopers_choice == items:
        print(f"The {items} is available")
        break
    else:
        print("Please the item requested is not available")
        available_items += 1
        continue
# while shopers_choice is True:
#     print(f"The requested item {shopers_choice} is available")
#     available_items += 1
