class CashRegister:
    def __init__(self, discount=0):
        # Initialize discount, ensuring it is an integer between 0 and 100
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount
            
        # Initialize properties
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity):
        # Add price to total
        self.total += (price * quantity)
        # Add item to the items list
        self.items.append(item)
        # Add transaction details to previous_transactions
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Apply discount as percentage off from the current total
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        return self.total

    def void_last_transaction(self):
        # Check if there are any transactions
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last item from previous_transactions
        last_transaction = self.previous_transactions.pop()
        
        # Adjust total price
        reduction = last_transaction['price'] * last_transaction['quantity']
        self.total -= reduction
        
        # Remove the last item from the items array
        self.items.pop()