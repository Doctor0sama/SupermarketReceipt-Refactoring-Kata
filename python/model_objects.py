from enum import Enum, auto
from catalog import SupermarketCatalog

class ProductUnit(Enum):
    EACH = auto()
    KILO = auto()
    
class Product:
    def __init__(self, name: str, unit: ProductUnit):
        self.name = name
        self.unit = unit


class ProductQuantity:
    def __init__(self, product: Product, quantity: float):
        self.product = product
        self.quantity = quantity

class SpecialOfferType(Enum):
    THREE_FOR_TWO = auto()
    TEN_PERCENT_DISCOUNT = auto()
    TWO_FOR_AMOUNT = auto()
    FIVE_FOR_AMOUNT = auto()

class Offer:
    def __init__(self, offer_type: SpecialOfferType, product: Product, argument: float):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument


class Discount:
    def __init__(self, product: Product, description: str, discount_amount: float):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount


class DiscountCalculator:
    """Handles all different discount types based on offers"""

    @staticmethod
    def calculate_discount(product: Product, quantity: float, offer: Offer, catalog: SupermarketCatalog) -> Discount | None:
        product = product
        quantity = quantity
        unit_price = catalog.unit_price(product)
        discount_amount = 0

        match offer.offer_type:
            case SpecialOfferType.THREE_FOR_TWO:
                discount_amount = (quantity // 3) * unit_price

            case SpecialOfferType.TEN_PERCENT_DISCOUNT:
                discount_amount = (quantity * unit_price) * (offer.argument / 100)
            
            case SpecialOfferType.TWO_FOR_AMOUNT:
                discount_amount = (quantity // 2) * (unit_price * 2 - offer.argument)
            
            case SpecialOfferType.FIVE_FOR_AMOUNT:
                discount_amount = (quantity // 5) * (unit_price * 5 - offer.argument)
            
        if discount_amount > 0:
            return Discount(product, f"{offer.offer_type.name}", round(discount_amount, 2))
        
        return None