from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if car_type == "MuscleCar" or car_type == "SportsCar":
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")
            if car_type == "MuscleCar":
                self.cars.append(MuscleCar(model, speed_limit))
            elif car_type == "SportsCar":
                self.cars.append(SportsCar(model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver_exist = False
        available_car = False
        current_driver = None
        current_car = None
        for driver in self.drivers:
            if driver.name == driver_name:
                driver_exist = True
                current_driver = driver
                break
        if not driver_exist:
            raise Exception(f"Driver {driver_name} could not be found!")
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                available_car = True
                current_car = car
                break
        if not available_car:
            raise Exception(f"Car {car_type} could not be found!")
        if current_driver.car:
            current_driver.car.is_taken = False
            old_model = current_driver.car.model
            new_model = current_car.model
            current_driver.car = current_car
            current_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."
        current_driver.car = current_car
        current_car.is_taken = True
        return f"Driver {driver_name} chose the car {current_car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race_exists = False
        driver_exists = False
        current_race = None
        current_driver = None
        for race in self.races:
            if race.name == race_name:
                race_exists = True
                current_race = race
                break
        if not race_exists:
            raise Exception(f"Race {race_name} could not be found!")
        for driver in self.drivers:
            if driver.name == driver_name:
                driver_exists = True
                current_driver = driver
                break
        if not driver_exists:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not current_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        for driver in current_race.drivers:
            if driver.name == driver_name:
                return f"Driver {driver_name} is already added in {race_name} race."
        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race_exists = False
        current_race = None
        all_drivers = {}
        for race in self.races:
            if race.name == race_name:
                race_exists = True
                current_race = race
                break
        if not race_exists:
            raise Exception(f"Race {race_name} could not be found!")
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        for driver in current_race.drivers:
            all_drivers[driver] = driver.car.speed_limit
        all_drivers = list(dict(sorted(all_drivers.items(), key=lambda x: -x[1])))[:3]
        result = ''
        for driver in all_drivers:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
        return result.strip()





# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]

