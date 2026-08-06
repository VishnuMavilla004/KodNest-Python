# Display a Number sequence and word characters

# Read the number and word by user input
Number = int(input("Enter any number: "))
Word = input("Enter any text: ")

# Print the number sequence
print("Numbers: ")
for i in range(1, Number+1):
    print(i)

# Print the word characters
print("Characters: ")
for i in Word:
    print(i)