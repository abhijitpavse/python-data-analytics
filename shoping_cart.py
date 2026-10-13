# # 12 10 2026


# # Smart Shopping Cart

# # Class 1: Product
# class Product:

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# # Class 2: ShoppingCart
# class ShoppingCart:

#     def __init__(self):
#         self.items = []

#     # Add product to cart
#     def add_item(self, product):
#         self.items.append(product)
#         print(f"Added {product.name} to the cart.")

#     # Remove product from cart
#     def remove_item(self, product_name):

#         for product in self.items:

#             if product.name == product_name:
#                 self.items.remove(product)
#                 print(f"Removed {product_name} from the cart.")
#                 return

#         print("Item not found in cart.")

#     # Calculate total bill
#     def calculate_total(self):

#         total = 0

#         for product in self.items:
#             total += product.price

#         return total

#     # Display cart items
#     def display_cart(self):

#         if len(self.items) == 0:
#             print("Your cart is empty.")
#             return

#         print("\n--- Shopping Cart ---")

#         for product in self.items:
#             print(f"- {product.name}: ${product.price:.2f}")

#         print("---------------------")


# # Create Product objects
# apple = Product("Apple", 0.99)
# milk = Product("Milk", 2.49)
# bread = Product("Bread", 1.99)


# # Create ShoppingCart object
# cart = ShoppingCart()


# # Add products to cart
# cart.add_item(apple)
# cart.add_item(milk)
# cart.add_item(bread)


# # Display shopping cart
# cart.display_cart()


# # Remove Milk from cart
# cart.remove_item("Milk")


# # Calculate and display total bill
# total = cart.calculate_total()

# print(f"Total Bill: ${total:.2f}")




# take user input 

# Smart Shopping Cart

# Class 1: Product
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


# Class 2: ShoppingCart
class ShoppingCart:

    def __init__(self):
        self.items = []

    # Add product to cart
    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    # Remove product from cart
    def remove_item(self, product_name):

        for product in self.items:

            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed {product_name} from the cart.")
                return

        print("Item not found in cart.")

    # Calculate total bill
    def calculate_total(self):

        total = 0

        for product in self.items:
            total += product.price

        return total

    # Display cart items
    def display_cart(self):

        if len(self.items) == 0:
            print("Your cart is empty.")
            return

        print("\n--- Shopping Cart ---")

        for product in self.items:
            print(f"- {product.name}: ${product.price:.2f}")

        print("---------------------")


# Create Shopping Cart
cart = ShoppingCart()


# Take user input for 3 products
for i in range(3):

    print(f"\nEnter details for Product {i + 1}")

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))

    product = Product(name, price)

    cart.add_item(product)


# Display shopping cart
cart.display_cart()


# Ask user which product to remove
remove_product = input("\nEnter product name to remove: ")

cart.remove_item(remove_product)


# Calculate total bill
total = cart.calculate_total()

print(f"Total Bill: ${total:.2f}")