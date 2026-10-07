import json
import os

inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]

# inventory = []
transactions = []
Failed = 0


def display_all():
    print("\nCurrent Inventory")
    print("-" * 50)

    for item in inventory:
        print(
            f"ID: {item["id"]} | "
            f"Name: {item["name"]} | "
            f"Price: ${item["price"]:.2f} | "
            f"Stock: {item["stock"]}"
        )

    print("-" * 50)

def add_product():
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")

    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)

    print("Product added successfully!")

def update_stock():
    product_id = input("Enter Product ID: ")

    for item in inventory:
        if item["id"] == product_id:

            print("\nProduct Found:")
            print("Name:", item["name"])
            print("Current Stock:", item["stock"])

            new_stock = int(input("\nNew Stock Quantity: "))

            item["stock"] = new_stock

            transactions.append(new_stock)

            print("\nStock updated successfully!")
            return

    print("Product not found.")

def search_product():
    product_id = input("Enter Product ID: ")

    for item in inventory:
        if item["id"] == product_id:

            print("\nProduct Found")
            print("-" * 30)
            print("ID:", item["id"])
            print("Name:", item["name"])
            print("Price:", item["price"])
            print("Stock:", item["stock"])
            print("-" * 30)

            return

    print("Product not found.")

# def load_inventory():
#     global inventory
#     try:
#         with open("inventory.json", "r") as file:
#             inventory = json.load(file)
            
#         print("Loaded inventory from file:")
#         print("Inventory loaded successfully")
#     except FileNotFoundError:
#         inventory = []
#         print("Inventory file not found. Starting with empty inventory.")
        

def save_inventory():
    global inventory, transactions
    data = {
        "inventory" : inventory,
        "transactions" : transactions
    }
    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Order successfully saved to inventory.json")

def get_valid_Input():
    global Failed
    stock = input("Please enter the stock quantity (or 'quit' to exit): ")
    if stock == "quit":
        return stock
    elif not stock.isdigit():
        print("Invalid stock quantity. Please enter again.")
        Failed += 1
        return None
    else:
        return int(stock)

def process_quantity(product_name, quantity):
    global inventory, transactions
    order_id = 1000 + len(inventory) + 1
    order = f"{order_id}, {product_name}, {quantity}"
    inventory.append(order)
    transactions.append(quantity)
    print("\nNew Order Added:")
    print(order)
    return inventory

def generate_report():
    print("Current Orders:")
    for item in inventory:
        print(item)
    print("Number of Failed/Rejected Entries:", Failed)
    print("Transaction History:", transactions)

# ---------------- MAIN PROGRAM ----------------

while True:
    print("--------------Menu--------------")
    print("1. Display All Products")
    print("2. Add New Product")
    print("3. Update Stock Quantity")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("--------------------------------")
    product_name = input("\nEnter option: ")
    if product_name == "1":
        display_all()
    elif product_name == "2":
        add_product()
    elif product_name == "3":
        update_stock()
    elif product_name == "4":
        search_product()
    elif product_name == "5":
        save_inventory()
    elif product_name == "6":
        print("Saving inventory before exit.....")
        save_inventory()
        generate_report()
        save_inventory()
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    # stock_quantity = get_valid_Input()
    # if stock_quantity == "quit":
    #     generate_report()
    #     save_inventory()
    #     break
    # if stock_quantity is not None:
    #     process_quantity(product_name, stock_quantity)
