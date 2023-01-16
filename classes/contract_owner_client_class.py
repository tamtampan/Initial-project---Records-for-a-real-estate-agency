import json
import os

from classes.contract_class import Contract
from classes.owner_class import Owner
from classes.agency_class import Agency
from classes.property_class import Property
from classes.client_class import Client

PATH = os.getcwd()


class ContractOwnerClient(Contract):
    def __init__(self, owner: Owner, agency: Agency, date: str, property_id: str, client: Client,
                 expiry_date="") -> None:
        super().__init__(owner=owner, agency=agency, date=date, property_id=property_id)
        self.client_id = client.person_id
        self.client_name = client.name
        self.client_surname = client.surname
        self.client_phone = client.phone
        self.client_address = client.address
        self.client_city = client.city
        self.client_state = client.state
        self.expiry_date = expiry_date

    def serialization(self) -> str:
        string_to_write = "CONTRACT\n"
        string_to_write += json.dumps(self.__dict__, sort_keys=True, default=str)
        return string_to_write

    def set_property_price(self, property_price) -> None:
        self.property_price = property_price

    @staticmethod
    def deserialization(string_from_file: str, property_line: str) -> "ContractOwnerClient":
        dict_from_file = json.loads(string_from_file)
        dict_property = json.loads(property_line)
        property_obj = Agency.convert_to_class(dict_property["property_type"]).deserialization(property_line)
        agency = Agency.agency[0]
        date = dict_from_file["date"]
        expiry_date = dict_from_file["expiry_date"]
        if Agency.owner_in_system(dict_from_file["owner_id"]):
            owner_object = Agency.get_person_by_id(dict_from_file["owner_id"], "owner")
            if Agency.client_in_system(dict_from_file["client_id"]):
                client_object = Agency.get_person_by_id(dict_from_file["client_id"], "client")
            else:
                raise "Client has been erased from system."
        else:
            raise "Owner has been erased from system."
        contract_object = ContractOwnerClient(owner=owner_object, agency=agency, date=date,
                                              property_id=dict_from_file["property_id"], client=client_object,
                                              expiry_date=expiry_date)
        contract_object.set_property_price(property_obj.price)
        return contract_object

    def make_contract(self) -> None:
        with open("Property file.txt") as file:
            line = file.readline()
            wanted_object = None
            while line and wanted_object is None:
                if line.startswith("{"):
                    property_dict = json.loads(line)
                    if property_dict["property_id"] == self.property_id:
                        offer = property_dict["offer"]
                        wanted_object = line
                    line = file.readline()
                else:
                    line = file.readline()
        string_to_write = self.serialization() + "\nPROPERTY\n" + wanted_object + "\n\n"
        if offer == "RENT":
            path = os.path.join(PATH, "Contracts", "Contracts owner-client", "Period contracts.txt")
        else:
            path = os.path.join(PATH, "Contracts", "Contracts owner-client", "Permanent contracts.txt")
        try:
            with open(path, "a") as f:
                f.write(string_to_write)
            print("Contract has been successfully made.")
            Property.remove_property_by_id(self.property_id)
        except FileNotFoundError:
            path_dir = os.path.join(PATH, "Contracts", "Contracts owner-client")
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
            with open(path, "w") as f:
                f.write(string_to_write)
            print("Contract has been successfully made.")
            Property.remove_property_by_id(self.property_id)
