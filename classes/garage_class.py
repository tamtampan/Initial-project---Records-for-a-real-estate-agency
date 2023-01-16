import json

from classes.property_class import Property


class Garage(Property):
    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str, owner_id: str,
                 property_id: str, property_type: str, num_of_car_places="0") -> None:
        super().__init__(offer, address, city, state, area, price, owner_id, property_id, property_type)
        self.num_of_car_places = num_of_car_places

    @staticmethod
    def deserialization(string_from_file: str) -> "Garage":
        return Garage(**json.loads(string_from_file))

    @staticmethod
    def make_object(owner_id: str) -> object:
        property_dict = Property.make_property_features()
        if property_dict == {}:
            return None
        property_dict["owner_id"] = owner_id
        property_dict["property_type"] = "Garage"
        num_of_car_places = input("Number of car places: ")
        return Garage(**property_dict, num_of_car_places=num_of_car_places)
