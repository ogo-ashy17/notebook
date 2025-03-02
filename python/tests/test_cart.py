import unittest

from cart import ShoppingCart
from product import Product


class ProductTestCase(unittest.TestCase):
    def test_transform_name_for_sku(self):
        medium_pink_tankl_top = Product('tank top', 'M', 'pink')
        self.assertEqual(medium_pink_tankl_top.transform_name_for_sku(), 'TANKTOP')

    def test_transform_color_for_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(small_black_shoes.transform_color_for_sku(), 'BLACK')

    def test_generate_sku(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(small_black_shoes.generate_sku(), 'SHOES-S-BLACK')


class ShoppingCartTestCase(unittest.TestCase):
    def test_add_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        self.assertDictEqual({'SHOES-S-BLACK': {'quantity': 1}}, cart.products)

    def test_add_two_of_the_same_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.add_product(product)
        self.assertDictEqual({'SHOES-S-BLACK': {'quantity': 2}}, cart.products)

    def test_add_and_remove_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)

    def test_add_and_remove_some_product(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.add_product(product)
        cart.remove_product(product)

        self.assertDictEqual({'SHOES-S-BLACK': {'quantity': 1}}, cart.products)

    def test_add_and_remove_some_product_twice(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.add_product(product)
        cart.remove_product(product)
        cart.remove_product(product)

        self.assertDictEqual({}, cart.products)

    def test_add_and_remove_different_products(self):
        cart = ShoppingCart()
        product_one = Product('shoes', 'S', 'black')
        product_two = Product('jacket', 'M', 'red')

        cart.add_product(product_one)
        cart.add_product(product_two)
        cart.remove_product(product_one)

        self.assertDictEqual({'JACKET-M-RED': {'quantity': 1}}, cart.products)

    def test_remove_too_many_products(self):
        cart = ShoppingCart()
        product = Product('shoes', 'S', 'black')

        cart.add_product(product)
        cart.remove_product(product, 2)

        self.assertDictEqual({}, cart.products)