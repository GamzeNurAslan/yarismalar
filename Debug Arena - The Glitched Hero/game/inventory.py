class Inventory:
    def __init__(self, max_slots=3):
        self.max_slots = max_slots
        self.items = []

    def add_item(self, item):
        for existing in self.items:
            if existing.name == item.name:
                existing.uses += item.uses
                return True
        if len(self.items) < self.max_slots:
            self.items.append(item)
            return True
        return False

    def expand_slot(self):
        self.max_slots += 1

    def show(self):
        print(f"\n  Envanter  ({len(self.items)}/{self.max_slots} slot):")
        if not self.items:
            print("  [Boş]")
            return
        for i, item in enumerate(self.items):
            print(f"    {i + 1}. {item}")

    def remove_empty(self):
        self.items = [item for item in self.items if item.uses > 0]

    def has_items(self):
        return len(self.items) > 0