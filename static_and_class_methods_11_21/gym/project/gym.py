class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subs = None
        cust = None
        train = None
        equip = None
        exercise = None
        for subscription in self.subscriptions:
            if subscription.id == subscription_id:
                subs = subscription
                for customer in self.customers:
                    if customer.id == subscription.customer_id:
                        cust = customer
                for trainer in self.trainers:
                    if trainer.id == subscription.trainer_id:
                        train = trainer
                for plan in self.plans:
                    if plan.id == subscription.exercise_id:
                        exercise = plan
                        for equipment in self.equipment:
                            if equipment.id == plan.equipment_id:
                                equip = equipment
        instances = [subs, cust, train, equip, exercise]
        result = ''
        for instance in instances:
            result += f"{instance}\n"
        return result








