# Intial code
""" current_age = "21"
    next_age = current_age + 1 # Error : Cannot convert string to integer.
    
    print(f"Current age : {current_age}")
    print(f"Next age : {next_age}") """

# Error Fixed Code
current_age = "21"
current_age = int(current_age)
next_age = current_age + 1
    
print(f"Current age : {current_age}")
print(f"Next age : {next_age}")