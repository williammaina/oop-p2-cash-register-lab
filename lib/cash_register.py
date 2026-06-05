#!/usr/bin/env python3
class CashRegister:
    """Represents a cash register system for a bookstore."""

    def __init__(self, discount=0):
        # Initialize attributes
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Ensure discount is an integer between 0 and 100
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity):
        """Adds an item, updates the total, and records the transaction."""
        cost = price * quantity
        self.total += cost
        self.items.append(item)
        
        # Store transaction object
        transaction = {"item": item, "price": price, "quantity": quantity}
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Applies the stored discount percentage to the current total."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return
        
        # Calculate discount: Total * (1 - discount/100)
        multiplier = 1 - (self.discount / 100)
        self.total *= multiplier

    def void_last_transaction(self):
        """Removes the last transaction and adjusts the total."""
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Retrieve the last transaction
        last_trans = self.previous_transactions.pop()
        
        # Adjust total
        cost = last_trans['price'] * last_trans['quantity']
        self.total -= cost
        
        # Remove item from items list
        if last_trans['item'] in self.items:
            self.items.remove(last_trans['item'])

# Example usage:
if __name__ == "__main__":
    register = CashRegister(discount=20)
    register.add_item("Book", 10.0, 2)
    print(f"Total after adding: {register.total}")
    
    register.apply_discount()
    print(f"Total after 20% discount: {register.total}")