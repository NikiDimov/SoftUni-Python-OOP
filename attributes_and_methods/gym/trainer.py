class Trainer:
    id = 0

    def __init__(self, name):
        Trainer.id += 1
        self.name = name
        self.id = Trainer.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Trainer.id + 1

