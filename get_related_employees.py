import json


def check_if_manager(id):
    with open('zoo_data.json') as data:
        zoo_data = json.load(data)
        is_manager = False
        for employee in zoo_data["employees"]:
            if employee["id"] == id and len(employee["managers"]) <= 1:
                is_manager = True
        return is_manager


def get_related_employees(id):
    is_manager = check_if_manager(id)
    related_people = []
    if is_manager is True:
        with open('zoo_data.json') as data:
            zoo_data = json.load(data)
            for employee in zoo_data["employees"]:
                for manager in employee["managers"]:
                    if (manager == id):
                        related_people.append(
                          f'{employee["firstName"]} {employee["lastName"]}'
                        )
    return related_people


if __name__ == "__main__":
    print(get_related_employees("0e7b460e-acf4-4e17-bcb3-ee472265db83"))
