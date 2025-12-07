stock = {
    "apple": 50,
    "banana": 30,
    "chicken breast": 20,
    "broccoli": 40,
}

item_name = input("Enter the name of the item: ").lower()
item_quantity = int(input("Enter the quantity: "))

if item_name in stock and stock[item_name] >= item_quantity:
    print(f"{item_quantity} grams of {item_name} is available in stock.")
    stock[item_name] -= item_quantity
    print(f"Remaining stock of {item_name}: {stock[item_name]} grams.")
else:
    if item_name not in stock:
        print(f"Sorry, {item_name} is not available in stock.")
    else:
        print(f"Sorry, only {stock[item_name]} grams of {item_name} is available in stock.")
print("\nFinalized Stock:")
for item, quantity in stock.items():
    print(f"{item}: {quantity} grams")
