salary = float(input("Enter your salary: "))
gender = input("Enter your gender (M/F): ").upper()
if gender == "M":
    base_tax_rate = 0.1
else:
    base_tax_rate = 0.08

income_tax = salary * base_tax_rate
print(f"Based on your salary and gender, your payable income tax is: {income_tax:.2f} dollars.")
