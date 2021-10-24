from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result += f"- {p.pokemon_details()}\n"
        return result.strip()


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
