import unittest
from src.core.use_cases.add_product import AddProduct
from src.core.entities.product import Product

class ProductRepositoryStub:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

class TestAddProduct(unittest.TestCase):
    def setUp(self):
        self.product_repository = ProductRepositoryStub()
        self.add_product_use_case = AddProduct(self.product_repository)

    def test_add_product_successfully(self):
        product_data = {
            "id": "1",
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.0,
            "stock": 100
        }

        self.add_product_use_case.execute(Product(**product_data))

        # Compare mo
        self.assertEqual(len(self.product_repository.products), 1)
        self.assertEqual(self.product_repository.products[0].name, "Test Product")

if __name__ == '__main__':
    unittest.main()