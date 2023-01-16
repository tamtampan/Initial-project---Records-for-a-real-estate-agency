from classes.agricultural_land_class import AgriculturalLand
from classes.building_class import Building
from classes.building_land_class import BuildingLand
from classes.building_part_class import BuildingPart
from classes.business_premises_class import BusinessPremises
from classes.client_class import Client
from classes.forest_class import Forest
from classes.forest_land_class import ForestLand
from classes.garage_class import Garage
from classes.garage_place_class import GaragePlace
from classes.house_class import House
from classes.apartment_class import Apartment
from classes.owner_class import Owner


class Agency:
    agency = []

    def __init__(self, name: str, boss_name: str, boss_surname: str, address: str, city: str, state: str) -> None:
        self.name = name
        self.boss_name = boss_name
        self.boss_surname = boss_surname
        self.address = address
        self.city = city
        self.state = state
        self.agency.append(self)

    @staticmethod
    def owner_in_system(owner_id: str) -> bool:
        try:
            with open("Owners.txt") as file:
                line = file.readline()
                while line:
                    if line == "OWNER\n":
                        line = file.readline()
                        if line.strip() == owner_id:
                            return True
                    else:
                        line = file.readline()
            return False
        except FileNotFoundError:
            with open("Owners.txt", "w") as file:
                file.write("")
            return False

    @staticmethod
    def client_in_system(client_id: str) -> bool:
        try:
            with open("Clients.txt") as file:
                line = file.readline()
                while line:
                    if line == "CLIENT\n":
                        line = file.readline()
                        if line.strip() == client_id:
                            return True
                    else:
                        line = file.readline()
            return False
        except FileNotFoundError:
            with open("Clients.txt", "w") as file:
                file.write("")
            return False

    @staticmethod
    def get_person_by_id(person_id: str, person_type: str) -> object:
        if person_type == "owner":
            file_path = "Owners.txt"
        else:
            file_path = "Clients.txt"
        with open(file_path) as file:
            line = file.readline()
            while line:
                if line == person_id + "\n":
                    line = file.readline()
                    if person_type == "owner":
                        return Owner.deserialization(line)
                    else:
                        return Client.deserialization(line)
                else:
                    line = file.readline()

    @staticmethod
    def convert_to_class(property_type: str):
        if property_type.upper() == "AGRICULTURAL LAND":
            return AgriculturalLand
        elif property_type.upper() == "APARTMENT":
            return Apartment
        elif property_type.upper() == "BUILDING":
            return Building
        elif property_type.upper() == "BUILDING LAND":
            return BuildingLand
        elif property_type.upper() == "BUILDING PART":
            return BuildingPart
        elif property_type.upper() == "BUSINESS PREMISES":
            return BusinessPremises
        elif property_type.upper() == "FOREST":
            return Forest
        elif property_type.upper() == "FOREST LAND":
            return ForestLand
        elif property_type.upper() == "GARAGE":
            return Garage
        elif property_type.upper() == "GARAGE PLACE":
            return GaragePlace
        elif property_type.upper() == "HOUSE":
            return House
