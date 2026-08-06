# Read the value of N by user input
N = int(input("Enter any number: "))

# Set accumulators
Counter = 1
Total = 0

# Loop N times
while Counter <= N:
    Total = Total + Counter # Accumulate the sum (Total += Counter)
    Counter = Counter + 1 # Increment counter (Counter += 1)

#display total
print(f"Sum of total numbers: {Total}")