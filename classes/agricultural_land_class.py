import json

from classes.property_class import Property


class AgriculturalLand(Property):
    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str, owner_id: str,
                 property_id: str, property_type: str, water="0", electricity="0", registered="0") -> None:
        super().__init__(offer, address, city, state, area, price, owner_id, property_id, property_type)
        self.water = water
        self.electricity = electricity
        self.registered = registered

    @staticmethod
    def deserialization(string_from_file: str) -> "AgriculturalLand":
        return AgriculturalLand(**json.loads(string_from_file))

    @staticmethod
    def make_object(owner_id: str) -> object:
        property_dict = Property.make_property_features()
        if property_dict == {}:
            return None
        property_dict["owner_id"] = owner_id
        property_dict["property_type"] = "Agricultural land"
        water = input("Does the agricultural land have water? y/n: ")
        if water == "y":
            water = "yes"
        else:
            water = "0"
        electricity = input("Does the agricultural land have electricity? y/n: ")
        if electricity == "y":
            electricity = "yes"
        else:
            electricity = "0"
        registered = input("Is the agricultural land registered? y/n: ")
        if registered == "y":
            registered = "yes"
        else:
            registered = "0"
        return AgriculturalLand(**property_dict, water=water, electricity=electricity, registered=registered)
