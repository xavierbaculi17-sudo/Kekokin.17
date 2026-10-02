# Stores the menu dictionary and related item fetching/validation functions

MENU = {
    "C1": ["Espresso", 90],
    "C2": ["Caffè Latte", 130],
    "C3": ["Caramel Macchiato", 150],
    "C4": ["Iced Matcha Latte", 160],
    "C5": ["Butter Croissant", 85],
    "C6": ["Blueberry Muffin", 95],
    "C7": ["Avocado Toast", 180]
}

def get_menu():
    return MENU

def get_menu_item():
    code = input("Enter item code: ").upper()
    if code in MENU:
        return code
    print("Code not found. Please select an item from the menu list.")
    return ""