class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        
        # Initialize internal storage for property and invoke setter validation
        self._discount = 0
        self.discount = discount

    # --- Properties ---
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            return
        self._discount = value

    # --- Methods ---
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        # Instructions: If no transactions in array/no discount to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        # Formats float to int cleanly if it has no decimals (e.g., 80.0 -> 80)
        total_amount = int(self.total) if self.total == int(self.total) else self.total
        print(f"After the discount, the total comes to ${total_amount}.")
        return self.total

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last_tx = self.previous_transactions.pop()
        self.total -= last_tx["price"] * last_tx["quantity"]

        for _ in range(last_tx["quantity"]):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])