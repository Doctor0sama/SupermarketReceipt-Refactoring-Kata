from model_objects import ProductQuantity, Discount
class ReceiptItem:
    def __init__(self, product_quantity: ProductQuantity, price: float):
        self.product = product_quantity.product
        self.quantity = product_quantity.quantity
        self.price = price
        self.total_price = self.price * self.quantity

class Receipt:
    def __init__(self):
        self._items = []
        self._discounts = []

    def total_price(self):
        total = sum(item.total_price for item in self._items)
        total -= sum(discount.discount_amount for discount in self._discounts)
        return total

    def add_product(self, product_quantity: ProductQuantity, price: float):
        self._items.append(ReceiptItem(product_quantity, price))

    def add_discount(self, discount: Discount):
        self._discounts.append(discount)

    @property
    def items(self):
        return self._items[:]

    @property
    def discounts(self):
        return self._discounts[:]
