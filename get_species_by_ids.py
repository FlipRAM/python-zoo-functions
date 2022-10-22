import json


def get_species_by_ids(id_list):
    with open('zoo_data.json') as data:
        zoo_data = json.load(data)
        species_match = []
        for id in id_list:
            for specie in zoo_data["species"]:
                if specie["id"] == id:
                    species_match.append(specie)
        return species_match


if __name__ == "__main__":
    print(get_species_by_ids(
      [
        '0938aa23-f153-4937-9f88-4858b24d6bce',
        '89be95b3-47e4-4c5b-b687-1fabf2afa274',
      ]
    ))
