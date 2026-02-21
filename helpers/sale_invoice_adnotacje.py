from typing import Union, Literal

from pydantic import BaseModel, Field

from models2.helpers.procedury_marzy import MarzaNie, MarzaTak


class AdnotacjeNie(BaseModel):
    adnotacje: Literal["nie"] = Field(
        "nie",
        title="Adnotacje",
        json_schema_extra={"exclude_from_form": True}
    )

class AdnotacjeTak(BaseModel):
    adnotacje: Literal["tak"] = Field(
        "tak",
        title="Adnotacje",
        json_schema_extra={"exclude_from_form": True}
    )
    cash_method: bool = False
    self_billing: bool = False
    reverse_charge: bool = False
    split_payment: bool = False
    ec_simplified: bool = False

    p_marzy: Union[
        MarzaNie,
        MarzaTak
    ] = Field(
        ...,
        discriminator='p_marzy',
        alias="ProceduraMarzy",
        title="Procedura Marży",
        exclude=True
    )

