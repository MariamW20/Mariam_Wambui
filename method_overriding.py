#Payment Processing using different Payment Methods
class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via generic method.")

class CreditCard(PaymentGateway):
    def process_payment(self, amount):  # Overrides parent method
        print(f"Processing ${amount} via Credit Card (with 5% fee).")

class PayPal(PaymentGateway):
    def process_payment(self, amount):  # Overrides parent method
        print(f"Processing ${amount} via PayPal (with $0.50 fixed fee).")

payment = PaymentGateway()
credit_card = CreditCard()
paypal = PayPal()

payment.process_payment(100)   # Using the Generic method  
credit_card.process_payment(100)  # Using the CreditCard version  
paypal.process_payment(100)      # Using the PayPal version  