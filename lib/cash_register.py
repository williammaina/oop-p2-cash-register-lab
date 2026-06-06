class CashRegister:
    def __init__(self, discount=0):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0
            
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += (price * quantity)
        
        # Add the item to the list for each quantity added
        for _ in range(quantity):
            self.items.append(item)
            
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply the discount to the current total
        self.total = self.total * (1 - (self.discount / 100))

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.") # Matching lab requirement if applicable
            return

        transaction = self.previous_transactions.pop()
        
        # Subtract the value from total
        self.total -= (transaction["price"] * transaction["quantity"])
        
        # Remove the specific number of items that were added
        for _ in range(transaction["quantity"]):
            self.items.remove(transaction["item"])