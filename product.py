class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def display_info(self):
        print(f'Product Name: {self.name}, Product Price: {self.price}, Product Quantity: {self.quantity}')
    
    def update_quantity(self, amount):
        if self.quantity + amount >= 0:
            print('Error: Negative quantity in stock. Check previous updates.')
        else:
            self.quantity += amount
    
    def __str__(self):
        return f'{self.name} - {self.price:.2f} - {self.quantity} '

        