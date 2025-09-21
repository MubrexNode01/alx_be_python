# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to handle rows
while row < size:
    # For loop to handle columns (printing asterisks in a row)
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line after finishing one row
    row += 1
