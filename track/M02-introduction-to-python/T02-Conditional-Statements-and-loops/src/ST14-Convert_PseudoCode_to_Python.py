# Pseudocode: 
"""
READ limit

SET number = 1
SET total = 0

WHILE number <= limit:
    IF number % 2 == 0:
        SET total = total + number
    ENDIF
    SET number = number + 1
ENDWHILE

PRINT "Even Sum:", total

"""

# Python Code:

limit = int(input("Enter any number: "))

# Set accumulators
number = 1
total = 0

while number <= limit:
    if number % 2 == 0:
        total = total + number

    number = number + 1

print(f"Even Sum: {total}")