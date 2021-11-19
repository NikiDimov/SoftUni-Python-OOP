from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    valid_names = ["Biologist", "Geodesist", "Meteorologist"]
    successful_missions = 0
    not_completed_missions = 0
    sent_astronauts = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name):
        if astronaut_type not in self.valid_names:
            raise Exception("Astronaut type is not valid!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."
        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.add(Meteorologist(name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items: str):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."
        new_planet = Planet(name)
        self.planet_repository.add(new_planet)
        new_planet.items = items.split(', ')
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name):
        chosen_ones = {}
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                chosen_ones[astronaut] = astronaut.oxygen
        if not chosen_ones:
            raise Exception("You need at least one astronaut to explore the planet!")
        chosen_ones = dict(sorted(chosen_ones.items(), key=lambda x: -x[1])[:5])
        for astronaut in chosen_ones:
            if not planet.items:
                break
            self.sent_astronauts += 1
            while planet.items and astronaut.oxygen > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
        if not planet.items:
            self.successful_missions += 1
            return f"Planet: {planet.name} was explored. {self.sent_astronauts} " \
                   f"astronauts participated in collecting items."
        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!" \
                 f"\n{self.not_completed_missions} missions were not completed!\nAstronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"{astronaut}\n"
        return result




