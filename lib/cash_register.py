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
        # Fix for test_apply_discount_when_no_discount
        # Check if there are no transactions OR if the discount is 0
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return

        if self.discount_applied:
            return

        self.total = self.total * (1 - (self.discount / 100))
        self.discount_applied = True
        
        print(f"After the discount, the total comes to ${self.total:g}.\n")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()
        
        reduction = transaction["price"] * transaction["quantity"]
        
        # If discount was applied, reverse the discount portion of the reduction
        if self.discount_applied:
            reduction = reduction * (1 - (self.discount / 100))
            
        self.total -= reduction

        for _ in range(transaction["quantity"]):
            if transaction["item"] in self.items:
                self.items.remove(transaction["item"])
        
        # If no transactions left, reset the discount state
        if not self.previous_transactions:
            self.discount_applied = False