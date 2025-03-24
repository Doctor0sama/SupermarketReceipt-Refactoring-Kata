import pytest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog


def test_ten_percent_discount():
    catalog = FakeCatalog()

    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)

    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart = ShoppingCart()
    cart.add_item_quantity(apples, 2.5)
    cart.add_item_quantity(toothbrush, 1)

    receipt = teller.checks_out_articles_from(cart)
    
    #Expected variables
    expected_toothbrush_price = 0.99
    expected_toothbrush_discount = expected_toothbrush_price * 0.1
    expected_toothbrush_discounted_price = expected_toothbrush_price - expected_toothbrush_discount

    expected_apples_price = 2.5 * 1.99

    expected_total_price = expected_toothbrush_discounted_price + expected_apples_price

    #Assertations

    assert pytest.approx(expected_total_price, 0.01) == receipt.total_price()

    assert len(receipt.discounts) == 1
    discount = receipt.discounts[0]
    assert discount.product == toothbrush
    assert discount.description == SpecialOfferType.TEN_PERCENT_DISCOUNT.name
    assert discount.discount_amount == pytest.approx(expected_toothbrush_discount, 0.1)

    assert len(receipt.items) == 2

    receipt_item = receipt.items[0]
    assert receipt_item.product == apples
    assert receipt_item.quantity == 2.5
    assert receipt_item.price == 1.99
    assert receipt_item.total_price == expected_apples_price
