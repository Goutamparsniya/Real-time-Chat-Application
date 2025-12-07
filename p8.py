from datetime import datetime

date_input = input("Enter the date in the format DD/MM/YYYY: ")
date_object = datetime.strptime(date_input, "%d/%m/%Y")
day_of_week = date_object.weekday()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Su0nday"]
print(f"The day on {date_input} is {days_of_week[day_of_week]}.")
