""""

Ovo je program za agenciju za nekretninte. Agencija vodi evidenciju o vlasnicima, klijentima i nekretninama.
Izmedju agencije i vlasnika se prave ugovori, odredjuje se cena usluge agencije i ugovori se cuvaju u
posebnom fajlu. Takodje ugovori izmedju vlasnika i klijenata se cuvaju u posebnom direktorijumu.

Fajlovi i sadrzaj:
* Owners.txt - vlasnici
* Clients.txt - klijenti
* Property file.txt - nekretnine
* Contracts - direktorijum koji sadrzi:
    Contracts with agency.txt - ugovori vlasnik - agencija
    Contracts owner-client - direktorijum koji sadrzi:
        Period contracts.txt - ugovori na period (izdavanje)
        Permanent contracts.txt - ugovori prodaje

        

Implementirane klase:

Apstraktna klasa "Property"

- Metode:
    serialization() - pretvara objekat u string za ispis
    __str__() - vraca string sa vaznim osobinama objekta
    make_property_features() - u inputu uzima neophodne informacije od kojih pravi recnik sa atributima klase
    remove_property_by_id() - uzima string id nekretnine, pomocu njega pronalazi u fajlu nekretninu i brise je

- Child klase (11):
    AgriculturalLand, Apartment, Building, BuildingLand, BuildingPart, BusinessPremises, Forest,
    ForestLand, Garage, GaragePlace, House

    Svaka od ovih klasa sadrzi:
    deserialization() - od datog stringa vraca objekat te klase
    make_object() - u inputu uzima neophodne informacije i uz pomoc funkcije parent klase
        (make_property_features()) pravi objekat koji je povratna vrednost


Apstraktna klasa "Person"

- Child klase (2):
    Owner, Client

    Obe klase sadrze:
    serialization() - pretvara objekat u string za ispis
    __str__() - vraca string sa vaznim osobinama objekta
    deserialization() - od datog stringa vraca objekat te klase
    find_by_id() - pomocu unete vrednosti pronalazi u fajlu informacije o objektu i pravi taj objekat
    add_new_client() / add_new_owner() - pomocu inputa pravi objekat i ispisuje informacije o njemu u fajl
    remove_client_by_id() / remove_client_by_id() - pomocu ulazne vrednosti nalazi objekat u fajlu i iz istog
        brise informacije o njemu

Apstraktna klasa "Contract"

- Metode:
    serialization() - pretvara objekat u string za ispis
    make_contract() - apstraktna metoda

- Child klase (2):
    ContractOwnerClient, AgencyContract

    Svaka od ovih klasa sadrzi:
    deserialization() - od datog stringa vraca objekat te klase
    make_contract() - uz pomoc metode deserialization() upisuje u fajl informacije o ugovoru. Ova
    metoda u klasi ContractOwnerClient ima zadatak i da obrise nekretninu iz fajla kad se ugovor napravi
    uz pomoc metode remove_property_by_id() pozvane pomocu klase Property


Klase "InputNotValid" i "InputNotDigit" - sluze za nepravilan unos u inputu


Modul main:
    Funkcije:
    - main() - na osnovu input unosa odredjuje koje ce funkcionalnosti biti pokrenute
    - add_new_property() - na osnovu inputa odredjuje koce ce se funkcionalnosti pokrenuti
        kako bi se upisala odgovarajuca nekretnina u fajl
    - translate_property_type_option() - na osnovu inputa vraca odgovarajuci string
    - get_property_by_id() - pomocu unosa stringa vraca objekat izabrane klase
    - property_in_system() - proverava da li nekretnina postoji u sistemu
    - get_every_property_and_id() - vraca recnik sa objektima svih nekretnina u fajlu i vrednostima
        koje se odnose na id vlasnia
    - get_price_sorted_offers() - stampa nekretnine i njihove vlasnike sortirane po ceni neketnine
    - find_owners_by_letter_and_phone() - na osnovu unetih vrednosti u inputu vraca listu objekta vlasnika
        sa zadatim inicijalnim vrednostima
    - get_contracts_by_year() - ucitava ugovore iz zadate godine i vraca listu objekata tih ugovora


Modul updating_functions koji u sebi ima 3 funkcije:
    contract_expired() - uporedjuje datum iz ugovora sa danasjim datumom, vraca True ako je ugovor istekao
    update_expired_contract_files() - brise ugovore ciji je datum istekao iz fajla "Period contracts.txt"
        uz pomoc funkcije remove_expired_contract() iz istog modula i upisuje iste ugovore u fajl
        "Permanent contracts.txt", zatim nekretninu vraca u fajl sa ponudama ("Property file.txt")
    remove_expired_contract() - brise iz fajla sve istekle ugovore


Projekat nije uspeo kao sto je zamisljeno i postoje nedostaci koje treba doraditi.

"""