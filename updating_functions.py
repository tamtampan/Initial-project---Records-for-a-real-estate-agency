import json
import os
from datetime import datetime

from classes.agency_class import Agency

PATH = os.getcwd()


def contract_expired(contract_date: str) -> bool:
    """ Compares date from file with current date. """
    contract_date = contract_date.split(".")
    contract_day = contract_date[0]
    contract_month = contract_date[1]
    contract_year = contract_date[2]
    now_date = datetime.now().date().__str__().split("-")
    now_year = now_date[0]
    now_month = now_date[1]
    now_day = now_date[2]
    if int(contract_year) > int(now_year):
        return False
    elif int(contract_year) == int(now_year):
        if int(contract_month) > int(now_month):
            return False
        elif int(contract_month) == int(now_month):
            if int(contract_day) >= int(now_day):
                return False
            else:
                return True
        else:
            return True
    else:
        return True


# ova funkcija brise istekle ugovore iz aktuelnog foldera, upisuje ih u folder isteklih ugovora i dodaje nekretninu u trenutno slobodne nekretnine
def update_expired_contract_files() -> None:
    """Erases expired contracts from file and writes them in another file."""
    path = os.path.join(PATH, "Contracts", "Contracts owner-client", "Period contracts.txt")
    expired_contracts = []
    expired_contracts_property_ids = []
    available_property_dicts = []
    with open(path) as file:
        line = file.readline()
        while line:
            if line == "CONTRACT\n":
                line = file.readline()
                dict_line = json.loads(line)
                if contract_expired(dict_line["expiry_date"]):
                    expired_contracts.append("CONTRACT\n")
                    expired_contracts.append(line)
                    expired_contracts.append(file.readline())
                    line = file.readline()
                    expired_contracts.append(line)
                    available_property_dicts.append(line)
                    expired_contracts_property_ids.append(dict_line["property_id"])
            else:
                line = file.readline()
    new_path = os.path.join(PATH, "Contracts", "Contracts owner-client", "Expired contracts.txt")
    with open(new_path, "a") as file:
        for contract in expired_contracts:
            file.write(contract)
    remove_expired_contract(expired_contracts_property_ids)
    for property_line in available_property_dicts:
        property_dict = json.loads(property_line)
        property_object = Agency.deserialize_property_obj(property_dict["property_type"], property_line)
        with open("Property file.txt", "a") as file:
            file.write(property_object.serialization())


def remove_expired_contract(list_of_ids: list) -> None:
    """Erases expired contracts from file. """
    path = os.path.join(PATH, "Contracts", "Contracts owner-client", "Period contracts.txt")
    with open(path) as file:
        lines = file.read()
    lines = lines.split("\n")
    line_indexes_to_erase = []
    for index, line in enumerate(lines):
        if line.startswith("{"):
            property_dict = json.loads(line)
            if property_dict["property_id"] in list_of_ids:
                line_indexes_to_erase.append(index-1)
                line_indexes_to_erase.append(index)
    lines_to_print = []
    for index, line in enumerate(lines):
        if index not in line_indexes_to_erase:
            lines_to_print.append(line)
    with open(path, "w") as file:
        for line in lines_to_print:
            line += "\n"
            file.write(line)
