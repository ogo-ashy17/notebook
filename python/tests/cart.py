from collections import defaultdict


class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int))

    def add_product(self, product, quantity=1):
        self.products[product.generate_sku()]['quantity'] += quantity

    def remove_product(self, prodeuct, quantity=1):
        sku = prodeuct.generate_sku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] <= 0:
            del self.products[sku]
