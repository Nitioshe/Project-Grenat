class CraftingSystem:
    def __init__(self):
        self.recipes = {
            "Health Potion": {"Slime Gall": 1, "Water": 1, "Bottle": 1}
        }

    def list_possible_craft(self, inventory):
        possible = []
        for recipe, items in self.recipes.items():
            if all(inventory.get(i.lower(), 0) >= q for i, q in items.items()):
                possible.append(recipe)
        return possible
