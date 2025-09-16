# Calculates the age of a user in future year eg 2050

future_year = 2050
current_year = 2023

while True:
    user_input = input("How old are you: ")
    
    if user_input.isdigit():   # check if input is only numbers
        age = int(user_input)
        break
    else:
        print("Please enter numbers only!")

age_in_2050 = age + (future_year - current_year)
print("In 2050, you will be", age_in_2050, "years old")

