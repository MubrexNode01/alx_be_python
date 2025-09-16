#calculates the projected savings for a year
interest = 0.05

# Collect user inputs
while True:
    user_input1 = input("Enter your monthly income: ")
    user_input2 = input("Enter your monthly expenses: ")

    # Validate inputs
    if user_input1.isdigit() and user_input2.isdigit():
        monthly_income = int(user_input1)
        monthly_expenses = int(user_input2)
        break
    else:
        print("Please enter numbers only!")

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected savings after 1 year with interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest)

print("Your monthly savings are:", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)
