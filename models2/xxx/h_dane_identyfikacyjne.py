from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, Field

from models2.xxx.h_enums import EuropeLandsEnum, WorldLandsEnum
from models2.enums import CounterpartyType


class ZagraniczneFirmoweDaneIdentyfikacyjne(BaseModel):
    nazwa: str = Field(
        ...,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    kod_ue: EuropeLandsEnum = Field(
        None,
        alias="KodUE",
        title="VIESS – kod UE"
    )
    nr_vat_ue: Optional[str] = Field(
        None,
        alias="NrVatUE",
        title="VIESS – nr identyfikacyjny bez kodu kraju"
    )

    kod_kraju: WorldLandsEnum = Field(
        None,
        alias="KodKraju",
        title="EKSPORT – kod kraju"
    )
    tax_id: str = Field(
        None,
        alias="NrID",
        title="EKSPORT – Numer podatkowy"
    )

class OsobaFizyczna(BaseModel):
    rodzaj_kontr: Literal["osoba_fizyczna"] = Field(
        "osoba_fizyczna",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )
    brak_id: str = Field(
        default="1",
        alias="BrakID",
        description="znacznik braku ID",
        json_schema_extra={"exclude_from_form": True}
    )
    nazwa: str = Field(
        ...,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )

    type: CounterpartyType = Field(
        CounterpartyType,
        alias="Typ",
        title="Typ"
    )

class PodatnikKrajowy(BaseModel):
    rodzaj_kontr: Literal["podatnik_krajowy"] = Field(
        "podatnik_krajowy",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    nip: str = Field(
        ...,
        alias="NIP",
        title="NIP",
        min_length=10,
        max_length=10,
        pattern=r'^\d{10}$|^brak$'
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        alias="Typ",
        title="Typ"
    )

class PodatnikVIES(ZagraniczneFirmoweDaneIdentyfikacyjne):
    rodzaj_kontr: Literal["podatnik_vies"] = Field(
        "podatnik_vies",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        alias="Typ",
        title="Typ"
    )
class PodatnikZagraniczny(ZagraniczneFirmoweDaneIdentyfikacyjne):
    rodzaj_kontr: Literal["podatnik_zagraniczny"] = Field(
        "podatnik_zagraniczny",
        title="Rodzaj Kontrahenta",
        json_schema_extra={"exclude_from_form": True}
    )

    nazwa: str = Field(
        ...,
        alias="Nazwa",
        title="Pełna nazwa Kontrahenta",
        max_length=200
    )
    type: CounterpartyType = Field(
        CounterpartyType,
        alias="Typ",
        title="Typ"
    )

# class OwnBankAccount(BaseModel):
#     iban: str  # IBAN
#     currency: str  # PLN, EUR
#     accounting_code: str  # np. "130-01" (powiązanie z kontem w FK)
#     name: str  # np. "Konto firmowe główne"



# class Bank(BaseModel):
#     rodzaj_kontr: Literal["bank"] = Field(
#         "bank",
#         title="Rodzaj",
#         json_schema_extra={"exclude_from_form": True}
#     )
#     nazwa_banku: str = Field(
#         None,
#         description="Numer IBAN"
#     )


class UrzadSkarbowy(BaseModel):
    rodzaj_kontr: Literal["urzad_skarbowy"] = Field(
        "urzad_skarbowy",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    nazwa_urzedu: str = Field(
        None,
        title="Nazwa urzędu"
    )

class Pracownik(BaseModel):
    rodzaj_kontr: Literal["pracownik"] = Field(
        "pracownik",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    imie: str = Field(
        None,
        title="Nr urzędu"
    )
    nazwisko: str = Field(
        None,
        title="Nazwa urzędu"
    )
    data_ur: date = Field(
        None,
        title="Data ur."
    )

class CzlonekZarzadu(BaseModel):
    rodzaj_kontr: Literal["czlonek_zarzadu"] = Field(
        "czlonek_zarzadu",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    imie: str = Field(
        None,
        title="Nr urzędu"
    )
    nazwisko: str = Field(
        None,
        title="Nazwa urzędu"
    )
    data_ur: date = Field(
        None,
        title="Data ur."
    )