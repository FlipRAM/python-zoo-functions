import json


def get_animal_older_than(specie_name, age):
    with open('zoo_data.json') as data:
        zoo_data = json.load(data)
        species_older_match = []
        for specie in zoo_data["species"]:
            if specie["name"] == specie_name:
                for resident in specie["residents"]:
                    if resident["age"] >= age:
                        species_older_match.append(resident)
        return species_older_match


if __name__ == "__main__":
    print(get_animal_older_than("penguins", 10))
