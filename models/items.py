class item:
    def __init__(self, name, tier, description):
        self.name = name
        self.tier = tier
        self.description = description

    def __str__(self):
        return f"{(self.name).upper()}\nTier\t\t: {self.tier}\nDeskription\t: {self.description}"

class Inventory:
    def __init__(self):
        self.list = []

    def add_item(self, new_item):
        if isinstance(new_item, item):
            self.list.append(new_item)
        else:
            print("New Item is not defined")

    def view_item(self):
        if self.list:
            for i in self.list:
                print(i)
        else:
            print("Inventory is empty")

# fire_sword = item("Fire Sword", "Heaven", "A Sword that can burn a city")
