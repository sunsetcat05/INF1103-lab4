inventory = []
transactions = []
Failed = 0

def load_inventory():
    global inventory
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
            inventory = [line.strip() for line in lines if line.strip()]
            print("Loaded inventory from file:")
            for item in inventory:
                print(item)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")
        inventory = []

def save_inventory():
    global inventory, transactions
    with open("inventory.txt", "w") as file:
        for item in inventory:
            file.write(item + "\n")
        file.write("\nTransaction History:\n")
        for t in transactions:
            file.write(str(t) + "\n")
    print("Order successfully saved to inventory.txt")

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
load_inventory()

while True:
    product_name = input("\nEnter Product Name (or 'quit' to exit): ")
    if product_name.lower() == "quit":
        generate_report()
        save_inventory()
        break

    stock_quantity = get_valid_Input()
    if stock_quantity == "quit":
        generate_report()
        save_inventory()
        break
    if stock_quantity is not None:
        process_quantity(product_name, stock_quantity)
