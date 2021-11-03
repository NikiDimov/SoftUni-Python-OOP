class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget:
            return "Not enough budget"
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if not len(self.workers) >= self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        current_sum = 0
        for worker in self.workers:
            current_sum += worker.salary
        if current_sum <= self.__budget:
            self.__budget -= current_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        current_sum = 0
        for animal in self.animals:
            current_sum += animal.money_for_care
        if current_sum <= self.__budget:
            self.__budget -= current_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]
        result += self.output(lions, "Lions")
        result += self.output(tigers, "Tigers")
        result += self.output(cheetahs, "Cheetahs")
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]
        result += self.output(keepers, "Keepers")
        result += self.output(caretakers, "Caretakers")
        result += self.output(vets, "Vets")
        return result.strip()

    def output(self, sequence, name):
        result = ''
        result += f"----- {len(sequence)} {name}:\n"
        for instance in sequence:
            result += f"{instance}\n"
        return result
