from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    # Add abstract process_payment()
    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    # Implement process_payment()
    def process_payment(self):
        print(f"UPI Payment: {self.amount}")
        


amount = int(input())

# Create the object and process the payment
upi = UPIPayment(amount)
upi.process_payment()