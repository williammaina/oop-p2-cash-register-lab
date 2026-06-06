class CashRegister:
    def __init__(self, discount=0):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

        self.items = []
        self.previous_transactions = []
        # We track the 'raw' total so we don't lose the original numbers
        self.raw_total = 0 
        self.discount_applied = False

    @property
    def total(self):
        """Calculates total on the fly based on current state."""
        current_total = self.raw_total
        if self.discount_applied:
            current_total = current_total * (1 - (self.discount / 100))
        return current_total

    def add_item(self, item, price, quantity=1):
        self.raw_total += (price * quantity)
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        if self.discount_applied:
            # If already applied, just print the message again if required
            print(f"After the discount, the total comes to ${self.total:g}.\n")
            return

        self.discount_applied = True
        print(f"After the discount, the total comes to ${self.total:g}.\n")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()
        
        # Remove raw price
        reduction = transaction["price"] * transaction["quantity"]
        self.raw_total -= reduction

        # Remove items
        for _ in range(transaction["quantity"]):
            if transaction["item"] in self.items:
                self.items.remove(transaction["item"])
        
        # If transaction list is empty, reset discount status
        if not self.previous_transactions:
            self.discount_applied = False