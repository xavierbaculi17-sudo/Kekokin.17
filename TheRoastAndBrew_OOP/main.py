# Entry point using OOP classes to run the program workflow

from coffee_shop import CoffeeShop, OrderManager

def main():
    shop = CoffeeShop()
    order_mgr = OrderManager(shop)

    shop.display_header()
    shop.display_menu()

    start = input("Start your order? (yes/no): ").lower() in ["yes", "y"]
    if start:
        ordering = True
        while ordering:
            code = input("Enter item code: ").upper()
            if shop.is_valid_code(code):
                qty_text = input("How many? ")
                if qty_text.isdigit() and int(qty_text) > 0:
                    order_mgr.add_item(code, int(qty_text))
                    ordering = input("Anything else for today? (yes/no): ").lower() in ["yes", "y"]
                else:
                    print("Please enter a valid count.")
            else:
                print("Code not found. Please select an item from the menu list.")

        if order_mgr.orders:
            order_mgr.print_receipt()
        else:
            print("No order placed.")
    else:
        print("\nHave a great day!")

if __name__ == "__main__":
    main()