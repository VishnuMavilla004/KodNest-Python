from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        print(f"UPI Payment: {self.amount}")


class CardPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        print(f"Card Payment: {self.amount}")


class NetBankingPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        print(f"Net Banking Payment: {self.amount}")


upi_amount = int(input())
card_amount = int(input())
net_banking_amount = int(input())

# Create the three objects
upi = UPIPayment(upi_amount)
card = CardPayment(card_amount)
net = NetBankingPayment(net_banking_amount)
# Store them in one list
Payments = [upi, card, net]

# Process them using one loop
for payment in Payments:
    payment.process_payment()