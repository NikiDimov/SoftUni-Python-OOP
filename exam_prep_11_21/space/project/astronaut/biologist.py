from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    oxygen_units = 5

    def __init__(self, name):
        super().__init__(name, oxygen=70)


