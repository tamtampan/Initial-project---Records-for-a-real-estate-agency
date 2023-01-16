import os
import json
from abc import ABC, abstractmethod

from classes.owner_class import Owner
from classes.agency_class import Agency

PATH = os.getcwd()


class Contract(ABC):
    def __init__(self, owner: Owner, agency: Agency, date: str, property_id: str) -> None:
        self.agency_name = agency.name
        self.agency_boss_name = agency.boss_name
        self.agency_boss_surname = agency.boss_surname
        self.agency_address = agency.address
        self.agency_city = agency.city
        self.agency_state = agency.state
        self.owner_id = owner.person_id
        self.owner_name = owner.name
        self.owner_surname = owner.surname
        self.owner_phone = owner.phone
        self.owner_address = owner.address
        self.owner_city = owner.city
        self.owner_state = owner.state
        self.date = date
        self.property_id = property_id
        self.contract_id = f"{property_id}/{owner.person_id}"
        with open("Property file.txt") as file:
            lines = file.read()
        lines = lines.split("\n")
        for line in lines:
            if line.startswith("{"):
                property_dict = json.loads(line)
                if property_dict["property_id"] == self.property_id:
                    self.property_price = property_dict["price"]
                    if property_dict["offer"] == "RENT":
                        self.service_price = str(round(int(self.property_price) * 0.5))
                    else:
                        self.service_price = str(round(int(self.property_price) * 0.01))

    def serialization(self) -> str:
        string_to_write = "CONTRACT\n"
        string_to_write += json.dumps(self.__dict__, sort_keys=True, default=str)
        return string_to_write + "\n\n"

    @abstractmethod
    def make_contract(self) -> None:
        pass
