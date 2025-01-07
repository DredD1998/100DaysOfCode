print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n>>> $ "))
tip = int(input("What percentage tip would you like to give?\n>>> $ "))
people = int(input("How many people to split the bill?\n>>> "))
bill_with_tip = tip / 100 * bill + bill
split_bill = round(bill_with_tip/people,2)
print(f"Each person should pay: ${split_bill} ")
