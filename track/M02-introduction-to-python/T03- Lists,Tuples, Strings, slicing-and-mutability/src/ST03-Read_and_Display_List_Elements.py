# Write a python code that first reads the size of a list by user input.
# and accepts each element from user input and stores in list

N = int(input("Enter the no. of elements: "))

# Empty list
numbers = []

for i in range(N):
    num = int(input("Enter the element: "))
    numbers.append(num)

print(f"The elements of the list are: {numbers}")
