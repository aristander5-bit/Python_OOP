from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment for ${amount}")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment for ${amount}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, value):
        if not isinstance(value, PaymentMethod):
            raise TypeError("Unsupported payment type")
        self.__payment_method = value

    def process_payment(self, order):
        total_amount = order.calculate_total()
        self.payment_method.process_payment(total_amount)

class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        total = 0
        for item in self.items:
            name, quantity, price = item
            total += quantity * price
        return total

order_obj = Order([
    ('Apple', 2, 1.0),
    ('Banana', 5, 0.5)
])

credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)