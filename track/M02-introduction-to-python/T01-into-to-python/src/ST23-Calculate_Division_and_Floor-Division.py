# Create two variable and store some value or User input
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Calculate the division and floor division
division = first_number / second_number
floor_division = first_number // second_number

# Display the results
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")

# Display the data types of results
print(type(division))
print(type(floor_division))