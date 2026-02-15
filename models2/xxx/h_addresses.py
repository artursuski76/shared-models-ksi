from typing import Optional

from pydantic import BaseModel, Field

from models.xxx.h_enums import EuropeLandsEnum, WorldLandsEnum


class AddressGeneral(BaseModel):

    # Address components
    street: str = Field(..., description="Street name and number.")
    apartment_number: Optional[str] = Field(None, description="Apartment or office number.")
    postal_code: str = Field(..., description="The official postal code.")
    city: str = Field(..., description="The city or town name.")
    country: str = Field(default="PL", description="The country name (ISO 3166-1 alpha-2 format recommended).")


class AddressDetailed(BaseModel):
    tel: str = Field(
        ...,
        description="Phone number.",
        max_length=20

    )



class AddressesModel(BaseModel):
    company_address: AddressDetailed
    contact_address: AddressGeneral
    bussiness_address: AddressDetailed


class AdressBase(BaseModel):
    adres_l1: Optional[str] = Field(
        None,
        alias="AdresL1",
        title="Ulica i numer domu/lokalu",
        max_length=100
    )
    adres_l2: Optional[str] = Field(
        None,
        alias="AdresL2",
        title="Kod pocztowy i miejscowość",
        max_length=100
    )


class AdresEU(AdressBase):
    kod_kraju: EuropeLandsEnum = Field(
        default=EuropeLandsEnum.PL,
        alias="KodKraju",
        title="Kod kraju"
    )

class AdresWR(AdressBase):
    kod_kraju: WorldLandsEnum = Field(
        default=WorldLandsEnum.PL,
        alias="KodKraju",
        title="Kod kraju"
    )
