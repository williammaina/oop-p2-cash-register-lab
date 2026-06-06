class CashRegister:

    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []

        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")
            self._discount = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last_transaction = self.previous_transactions.pop()

        item = last_transaction["item"]
        price = last_transaction["price"]
        quantity = last_transaction["quantity"]

        self.total -= price * quantity

        for _ in range(quantity):
            if item in self.items:
                self.items.remove(item)