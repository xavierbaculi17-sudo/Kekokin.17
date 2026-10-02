# Handles header, menu listing, and receipt output formatting

from menu import get_menu
from order import calculate_total, calculate_discount

def print_header():
    print("\n" + "=" * 50)
    print("           THE ROAST & BREW")
    print("       ARTISAN COFFEE & BAKERY")
    print("=" * 50)

def print_menu():
    menu = get_menu()
    print("\n" + "-" * 50)
    print("                 DRINKS & BITES")
    print("-" * 50)
    print("{:<8} {:<28} {:>10}".format("CODE", "ITEM", "PRICE"))
    for code, details in menu.items():
        print("{:<8} {:<28} ₱{:>9,.2f}".format(code, details[0], details[1]))
    print("-" * 50)

def print_receipt(orders):
    subtotal = calculate_total(orders)
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    print("\n" + "=" * 60)
    print("           THE ROAST & BREW")
    print("            CUSTOMER RECEIPT")
    print("=" * 60)
    print("{:<25} {:>5} {:>12} {:>12}".format("ITEM", "QTY", "PRICE", "TOTAL"))
    print("-" * 60)
    for code, (name, qty, price) in orders.items():
        print("{:<25} {:>5} ₱{:>10,.2f} ₱{:>10,.2f}".format(name, qty, price, qty * price))
    print("-" * 60)
    print("{:<45} ₱{:>10,.2f}".format("SUBTOTAL:", subtotal))
    print("{:<45} ₱{:>10,.2f}".format("DISCOUNT:", discount))
    print("{:<45} ₱{:>10,.2f}".format("TOTAL DUE:", final_total))
    print("=" * 60)
    print("       Have a wonderful day! See you tomorrow!")
    print("=" * 60)