from model_objects import Offer, SpecialOfferType, Product
from catalog import SupermarketCatalog
from receipt import Receipt
from shopping_cart import ShoppingCart

class Teller:

    def __init__(self, catalog: SupermarketCatalog):
        self.catalog = catalog
        self.offers = {}

    def add_special_offer(self, offer_type: SpecialOfferType, product: Product, argument: float):
        self.offers[product] = Offer(offer_type, product, argument)

    def checks_out_articles_from(self, the_cart: ShoppingCart):
        receipt = Receipt()
        product_quantities = the_cart.items
        for product_quantity in product_quantities:
            product = product_quantity.product
            unit_price = self.catalog.unit_price(product)
            receipt.add_product(product_quantity, unit_price)

        the_cart.handle_offers(receipt, self.offers, self.catalog)

        return receipt
