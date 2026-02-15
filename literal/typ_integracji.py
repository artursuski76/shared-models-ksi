from datetime import date
from typing import Literal

from pydantic import BaseModel, Field






class WooCommerce(BaseModel):
    typ_integracji: Literal["woo_commerce"] = Field(
        "woo_commerce",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    url: str = Field(
        None,
        title="Adres sklepu Woo"
    )
    key: str = Field(
        None,
        title="Consumer key"
    )
    secret: str = Field(
        None,
        title="Consumer secret"
    )

class FakturowniaPl(BaseModel):
    typ_integracji: Literal["fakturownia_pl"] = Field(
            "fakturownia_pl",
            title="Rodzaj",
            json_schema_extra={"exclude_from_form": True}
    )
    store_url: str = Field(
        alias="tore_url",
        title="tore_url",
        max_length=100
    )
    consumer_key: str = Field(
        alias="tore_url",
        title="tore_url",
        max_length=100
    )
    consumer_secret: str = Field(
        alias="tore_url",
        title="tore_url",
        max_length=100
    )