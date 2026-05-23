class Product:
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__ (self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} has been added to the inventory.")
        
    def show_all_products(self):
        print("Products in Inventory:")
        for product in self.products:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            
    def calculate_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value
    
product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.show_all_products()
total_value = inventory.calculate_total_value()
print(f"Total value of inventory: {total_value}")