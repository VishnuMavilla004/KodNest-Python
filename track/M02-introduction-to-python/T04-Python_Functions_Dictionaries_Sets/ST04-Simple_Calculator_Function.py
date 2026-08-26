def calculate(first_number, second_number, operator):
    # Write your code here

    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number/second_number
    else:
        pass

first_number = int(input("Enter any number: "))
second_number = int(input("Enter any number: "))
operator = input("Enter any operator: ").strip()

result = calculate(first_number, second_number, operator)
print(result)