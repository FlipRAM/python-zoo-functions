import json


def get_employee_by_name(name):
    with open('zoo_data.json') as data:
        zoo_data = json.load(data)
        for employee in zoo_data["employees"]:
            if (
              employee["firstName"].lower() == name.lower() or
              employee["lastName"].lower() == name.lower()
            ):
                return employee


if __name__ == "__main__":
    print(f'Case first name\n {get_employee_by_name("Burl")}')
    print(f'Case first name lowered\n {get_employee_by_name("burl")}')
    print(f'Case last name\n {get_employee_by_name("Nelson")}')
    print(f'Case last name lowered\n {get_employee_by_name("nelson")}')
