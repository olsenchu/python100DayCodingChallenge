print("Welcome to the tip calculator!")
bill_total = input("What was the total bill?\n")
tip_percent = input("What % tip would you like to give?\n")
tip_factor = ((int(tip_percent) / 100)) + 1
guest_count = input("How many people to split the bill?\n")
cost_per_guest = ((float(bill_total)) / (int(guest_count))) * (tip_factor)
cost_per_guest = round(cost_per_guest, 2)
cost_per_guest = "{:.2f}".format(cost_per_guest)
print(f"Each person should pay ${cost_per_guest}.")