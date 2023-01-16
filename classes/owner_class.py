from classes.person_class import Person
import json


class Owner(Person):
    def __init__(self, name: str, surname: str, person_id: str, address: str, city: str, state: str, phone: str) -> None:
        super().__init__(name=name, surname=surname, person_id=person_id, address=address, city=city,
                         state=state, phone=phone)

    def serialization(self) -> str:
        string_to_write = f"OWNER\n{self.person_id}\n"
        string_to_write += json.dumps(self.__dict__, sort_keys=True, default=str)
        return string_to_write + "\n\n"

    def __str__(self) -> str:
        return f"{self.name.title()} {self.surname.title()} - {self.phone}, {self.address}" \
               f" {self.city} {self.state}"

    @staticmethod
    def deserialization(string_from_file: str) -> "Owner":
        return Owner(**json.loads(string_from_file))

    @staticmethod
    def find_by_id(person_id: str) -> "Owner":
        with open("Owners.txt") as file:
            line = file.readline()
            while line:
                if line == "OWNER\n":
                    line = file.readline()
                    if line == (person_id + "\n"):
                        line = file.readline()
                        return Owner.deserialization(line)
                else:
                    line = file.readline()

    @staticmethod
    def add_new_owner(owner_id: str) -> None:
        name = input("Name: ")
        surname = input("Surname: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        phone = input("Phone number: ")
        owner = Owner(name, surname, owner_id, address, city, state, phone)
        with open("Owners.txt", "a") as file:
            file.write(owner.serialization())
        print("Owner successfully added to system.")

    @staticmethod
    def remove_owner_by_id(owner_id: str) -> None:
        with open("Owners.txt") as file:
            lines = file.read()
        lines = lines.split("\n")

        for index, line in enumerate(lines):
            if line == owner_id:
                line_index = index
        try:
            del lines[line_index - 1: line_index + 3]
            with open("Owners.txt", "w") as file:
                for line in lines:
                    line += "\n"
                    file.write(line)
        except Exception as e:
            print(e)
