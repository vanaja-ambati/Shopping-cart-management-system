class Cart:
    flat_discount = 20
    min_bill = 100

    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(item_name, "added successfully")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(item_name, "removed successfully")
        else:
            print("Item not found")

    def display_items(self):
        print("\nCart Items:")
        print(self.items)

    def calculate_bill(self):
        total = sum(self.items.values())

        if total < Cart.min_bill:
            print("Minimum bill should be Rs.", Cart.min_bill)
            return

        final_amount = total - Cart.flat_discount

        print("Total Bill:", total)
        print("Discount:", Cart.flat_discount)
        print("Amount to Pay:", final_amount)

cart = Cart()

cart.add_item("Book", 120)
cart.add_item("Pen", 30)
cart.display_items()
cart.remove_item("Pen")
cart.display_items()

# Calculate Bill
cart.calculate_bill()
