height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)

underweight_category = "Underweight"
healthy_weight_category = "Healthy Weight"
overweight_category = "Overweight"
obesity_category = "Obesity"
if bmi < 18.5:
    weight_category = underweight_category
elif 18.5 <= bmi < 24.9:
    weight_category = healthy_weight_category
elif 25 <= bmi < 29.9:
    weight_category = overweight_category
else:
    weight_category = obesity_category
print(f"Your BMI is: {bmi:.2f}")
print(f"Weight Category: {weight_category}")
