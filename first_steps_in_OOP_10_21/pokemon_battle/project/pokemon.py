class Pokemon:
    def __init__(self, name, health):
        self.name, self.health = name, health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"
