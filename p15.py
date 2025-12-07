def calculate_interest(loan_type, loan_amount):
    if loan_type == "home":
        interest_rate = 0.05  # 5% for home loans
    elif loan_type == "car":
        interest_rate = 0.08  # 8% for car loans
    elif loan_type == "personal":
        interest_rate = 0.1  # 10% for personal loans
    else:
        print("Invalid loan type.")
        return None
    interest_amount = loan_amount * interest_rate
    return interest_amount

loan_type = input("Enter the type of loan (home/car/personal): ").lower()
loan_amount = float(input("Enter the loan amount: "))
interest = calculate_interest(loan_type, loan_amount)
if interest is not None:
    print(f"For a {loan_type} loan of ${loan_amount}, the interest to be paid is ${interest:.2f}.")
