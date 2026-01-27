import json

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        item = item.lower()
        self.items[item] = self.items.get(item, 0) + quantity

    def remove_item(self, item, quantity):
        if item in self.items:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                del self.items[item]

    def display_inventory(self):
        print("Inventory:")
        if not self.items:
            print("Empty")
        for item, qty in self.items.items():
            print(f"- {item}: {qty}")
