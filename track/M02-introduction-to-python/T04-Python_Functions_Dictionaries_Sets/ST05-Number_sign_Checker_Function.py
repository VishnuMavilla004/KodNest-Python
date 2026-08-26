def check_sign(number):
    # Write your code here
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter any number: "))
result = check_sign(number)
print(result)