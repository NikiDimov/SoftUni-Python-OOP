class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif price > self.__budget and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
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
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needs = 0
        for animal in self.animals:
            total_needs += animal.get_needs()
        if total_needs <= self.__budget:
            self.__budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        res = f"You have {len(self.animals)} animals"
        for animal in self.animals:
            animal_dict[animal.__class__.__name__].append(str(animal))
        for key, value in animal_dict.items():
            res += f"\n----- {len(animal_dict[key])} {key}s:\n"
            res += '\n'.join(value)
        return res

    def workers_status(self):
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}
        res = f"You have {len(self.workers)} workers"
        for worker in self.workers:
            workers_dict[worker.__class__.__name__].append(str(worker))
        for key, value in workers_dict.items():
            res += f"\n----- {len(workers_dict[key])} {key}s:\n"
            res += '\n'.join(value)
        return res
