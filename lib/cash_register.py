class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

        if isinstance(discount, int) and 0 <= discount <= 100:
            self.discount = discount
        else:
            print("Not valid discount")
            self.discount = 0

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        # Only add item once to items list
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

        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["price"] * transaction["quantity"]

        if transaction["item"] in self.items:
            self.items.remove(transaction["item"])