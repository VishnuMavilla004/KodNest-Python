def display_invoice_total(price, quantity):
    # Write your code here
    total = price * quantity
    return print(f"Total: {total}")

price = int(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

display_invoice_total(price, quantity)