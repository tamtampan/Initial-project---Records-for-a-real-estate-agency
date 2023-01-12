import json
import os
from datetime import datetime

from classes.agency_contract_class import AgencyContract
from classes.client_class import Client
from classes.contract_owner_client_class import ContractOwnerClient
from classes.owner_class import Owner
from classes.agency_class import Agency


PATH = os.getcwd()
DATE = datetime.now().date().__str__().split("-")
DATE = f"{DATE[2]}.{DATE[1]}.{DATE[0]}."


def add_new_property(agency: Agency) -> None:
    """ Writes new property in file and new contract in Contracts with agency.txt."""
    owner_id = input("Write owner id: ")
    if not Agency.owner_in_system(owner_id):
        Owner.add_new_owner(owner_id)
    property_type = input("What type of property do you want to add?\n1 - Agricultural land\n2 - Apartment\n3 - "
                          "Building\n4 - Building land\n5 - Building part\n6 - Business premises\n7 - Forest\n8 - "
                          "Forest land\n9 - Garage\n10 - Garage place\n11 - House\n")
    property_type = translate_property_type_option(property_type)
    if property_type == "":
        print("Invalid input.")
    else:
        new_property = Agency.convert_to_class(property_type).make_object(owner_id)
        if new_property is not None:
            with open("Property file.txt", "a") as file:
                file.write(new_property.serialization())
            print("Property successfully added.")
            owner_object = Agency.get_person_by_id(owner_id, "owner")
            new_contract = AgencyContract(owner_object, agency, DATE, new_property.property_id)
            new_contract.make_contract()


def translate_property_type_option(input_string: str) -> str:
    """ Converts option to new string. """
    if input_string == "1":
        return "Agricultural land"
    elif input_string == "2":
        return "Apartment"
    elif input_string == "3":
        return "Building"
    elif input_string == "4":
        return "Building land"
    elif input_string == "5":
        return "Building part"
    elif input_string == "6":
        return "Business premises"
    elif input_string == "7":
        return "Forest"
    elif input_string == "8":
        return "Forest land"
    elif input_string == "9":
        return "Garage"
    elif input_string == "10":
        return "Garage place"
    elif input_string == "11":
        return "House"
    else:
        return ""


def get_property_by_id(property_id: str) -> object:
    """ Gets property object from file by id."""
    with open("Property file.txt") as f:
        line = f.readline()
        while line:
            if line.startswith("{"):
                property_dict = json.loads(line)
                if property_dict["property_id"] == property_id:
                    return Agency.convert_to_class(property_dict["property_type"]).deserialization(line)
                line = f.readline()
            else:
                line = f.readline()


def property_in_system(property_id: str) -> bool:
    """ Returns True if property id is in file. """
    with open("Property file.txt") as f:
        line = f.readline()
        while line:
            if line.startswith("{"):
                property_dict = json.loads(line)
                if property_dict["property_id"] == property_id:
                    return True
                line = f.readline()
            else:
                line = f.readline()
    return False


def get_every_property_and_id(property_types=("AGRICULTURAL LAND", "APARTMENT", "BUILDING", "BUILDING LAND",
                                              "BUILDING PART", "BUSINESS PREMISES", "FOREST", "FOREST LAND",
                                              "GARAGE", "GARAGE PLACE", "HOUSE")) -> dict:
    """ Gets all property objects as keys and property id as values in dictionary. """
    try:
        with open("Property file.txt") as f:
            property_with_owner_id = {}
            line = f.readline()
            while line:
                if line.strip() in property_types:
                    next_line = f.readline()
                    property_object = Agency.convert_to_class(line.strip()).deserialization(next_line)
                    property_with_owner_id[property_object] = property_object.owner_id
                    line = next_line
                else:
                    line = f.readline()
            return property_with_owner_id
    except FileNotFoundError:
        with open("Property file.txt", "w") as f:
            f.write("")
            return {}


def get_price_sorted_offers() -> None:
    """ Gets Property objects from file and sorts in returning list. """
    dict_property_with_id = get_every_property_and_id()
    property_list = [property_ for property_ in dict_property_with_id]
    property_list.sort(key=lambda property_object: int(property_object.price), reverse=False)
    if len(property_list) == 0:
        print("We don't have offers today.")
    else:
        for item in property_list:
            print(item)
            print(Owner.find_by_id(item.owner_id))
            print()


def find_owners_by_letter_and_phone(first_letter: str, first_few_phone_numbers: str) -> list:
    """ Gets all owners by initials of names and phone numbers."""
    owners = []
    with open("Owners.txt") as file:
        lines = file.read()
    lines = lines.split("\n")
    for line in lines:
        if line.startswith("{"):
            owner_dict = json.loads(line)
            if owner_dict["phone"].startswith(first_few_phone_numbers) and owner_dict["name"].startswith(
                    first_letter.title()):
                owners.append(Owner.deserialization(line))
    return owners


def get_contracts_by_year(year: str) -> list:
    """ Gets contracts from specific year. """
    path1 = os.path.join(PATH, "Contracts", "Contracts owner-client", "Period contracts.txt")
    path2 = os.path.join(PATH, "Contracts", "Contracts owner-client", "Permanent contracts.txt")
    paths = [path1, path2]
    contract_objects = []
    for path in paths:
        if not os.path.exists(path):
            with open(path1, "w") as file:
                file.write("")
    for path in paths:
        with open(path) as f:
            line = f.readline()
            while line:
                if line == "CONTRACT\n":
                    line = f.readline()
                    contract_date = json.loads(line)["date"]
                    contract_date = contract_date.split(".")
                    if contract_date[2] == year:
                        f.readline()
                        property_line = f.readline()
                        contract_objects.append(ContractOwnerClient.deserialization(line, property_line))
                else:
                    line = f.readline()
    return contract_objects


def main():
    agency = Agency("Real estate agency", "Pera", "Peric", "Resavska 5", "Belgrade", "Serbia")
    option = input("Option number: ")
    while option != "x":
        if option == "1":
            add_new_property(agency)
        elif option == "2":
            owner_id = input("Write owner id: ")
            if not Agency.owner_in_system(owner_id):
                Owner.add_new_owner(owner_id)
            else:
                print("We already have that owner in system.")
        elif option == "3":
            client_id = input("Write client id: ")
            if Agency.client_in_system(client_id):
                print("We already have that client in system.")
            else:
                Client.add_new_client(client_id)
        elif option == "4":
            owner_id = input("Write owner id: ")
            if Agency.owner_in_system(owner_id):
                owner_object = Agency.get_person_by_id(owner_id, "owner")
                client_id = input("Write client id: ")
                if Agency.client_in_system(client_id):
                    client_object = Agency.get_person_by_id(client_id, "client")
                    property_id = input("Write property id: ")

                    if property_in_system(property_id):
                        date = input("The date of signing the contract (separated by full stop): ")
                        while True:
                            if "." not in date or (len(date.split(".")[0]) > 2 or
                                                   len(date.split(".")[1]) > 2 or
                                                   len(date.split(".")[2]) != 4 or not
                                                   (date.split(".")[0]).isdigit() or not
                                                   (date.split(".")[1]).isdigit() or not
                                                   (date.split(".")[2]).isdigit()):
                                date = input("Date has to be in form dd.mm.yyyy.\n")
                            else:
                                break
                        expiry_date = input("Contract expiration date (separated by full stop): ")
                        while True:
                            if "." not in expiry_date or (len(expiry_date.split(".")[0]) > 2 or
                                                          len(expiry_date.split(".")[1]) > 2 or
                                                          len(expiry_date.split(".")[2]) != 4 or not
                                                          (expiry_date.split(".")[0]).isdigit() or not
                                                          (expiry_date.split(".")[1]).isdigit() or not
                                                          (expiry_date.split(".")[2]).isdigit()):
                                expiry_date = input("Date has to be in form dd.mm.yyyy.\n")
                            else:
                                break
                        contract = ContractOwnerClient(owner=owner_object, agency=agency, property_id=property_id,
                                                       client=client_object, date=date, expiry_date=expiry_date)
                        contract.make_contract()
                    else:
                        print("We can't make contract with unregistered property.")
                else:
                    print("We can't make contracts with unregistered client.")
            else:
                print("We can't make contracts with unregistered owner.")
        elif option == "5":
            letter = input("Write initial letter/letters of name: ")
            phone = input("Write initial phone number/numbers: ")
            list_of_owners = find_owners_by_letter_and_phone(letter, phone)
            if len(list_of_owners) == 0:
                print("No owner found.")
            else:
                for owner in list_of_owners:
                    print(owner)
        elif option == "6":
            get_price_sorted_offers()
        elif option == "7":
            year = input("Contracts concluded which year you want? ")
            list_of_contracts = get_contracts_by_year(year)
            if len(list_of_contracts) == 0:
                print("No contracts found from that year.")
            else:
                for contract in list_of_contracts:
                    print(f"Owner: {contract.owner_name} {contract.owner_surname}, Client: {contract.client_name} "
                          f"{contract.client_surname}, Date: {contract.date}\nPrice: {contract.property_price}e\n\n")
        elif option == "8":
            owner_id = input("Write id of owner you want to erase: ")
            if Agency.owner_in_system(owner_id):
                Owner.remove_owner_by_id(owner_id=owner_id)
        elif option == "9":
            client_id = input("Write id of client you want to erase: ")
            if Agency.client_in_system(client_id):
                Client.remove_client_by_id(client_id=client_id)
                print("You removed client.")
        else:
            print("Invalid input, try again.")
        option = input("Option number: ")


if __name__ == '__main__':
    print("Options:\n1 - Add new property\n2 - Add new owner\n3 - Add new client\n4 - Make contract\n"
          "5 - Find owner by initial letters and phone numbers\n6 - Get price sorted offers\n"
          "7 - Contracts from specific year\nx - Close program")
    main()

# SOME OWNERS WITH PROPERTY IDS:
# {OWNER:OWNER_ID}
# {1111660201865: 112946, 26052782551: 676255, 30129856252: 332145, 23565481111: 444487, 0606996423151: 111353,
#   05064843214: 445662, 090699325147: 119991}
# SOME CLIENTS IDS:
# [030299632514, 09129876541, 1304997654020, 0203987654020, 0910988326502, 1408999656030]
