import json

from classes.property_class import Property


class BusinessPremises(Property):
    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str, owner_id: str,
                 property_id: str, property_type: str, on_floor: str, elevator="0", parking="0",
                 air_conditioner="0", cable_tv="0", heating="0") -> None:
        super().__init__(offer, address, city, state, area, price, owner_id, property_id, property_type)
        self.on_floor = on_floor
        self.elevator = elevator
        self.parking = parking
        self.air_conditioner = air_conditioner
        self.cable_tv = cable_tv
        self.heating = heating

    @staticmethod
    def deserialization(string_from_file: str) -> "BusinessPremises":
        return BusinessPremises(**json.loads(string_from_file))

    @staticmethod
    def make_object(owner_id: str) -> object:
        property_dict = Property.make_property_features()
        if property_dict == {}:
            return None
        property_dict["owner_id"] = owner_id
        property_dict["property_type"] = "Business premises"
        on_floor = input("What floor is the local on? ")
        parking = input("Is there reserved parking lot? y/n: ")
        if parking == "y":
            parking = "1"
        else:
            parking = "0"
        air_conditioner = input("Is there air conditioner? y/n: ")
        if air_conditioner == "y":
            air_conditioner = "1"
        else:
            air_conditioner = "0"
        cable_tv = input("Is there cable tv? y/n: ")
        if cable_tv == "y":
            cable_tv = "1"
        else:
            cable_tv = "0"
        heating = input("Type of heating: ")
        elevator = input("Is there elevator? y/n: ")
        if elevator == "y":
            elevator = "1"
        else:
            elevator = "0"
        return BusinessPremises(**property_dict, on_floor=on_floor, parking=parking, air_conditioner=air_conditioner,
                                cable_tv=cable_tv, heating=heating, elevator=elevator)
