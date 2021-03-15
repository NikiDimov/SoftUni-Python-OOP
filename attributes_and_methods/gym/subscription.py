class Subscription:
    id = 0

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        Subscription.id += 1
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.id

    @staticmethod
    def get_next_id():
        return Subscription.id + 1

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
