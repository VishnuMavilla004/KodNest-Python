# Write a python code that first reads how many numbers should be entered.
# Then read each number and determine if it is positive, negative or zero. 
# Display the result and the final count of positive, negative, zero numbers and total of sum of the numbers.

number_count = int(input("Enter how many numbers should be entered: "))

#Set Positive, Negative, Zero, Total accumulators
Positive_Count = 0
Negative_Count = 0
Zero_Count = 0
Total = 0 

# Read and analyze each number:
for i in range(number_count):
    numbers = int(input("Enter the number: "))
    Total = Total + numbers
    if numbers > 0:
        Positive_Count = Positive_Count + 1
    elif numbers < 0:
        Negative_Count = Negative_Count + 1
    else:
        Zero_Count = Zero_Count + 1

# Display the results
print(f"Count of Positive Numbers: {Positive_Count}")
print(f"Count of Negative Numbers: {Negative_Count}")
print(f"Count of Zero Numbers: {Zero_Count}")
print(f"Total sum of all Numbers: {Total}")
