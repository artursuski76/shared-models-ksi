
from typing import Literal

from pydantic import Field, BaseModel


class Podstawowa(BaseModel):
    rodzaj_fv: Literal["Podstawowa"] = Field(
        "VAT",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Zaliczkowa(BaseModel):
    rodzaj_fv: Literal["Zaliczkowa"] = Field(
        "ZAL",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Rozliczeniowa(BaseModel):
    rodzaj_fv: Literal["Rozliczeniowa"] = Field(
        "ROZ",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Korekta(BaseModel):
    rodzaj_fv: Literal["Korekta"] = Field(
        "KOR",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

