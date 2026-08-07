# Extract data using slicing only
# Create three different data types of variables

# String
word = input("Enter any word: ")

first = int(input("Enter any number: "))
second = int(input("Enter any number: "))
third = int(input("Enter any number: "))
#List and Tuple
numbers = [first, second, third]
records = (first, second, third)

# Original Values of the three data types
print(word)
print(numbers)
print(records)

# Display the characters of string without first and last character
# Display the first two elements of List
# Display the elements of tuple in reverse order

print(f"Middle elements: {word[1:-1]}")
print(f"First Two elements of List: {numbers[0:2]}")
print(f"Reversed tuple: {records[::-1]}") 