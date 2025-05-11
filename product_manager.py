from product import Product
class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f' - Product {product.name} was added')
    
    def display_info(self):
        if not self.products:
            print('Error: no products available')       
        print('Product List: ')
        for product in self.products:
            print(f' - {product}')

    def suma_total(self):
        total = sum(produs.price for produs in self.products)
        print(f'Total value: {total:.2f} Euros')
        return total
    
    def remove_product_by_name(self, name):
        self.products = [p for p in self.products if p.name != name]

        
        
    

            