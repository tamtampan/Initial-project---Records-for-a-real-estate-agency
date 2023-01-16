import json
import os

from classes.contract_class import Contract
from classes.owner_class import Owner
from classes.agency_class import Agency

PATH = os.getcwd()


class AgencyContract(Contract):
    def __init__(self, owner: Owner, agency: Agency, date: str, property_id: str) -> None:
        super().__init__(owner=owner, agency=agency, date=date, property_id=property_id)

    @staticmethod
    def deserialization(string_from_file: str) -> "AgencyContract":
        return AgencyContract(**json.loads(string_from_file))

    def make_contract(self) -> None:
        path = os.path.join(PATH, "Contracts", f"Contracts with agency.txt")
        try:
            with open(path, "a") as f:
                f.write(self.serialization())
        except FileNotFoundError:
            dir_path = os.path.join(PATH, "Contracts")
            os.mkdir(dir_path)
            with open(path, "w") as f:
                f.write(self.serialization())
