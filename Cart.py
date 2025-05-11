class Cart:    
    def __init__(self, ):
        self.cart_items = []

    def add_products(self, products):
        self.cart_items.append(products)
        print(f' - Produsul {products.name} a fost adaugat')
    
    def display_rezult(self):
        total = sum(product.price for product in self.cart_items)
        print(f' - Valoarea tootala a prduselor: {total}')
        return total

    def products_list(self):
        print('Lista Produselor: ')
        for products in self.cart_items:
            print(f'{products}')
        if not self.cart_items:
            print('Error: no products available')


