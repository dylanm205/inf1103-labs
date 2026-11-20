import unittest
from supplier import Supplier
from product_factory import ProductFactory
from order import Order
from order_line import OrderLine
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount
from inventory import Inventory
from product_loader import load_products


class TestInventorySystem(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Tech Pte Ltd", "sales@tech.com")
        self.chair = ProductFactory.create("physical", "P001", "Chair", 50.00, 20, self.supplier, 5.0)

    # Strategy pattern
    def test_bulk_discount(self):
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(self.chair, 5)
        self.assertEqual(order.calculate_total(), 230.0)

    def test_set_discount(self):
        order = Order("O001", BulkDiscount(200, 20))
        order.add_order_line(self.chair, 5)
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225.0)

    def test_student_discount(self):
        order = Order("O001", StudentDiscount())
        order.add_order_line(self.chair, 5)
        self.assertEqual(order.calculate_total(), 237.5)

    # Factory pattern
    def test_factory_creates_product(self):
        lamp = ProductFactory.create("physical", "P002", "Lamp", 25.00, 10, self.supplier, 1.2)
        self.assertEqual(lamp.get_product_id(), "P002")

    def test_factory_unknown_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Installation", 30.00, 5, self.supplier)

    # Validation
    def test_price_must_be_positive(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P003", "Free", 0, 5, self.supplier)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P004", "Box", 10.00, -1, self.supplier)

    def test_order_quantity_must_be_positive(self):
        with self.assertRaises(ValueError):
            OrderLine(self.chair, 0)

    # Exception handling
    def test_bad_rows_skipped(self):
        inventory = Inventory()
        load_products("products.csv", inventory, self.supplier)
        self.assertEqual(len(inventory.get_products()), 3)

    def test_missing_file(self):
        inventory = Inventory()
        load_products("missing.csv", inventory, self.supplier)
        self.assertEqual(len(inventory.get_products()), 0)


if __name__ == "__main__":
    unittest.main()