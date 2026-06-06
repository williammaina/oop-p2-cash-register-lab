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
        # Added a flag to prevent multiple applications of the same discount
        self.discount_applied = False

    def add_item(self, item, price, quantity=1):
        self.total += (price * quantity)
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # Check if already applied to prevent error in test logic
        if self.discount_applied:
            return

        self.total = self.total * (1 - (self.discount / 100))
        self.discount_applied = True
        
        # Format string as required by tests
        print(f"After the discount, the total comes to ${self.total:g}.\n")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()
        
        # If we void, we must revert the total
        # If the discount was already applied, we must calculate the value 
        # relative to the discounted state
        reduction = transaction["price"] * transaction["quantity"]
        
        if self.discount_applied:
            reduction = reduction * (1 - (self.discount / 100))
            
        self.total -= reduction

        for _ in range(transaction["quantity"]):
            if transaction["item"] in self.items:
                self.items.remove(transaction["item"])