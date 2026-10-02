# Defines the classes and methods representing shop operations and customer orders

class CoffeeShop:
    def __init__(self):
        self.menu = {
            "C1": ["Espresso", 90],
            "C2": ["Caffè Latte", 130],
            "C3": ["Caramel Macchiato", 150],
            "C4": ["Iced Matcha Latte", 160],
            "C5": ["Butter Croissant", 85],
            "C6": ["Blueberry Muffin", 95],
            "C7": ["Avocado Toast", 180]
        }

    def display_header(self):
        print("\n" + "=" * 50)
        print("           THE ROAST & BREW")
        print("       ARTISAN COFFEE & BAKERY")
        print("=" * 50)

    def display_menu(self):
        print("\n" + "-" * 50)
        print("                 DRINKS & BITES")
        print("-" * 50)
        print("{:<8} {:<28} {:>10}".format("CODE", "ITEM", "PRICE"))
        for code, details in self.menu.items():
            print("{:<8} {:<28} ₱{:>9,.2f}".format(code, details[0], details[1]))
        print("-" * 50)

    def is_valid_code(self, code):
        return code in self.menu


class OrderManager:
    def __init__(self, shop):
        self.shop = shop
        self.orders = {}

    def add_item(self, code, qty):
        name, price = self.shop.menu[code]
        if code in self.orders:
            self.orders[code]["qty"] += qty
        else:
            self.orders[code] = {"name": name, "qty": qty, "price": price}

    def calculate_subtotal(self):
        return sum(item["qty"] * item["price"] for item in self.orders.values())

    def calculate_discount(self, total):
        if total >= 600:
            return total * 0.10
        elif total >= 350:
            return total * 0.05
        return 0

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        final_total = subtotal - discount

        print("\n" + "=" * 60)
        print("           THE ROAST & BREW")
        print("            CUSTOMER RECEIPT")
        print("=" * 60)
        print("{:<25} {:>5} {:>12} {:>12}".format("ITEM", "QTY", "PRICE", "TOTAL"))
        print("-" * 60)

        for details in self.orders.values():
            name = details["name"]
            qty = details["qty"]
            price = details["price"]
            print("{:<25} {:>5} ₱{:>10,.2f} ₱{:>10,.2f}".format(name, qty, price, qty * price))

        print("-" * 60)
        print("{:<45} ₱{:>10,.2f}".format("SUBTOTAL:", subtotal))
        print("{:<45} ₱{:>10,.2f}".format("DISCOUNT:", discount))
        print("{:<45} ₱{:>10,.2f}".format("TOTAL DUE:", final_total))
        print("=" * 60)
        print("       Have a wonderful day! See you tomorrow!")
        print("=" * 60)