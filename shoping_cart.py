# # # 12 10 2026


# # # Smart Shopping Cart

# # # Class 1: Product
# # class Product:

# #     def __init__(self, name, price):
# #         self.name = name
# #         self.price = price


# # # Class 2: ShoppingCart
# # class ShoppingCart:

# #     def __init__(self):
# #         self.items = []

# #     # Add product to cart
# #     def add_item(self, product):
# #         self.items.append(product)
# #         print(f"Added {product.name} to the cart.")

# #     # Remove product from cart
# #     def remove_item(self, product_name):

# #         for product in self.items:

# #             if product.name == product_name:
# #                 self.items.remove(product)
# #                 print(f"Removed {product_name} from the cart.")
# #                 return

# #         print("Item not found in cart.")

# #     # Calculate total bill
# #     def calculate_total(self):

# #         total = 0

# #         for product in self.items:
# #             total += product.price

# #         return total

# #     # Display cart items
# #     def display_cart(self):

# #         if len(self.items) == 0:
# #             print("Your cart is empty.")
# #             return

# #         print("\n--- Shopping Cart ---")

# #         for product in self.items:
# #             print(f"- {product.name}: ${product.price:.2f}")

# #         print("---------------------")


# # # Create Product objects
# # apple = Product("Apple", 0.99)
# # milk = Product("Milk", 2.49)
# # bread = Product("Bread", 1.99)


# # # Create ShoppingCart object
# # cart = ShoppingCart()


# # # Add products to cart
# # cart.add_item(apple)
# # cart.add_item(milk)
# # cart.add_item(bread)


# # # Display shopping cart
# # cart.display_cart()


# # # Remove Milk from cart
# # cart.remove_item("Milk")


# # # Calculate and display total bill
# # total = cart.calculate_total()

# # print(f"Total Bill: ${total:.2f}")




# # take user input 

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


# # Create Shopping Cart
# cart = ShoppingCart()


# # Take user input for 3 products
# for i in range(3):

#     print(f"\nEnter details for Product {i + 1}")

#     name = input("Enter product name: ")
#     price = float(input("Enter product price: "))

#     product = Product(name, price)

#     cart.add_item(product)


# # Display shopping cart
# cart.display_cart()


# # Ask user which product to remove
# remove_product = input("\nEnter product name to remove: ")

# cart.remove_item(remove_product)


# # Calculate total bill
# total = cart.calculate_total()

# print(f"Total Bill: ${total:.2f}")











# Smart Shopping Cart

# -----------------------------------
# Class 1: Product
# -----------------------------------

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


# -----------------------------------
# Class 2: ShoppingCart
# -----------------------------------

class ShoppingCart:

    def __init__(self):
        self.items = []


    # Add product to cart
    def add_item(self, product, quantity):

        # Check if product already exists in cart
        for item in self.items:

            if item["product"].name == product.name:

                item["quantity"] += quantity

                print(
                    f"\nAdded {quantity} more {product.name}(s) to the cart."
                )

                return

        # If product is not already in cart
        self.items.append({
            "product": product,
            "quantity": quantity
        })

        print(
            f"\nAdded {quantity} {product.name}(s) to the cart."
        )


    # Remove product or quantity
    def remove_item(self, product_name, quantity):

        for item in self.items:

            if item["product"].name.lower() == product_name.lower():

                # If quantity to remove is less than cart quantity
                if quantity < item["quantity"]:

                    item["quantity"] -= quantity

                    print(
                        f"\nRemoved {quantity} {item['product'].name}(s) "
                        f"from the cart."
                    )

                # If quantity to remove is equal to cart quantity
                elif quantity == item["quantity"]:

                    self.items.remove(item)

                    print(
                        f"\nRemoved {item['product'].name} from the cart."
                    )

                # If user tries to remove more than available
                else:

                    print(
                        f"\nYou only have {item['quantity']} "
                        f"{item['product'].name}(s) in the cart."
                    )

                return

        print("\nItem not found in cart.")


    # Display cart
    def display_cart(self):

        if len(self.items) == 0:

            print("\nYour cart is empty.")
            return

        print("\n--- Shopping Cart ---")

        total = 0

        for item in self.items:

            product = item["product"]
            quantity = item["quantity"]

            item_total = product.price * quantity

            total += item_total

            print(
                f"- {product.name}: "
                f"${product.price:.2f} x {quantity} "
                f"= ${item_total:.2f}"
            )

        print("---------------------")
        print(f"Current Total: ${total:.2f}")


    # Calculate total bill
    def calculate_total(self):

        total = 0

        for item in self.items:

            product = item["product"]
            quantity = item["quantity"]

            total += product.price * quantity

        return total


# -----------------------------------
# SHOP INVENTORY
# -----------------------------------

shop_products = [

    Product("Apple", 0.99),
    Product("Milk", 2.49),
    Product("Bread", 1.99),
    Product("Eggs", 3.49),
    Product("Rice", 5.99),
    Product("Sugar", 2.99),
    Product("Coffee", 4.99),
    Product("Tea", 3.99),
    Product("Butter", 4.49),
    Product("Cheese", 6.99)
]


# -----------------------------------
# Create Shopping Cart
# -----------------------------------

cart = ShoppingCart()


# -----------------------------------
# Display Shop Menu
# -----------------------------------

print("================================")
print("       WELCOME TO SHOP")
print("================================")

print("\nAvailable Products:\n")

for i in range(len(shop_products)):

    product = shop_products[i]

    print(
        f"{i + 1}. {product.name:<10} "
        f"${product.price:.2f}"
    )


# -----------------------------------
# Shopping Loop
# -----------------------------------

while True:

    print("\n================================")
    print("           SHOP MENU")
    print("================================")

    print("1. Add Item to Cart")
    print("2. Remove Item from Cart")
    print("3. Display Cart")
    print("4. Stop Shopping")

    choice = input("\nEnter your choice: ")


    # -----------------------------------
    # ADD ITEM
    # -----------------------------------

    if choice == "1":

        print("\nAvailable Products:")

        for i in range(len(shop_products)):

            product = shop_products[i]

            print(
                f"{i + 1}. {product.name:<10} "
                f"${product.price:.2f}"
            )


        product_choice = input(
            "\nEnter product number: "
        )


        # Check whether input is a number
        if not product_choice.isdigit():

            print("\nInvalid product choice.")
            continue


        product_choice = int(product_choice)


        # Check whether product exists
        if product_choice < 1 or product_choice > len(shop_products):

            print("\nItem not available.")
            continue


        # Get selected product
        selected_product = shop_products[product_choice - 1]


        # Ask quantity
        quantity = input(
            f"Enter quantity of {selected_product.name}: "
        )


        if not quantity.isdigit():

            print("\nInvalid quantity.")
            continue


        quantity = int(quantity)


        if quantity <= 0:

            print("\nQuantity must be greater than 0.")
            continue


        # Add product to cart
        cart.add_item(
            selected_product,
            quantity
        )


        # Show cart after adding
        cart.display_cart()


        # Ask whether user wants to continue
        continue_shopping = input(
            "\nDo you want to continue shopping? (y/n): "
        ).lower()


        if continue_shopping == "n":

            break


    # -----------------------------------
    # REMOVE ITEM
    # -----------------------------------

    elif choice == "2":

        if len(cart.items) == 0:

            print("\nYour cart is empty.")
            continue


        # Display current cart
        cart.display_cart()


        product_name = input(
            "\nEnter product name to remove: "
        )


        quantity = input(
            "Enter quantity to remove: "
        )


        if not quantity.isdigit():

            print("\nInvalid quantity.")
            continue


        quantity = int(quantity)


        if quantity <= 0:

            print("\nQuantity must be greater than 0.")
            continue


        cart.remove_item(
            product_name,
            quantity
        )


        # Display updated cart
        cart.display_cart()


    # -----------------------------------
    # DISPLAY CART
    # -----------------------------------

    elif choice == "3":

        cart.display_cart()


    # -----------------------------------
    # STOP SHOPPING
    # -----------------------------------

    elif choice == "4":

        break


    # -----------------------------------
    # INVALID MENU CHOICE
    # -----------------------------------

    else:

        print("\nInvalid choice. Please select 1-4.")


# -----------------------------------
# FINAL BILL
# -----------------------------------

print("\n================================")
print("          FINAL BILL")
print("================================")

cart.display_cart()

total = cart.calculate_total()

print(f"\nTotal Bill: ${total:.2f}")

print("\nThank you for shopping!")