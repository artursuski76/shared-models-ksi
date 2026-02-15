
from typing import Optional, Union, Dict, Any

from pydantic import Field, model_serializer

from models2.xxx.h_dane_identyfikacyjne import (OsobaFizyczna,
                                               PodatnikKrajowy,
                                               PodatnikVIES,
                                               PodatnikZagraniczny, Pracownik
                                               )
from models2.xxx.h_enums import WorldLandsEnum
from models2.abase import BasicBasic


class Counterparty(BasicBasic):

    model_name: str = Field(
        "Counterparty",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    address_l1: Optional[str] = Field(
        None,
        alias="AdresL1",
        title="Adres - ulica i nr",
        max_length=100
    )
    address_l2: Optional[str] = Field(
        None,
        alias="AdresL2",
        title="Adres - kod i poczta",
        max_length=100
    )
    address_country: WorldLandsEnum = Field(
        WorldLandsEnum.PL,
        alias="Adres - kraj",
        title="Adres - kraj",
    )

    dane_identyfikacyjne: Union[
        OsobaFizyczna,
        PodatnikKrajowy,
        PodatnikVIES,
        PodatnikZagraniczny,
        Pracownik
    ] = Field(
        ...,
        discriminator='rodzaj_kontr',
        alias="DaneIdentyfikacyjne",
        title="Dane Kontrahenta"
    )

    @model_serializer(mode="wrap")
    def serialize_flat(self, handler) -> Dict[str, Any]:
        # Pobieramy standardowy słownik (wywołując oryginalny serializer)
        data = handler(self)

        # Wyciągamy dane identyfikacyjne
        dane_ident = data.pop("dane_identyfikacyjne", {})

        # Łączymy główny słownik z polami z dane_identyfikacyjne
        # Uwaga: Jeśli klucze się powtórzą, dane_ident nadpiszą te z poziomu głównego
        return {**data, **dane_ident}

    class FormConfig:

        list_view_fields = [
            "my_id", "nazwa", "type", "tax_id", "brak_id", "rodzaj_kontr",
            "address_country", "address_l2", "address_l1",
            "status", "last_sync", "created_at"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "counterparty"