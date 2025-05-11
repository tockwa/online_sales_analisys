from product_manager import ProductManager
from product import Product

manager = ProductManager()

product1 = Product('Gaming Keyboards', 200, 10)
product2 = Product('Gaming Mouse', 500, 20)
product3 = Product('Gaming Monitor', 1500, 34)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)


manager.display_info()
manager.suma_total()