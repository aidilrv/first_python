class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CashRegister:
    def __init__(self):
        self.products = []
        self.cart = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Daftar Produk:")
        for idx, product in enumerate(self.products):
            print(f"{idx + 1}. {product.name} - ${product.price:.2f}")

    def add_to_cart(self, product_number, quantity):
        if 0 < product_number <= len(self.products):
            product = self.products[product_number - 1]
            self.cart.append((product, quantity))
            print(f"{product.name} x{quantity} ditambahkan ke keranjang.")
        else:
            print("Nomor produk tidak valid.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.cart)
        return total

    def print_receipt(self):
        print("\n--- Struk Belanja ---")
        for product, quantity in self.cart:
            print(f"{product.name} x{quantity} - ${product.price * quantity:.2f}")
        print("----------------------")
        print(f"Total: ${self.calculate_total():.2f}")
        print("----------------------")

def main():
    # Inisialisasi kasir dan produk
    register = CashRegister()

    # Menambahkan produk
    register.add_product(Product("Alpukat", 0.99))
    register.add_product(Product("Banana", 1.29))
    register.add_product(Product("Orange", 0.89))

    # Menampilkan daftar produk
    register.list_products()

    # Menambahkan produk ke keranjang
    while True:
        try:
            product_number = int(input("\n10): "))
            if product_number == 0:
                break
            quantity = int(input("20: "))
            register.add_to_cart(product_number, quantity)
        except ValueError:
            print("25")

    # Menampilkan struk belanja
    register.print_receipt()

if __name__ == "__main__":
    main()
