inventory = 0
Failed = 0


def get_valid_Input():
    global Failed
    stock = input("Please enter the stock quantity: ")
    if stock == "quit":
        return stock
    elif not stock.isdigit():
        print("Invalid stock quantity. Please enter again.")
        Failed += 1
        return None
    else:
        return int(stock)

def process_quantity(current_total, new_value):
        if isinstance(new_value, int):
                current_total += new_value
                print("Current Stock Quantity:", current_total)
        return current_total

def calculate_tax(inventory):
    tax_rate = 0.1  # 10% tax rate
    tax = inventory * tax_rate
    return tax

def generate_report(total_units, Failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", Failed_attempts, "units")
    tax = calculate_tax(total_units)
    print("Total Tax on Inventory:", tax)
# while stock != "quit":   
#     if not stock.isdigit():
#         print("Invalid stock quantity. Please enter again.")
#         Failed += 1
#         print("Number of Failed/Rejected Entries:", Failed, "units")
#     else:
#         inventory += int(stock)
#         print("Current Stock Quantity:", inventory)
#     if inventory > 500:
#         print("Inventory is exceeded.")
#         break
#     if inventory == 500:
#         print("Maximum inventory reached. No more stock can be added.")
#         break
#     stock = input("Please enter the stock quantity:")

# print("Total Units Processed:", inventory)
# print ("Number of Failed/Rejected Entries:", Failed, "units")

while True:
    stock_quantity = get_valid_Input()
    if stock_quantity == "quit":
        generate_report(inventory, Failed)
        break
    if stock_quantity is not None:
        inventory = process_quantity(inventory, stock_quantity)
    if inventory > 500:
        print("Inventory is exceeded.")
        generate_report(inventory, Failed)
        break
    if inventory == 500:
        print("Maximum inventory reached. No more stock can be added.")
        generate_report(inventory, Failed)
        break