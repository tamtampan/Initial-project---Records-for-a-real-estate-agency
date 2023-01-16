import json

from classes.property_class import Property


class Forest(Property):
    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str, owner_id: str,
                 property_id: str, property_type: str, registered="0") -> None:
        super().__init__(offer, address, city, state, area, price, owner_id, property_id, property_type)
        self.registered = registered

    @staticmethod
    def deserialization(string_from_file: str) -> "Forest":
        return Forest(**json.loads(string_from_file))

    @staticmethod
    def make_object(owner_id: str) -> object:
        property_dict = Property.make_property_features()
        if property_dict == {}:
            return None
        property_dict["owner_id"] = owner_id
        property_dict["property_type"] = "Forest"
        registered = input("Is the forest registered? y/n: ")
        if registered == "y":
            registered = "yes"
        else:
            registered = "0"
        return Forest(**property_dict, registered=registered)
