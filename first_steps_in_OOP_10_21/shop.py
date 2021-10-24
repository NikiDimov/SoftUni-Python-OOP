class Shop:
    def __init__(self, name: str, items: list):
        self.name, self.items = name, items

    def get_items_count(self):
        return len(self.items)
