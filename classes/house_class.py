import json

from classes.property_class import Property


class House(Property):
    def __init__(self, offer: str, address: str, city: str, state: str, area: str, price: str, owner_id: str,
                 property_id: str, num_bedrooms: str, num_floors: str, parking="0", terrace="0", yard_area="0",
                 property_type="Kuca", air_conditioner="0", cable_tv="0", heating="0") -> None:
        super().__init__(offer, address, city, state, area, price, owner_id, property_id, property_type)
        self.num_bedrooms = num_bedrooms
        self.num_floors = num_floors
        self.parking = parking
        self.terrace = terrace
        self.yard_area = yard_area
        self.air_conditioner = air_conditioner
        self.cable_tv = cable_tv
        self.heating = heating

    @staticmethod
    def make_object(owner_id: str) -> object:
        property_dict = Property.make_property_features()
        if property_dict == {}:
            return None
        property_dict["owner_id"] = owner_id
        property_dict["property_type"] = "House"
        num_bedrooms = input("Number of bedrooms: ")
        num_floors = input("Number of floors: ")
        parking = input("Is there a parking lot? y/n: ")
        if parking == "y":
            parking = "1"
        else:
            parking = "0"
        terrace = input("Number of terraces: ")
        yard_area = input("How many square meters does the yard have? ")
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
        return House(**property_dict, num_bedrooms=num_bedrooms, num_floors=num_floors, parking=parking,
                     terrace=terrace, yard_area=yard_area, air_conditioner=air_conditioner, cable_tv=cable_tv,
                     heating=heating)

    @staticmethod
    def deserialization(string_from_file: str) -> "House":
        return House(**json.loads(string_from_file))
