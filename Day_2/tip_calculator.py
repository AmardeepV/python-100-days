print("Welcome to the tip calculator")
total_bill = float(input("What was the totatl bill? "))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = float(input("How many people to split the bill? "))
bill_for_each = (total_bill + (total_bill * tip / 100)) / total_people
print(f"Each person should pay: {bill_for_each:.2f}")
