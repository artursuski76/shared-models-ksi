from datetime import datetime, date
from typing import Literal, Optional

from pydantic import BaseModel, Field


# class OneDateTransaction(BaseModel):
#     typ_transakcji: Literal["one_date_transaction"] = Field(
#         "one_date_transaction",
#         title="Rodzaj",
#         json_schema_extra={"exclude_from_form": True}
#     )
#
# class FullDateTransaction(BaseModel):
#     typ_transakcji: Literal["full_date_transaction"] = Field(
#         "full_date_transaction",
#         title="Rodzaj",
#         json_schema_extra={"exclude_from_form": True}
#     )
#
#
#     date_vat: Optional[date] = Field(None, title="Data VAT")
#     date_cit: Optional[date] = Field(None, title="Data CIT")
#     date_supply: Optional[date] = Field(None, title="Data sprzedaży/dostawy")
#     date_settlement: Optional[date] = Field(None, title="Termin zapłaty")
#     date_issue: Optional[date] = Field(None, title="Data wystawienia")
#     date_received: Optional[date] = Field(None, title="Data otrzymania faktury")
#     date_goods_receipt: Optional[date] = Field(None, title="Data przyjęcia towaru")


class DataWspolna(BaseModel):
    typ_transakcji: Literal["data_wspolna"] = Field(
        "data_wspolna",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class RozneDaty(BaseModel):
    typ_transakcji: Literal["rozne_daty"] = Field(
        "rozne_daty",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

    date_vat: Optional[date] = Field(None, title="Data VAT")
    date_cit: Optional[date] = Field(None, title="Data CIT")
    date_supply: Optional[date] = Field(None, title="Data sprzedaży/dostawy")
    date_settlement: Optional[date] = Field(None, title="Termin zapłaty")
    date_issue: Optional[date] = Field(None, title="Data wystawienia dokumentu")
    date_received: Optional[date] = Field(None, title="Data otrzymania faktury")
    date_goods_receipt: Optional[date] = Field(None, title="Data przyjęcia towaru")

class SprzedazOdDo(BaseModel):
    typ_transakcji: Literal["sprzedaz_od_do"] = Field(
        "sprzedaz_od_do",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    date_supply_from: date = Field(None, title="From*")
    date_supply_to: date = Field(None, title="To*")
    date_vat: Optional[date] = Field(None, title="Data VAT")
    date_cit: Optional[date] = Field(None, title="Data CIT")
    date_settlement: Optional[date] = Field(None, title="Termin zapłaty")
    date_issue: Optional[date] = Field(None, title="Data wystawienia dokumentu")
    date_received: Optional[date] = Field(None, title="Data otrzymania faktury")
    date_goods_receipt: Optional[date] = Field(None, title="Data przyjęcia towaru")