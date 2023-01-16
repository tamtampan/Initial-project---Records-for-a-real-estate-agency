from abc import ABC


class Person(ABC):

    def __init__(self, name: str, surname: str, person_id: str,
                 address: str, city: str, state: str, phone: str) -> None:
        self.name = name
        self.surname = surname
        self.person_id = person_id
        self.address = address
        self.city = city
        self.state = state
        self.phone = phone
