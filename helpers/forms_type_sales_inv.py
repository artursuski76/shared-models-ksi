from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class DostawaWDacieWystawienia(BaseModel):
    date_sale: Literal["dostawa_w_dacie_wystawienia"] = Field(
        "dostawa_w_dacie_wystawienia",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class WspolnaDataDostawy(BaseModel):
    date_sale: Literal["wspolna_data_dostawy"] = Field(
        "wspolna_data_dostawy",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

    common_date_sale: date = Field(default=date.today, title="Wspólna data sprzedaży")


class DostawaWOkresieCzasu(BaseModel):
    date_sale: Literal["dostawa_w_okresie_czasu"] = Field(
        "dostawa_w_okresie_czasu",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    date_sale_from: date = Field(None, title="Dostawa Od")
    date_sale_to: date = Field(None, title="Dostawa Do")