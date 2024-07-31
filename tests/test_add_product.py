import unittest
from src.core.use_cases.add_product import AddProduct
from unittest.mock import Mock

class TestAddProduct(unittest.TestCase):
    def setUp(self):
        self.product_repository = Mock()
        self.add_product_use_case = AddProduct(self.product_repository)

    def test_add_product_successfully(self):
        product_data = {
            "id": "1",
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.0,
            "inventory_quantity": 100
        }

        self.add_product_use_case.execute(product_data)
        self.product_repository.add_product.assert_called_once()

if __name__ == '__main__':
    unittest.main()