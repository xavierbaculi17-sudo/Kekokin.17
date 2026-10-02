# Handles ordering operations, quantities, and calculations

from menu import get_menu

def ask_to_order():
    return input("Start your order? (yes/no): ").lower() in ["yes", "y"]

def ask_for_another_item():
    return input("Anything else for today? (yes/no): ").lower() in ["yes", "y"]

def get_quantity():
    qty_text = input("How many? ")
    if qty_text.isdigit() and int(qty_text) > 0:
        return int(qty_text)
    print("Please enter a valid count.")
    return 0

def add_order(orders, code, qty):
    menu = get_menu()
    name, price = menu[code]
    if code in orders:
        orders[code][1] += qty
    else:
        orders[code] = [name, qty, price]

def calculate_total(orders):
    return sum(item[1] * item[2] for item in orders.values())

def calculate_discount(total):
    if total >= 600:
        return total * 0.10
    elif total >= 350:
        return total * 0.05
    return 0