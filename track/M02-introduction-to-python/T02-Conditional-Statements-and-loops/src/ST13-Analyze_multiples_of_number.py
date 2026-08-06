limit = int(input("Enter any number: "))
target = int(input("Enter any number: "))
divisor = int(input("Enter any number: "))

# Set accumulators
count = 0
total = 0
found = False

# Examine every number from 1 to the limit
for i in range(1, limit+1):
    if i % divisor == 0:
        count = count + 1
        total = total + i
        if i == target:
            found = True

# Display the results
print(count)
print(total)
if found == False:
    print("Target Found: No")
else:
    print("Target Found: Yes")