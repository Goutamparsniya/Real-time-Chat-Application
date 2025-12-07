def create_cracker_price_dict(crackers, prices):
    if len(crackers) != len(prices):
        print("Error: Number of crackers and prices should be the same.")
        return None
    cracker_price_dict = dict(zip(crackers, prices))
    return cracker_price_dict
def get_cracker_price(cracker_price_dict, cracker_name):
    return cracker_price_dict.get(cracker_name, "Cracker not found.")
crackers_input = input("Enter the list of crackers (comma-separated): ")
crackers = crackers_input.split(',')
prices_input = input("Enter the list of prices corresponding to crackers (comma-separated): ")
prices = [float(price) for price in prices_input.split(',')]
if all(isinstance(cracker, str) for cracker in crackers) and all(isinstance(price, (int, float)) for price in prices):
    cracker_price_dict = create_cracker_price_dict(crackers, prices)
    if cracker_price_dict is not None:
        cracker_name = input("Enter the name of the cracker: ")
        price = get_cracker_price(cracker_price_dict, cracker_name)
        print(f"The price of {cracker_name} is: {price}")
else:
    print("Error: Invalid input types. The cracker names should be strings, and the prices should be numbers.")
