class Car:
    def __init__(self, name, model, engine):
        self.name, self.model, self.engine = name, model, engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"
