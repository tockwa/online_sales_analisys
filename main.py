from product_manager import ProductManager
from product import Product
from Cart import Cart

manager = ProductManager()

product1 = Product('Gaming Keyboards', 200, 10)
product2 = Product('Gaming Mouse', 500, 20)
product3 = Product('Gaming Monitor', 1500, 34)


manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)


manager.display_info()
manager.suma_total()

print()

cartlist = Cart()
products1 = Product('Mobile Iphone', 15000, 100)
products2 = Product('Mobile Samsung', 12000, 200)
products3 = Product('Mobile Xiaomi', 5400, 130)

cartlist.add_products(products1)
cartlist.add_products(products2)
cartlist.add_products(products3)

cartlist.products_list()
cartlist.display_rezult()


