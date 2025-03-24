import math
from collections import defaultdict
from typing import Dict

from model_objects import Offer, ProductQuantity, Product, DiscountCalculator
from catalog import SupermarketCatalog
from receipt import Receipt


class ShoppingCart:

    def __init__(self):
        self._items = []
        self._product_quantities = defaultdict(float)

    @property
    def items(self):
        return self._items

    def add_item(self, product: Product):
        self.add_item_quantity(product, 1.0)

    @property
    def product_quantities(self):
        return self._product_quantities

    def add_item_quantity(self, product: Product, quantity: float):
        self._items.append(ProductQuantity(product, quantity))
        self._product_quantities[product] += quantity

    def handle_offers(self, receipt: Receipt, offers: Dict[Product, Offer], catalog: SupermarketCatalog):
        for product, quantity in self._product_quantities.items():
            if product in offers:
                discount = DiscountCalculator.calculate_discount(product, quantity, offers[product], catalog)

                if discount:
                    receipt.add_discount(discount)