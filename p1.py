def calculate_discounted_price(product_price):
    threshold_price = 100
    discount_rate = 0.10
    if product_price > threshold_price:
        discounted_price = product_price * (1 - discount_rate)
        return discounted_price
    else:
        return product_price
def main():
    products = {
        'Product1': 120,
        'Product2': 80,
        'Product3': 150,
    }

    user_choice = input("Enter the product you want to buy: ")
    if user_choice in products:
        product_price = products[user_choice]
        discounted_price = calculate_discounted_price(product_price)
        print(f"The discounted price for {user_choice} is: ${discounted_price:.2f}")
    else:
        print(f"Sorry, {user_choice} is not available in our store.")

if __name__ == "__main__":
    main()
