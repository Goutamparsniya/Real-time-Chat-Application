food_calories = {
    "apple": 52,
    "banana": 89,
    "chicken breast": 165,
    "broccoli": 55,
}
food_item = input("Enter the name of the food item: ").lower()
quantity = float(input("Enter the quantity in grams: "))

if food_item in food_calories:
    calories_intake = (food_calories[food_item] / 100) * quantity
    print(f"The amount of calories in {quantity} grams of {food_item} is {calories_intake:.2f} calories.")
else:
    print("Sorry, the entered food item is not in the list. Please choose from the provided list.")
