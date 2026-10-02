# Controls program execution workflow

from display import print_header, print_menu, print_receipt
from order import ask_to_order, get_quantity, add_order, ask_for_another_item
from menu import get_menu_item

def main():
    orders = {}
    print_header()
    print_menu()

    if ask_to_order():
        ordering = True
        while ordering:
            item_code = get_menu_item()
            if item_code:
                qty = get_quantity()
                if qty > 0:
                    add_order(orders, item_code, qty)
                    ordering = ask_for_another_item()

        if orders:
            print_receipt(orders)
        else:
            print("No order placed.")
    else:
        print("\nHave a great day!")

if __name__ == "__main__":
    main()