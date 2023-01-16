import json
from abc import ABC


class Property(ABC):

    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str,
                 owner_id: str, property_id: str, property_type: str) -> None:
        self.offer = offer
        self.address = address
        self.city = city
        self.state = state
        self.area = area
        self.price = price
        self.owner_id = owner_id
        self.property_id = property_id
        self.property_type = property_type

    def serialization(self) -> str:
        string_to_write = self.property_type.upper() + "\n"
        string_to_write += json.dumps(self.__dict__, sort_keys=True, default=str)
        return string_to_write + "\n\n"

    def __str__(self) -> str:
        return f"{self.property_type} - {self.offer.upper()}, {self.address}, {self.city}, {self.state}\n" \
               f"Povrsina: {self.area}, Cena: {self.price}"

    @staticmethod
    def make_property_features() -> dict:
        offer = input("Do you want to:\n1 - Sell property\n2 - Rent property\n")
        if offer == "1":
            offer = "Sell"
        elif offer == "2":
            offer = "Rent"
        address = input("Property address: ")
        city = input("City: ")
        state = input("State: ")
        price = input("Price (in euros): ")
        if not price.isdigit():
            print("Input is not digit.")
            return {}
        area = input("Square meters: ")
        if not area.isdigit():
            print("Input is not digit.")
        property_id = input("Property id: (minimum 6 characters): ")
        return {"offer": offer, "address": address, "city": city, "state": state, "area": area, "price": price,
                "property_id": property_id}

    @staticmethod
    def remove_property_by_id(property_id: str) -> None:
        with open("Property file.txt") as file:
            lines = file.read()
        lines = lines.split("\n")
        for index, line in enumerate(lines):
            if line.startswith("{"):
                property_dict = json.loads(line)
                if property_dict["property_id"] == property_id:
                    line_to_erase = index
        try:
            del lines[line_to_erase - 1: line_to_erase + 2]
            with open("Property file.txt", "w") as file:
                for line in lines:
                    line += "\n"
                    file.write(line)
        except Exception as e:
            print(e)
