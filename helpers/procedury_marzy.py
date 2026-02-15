from typing import Literal

from pydantic import BaseModel, Field


class Nie(BaseModel):
    p_marzy: Literal["nie"] = Field(
        "nie",
        title="Procedura Marży",
        json_schema_extra={"exclude_from_form": True}
    )
    p_marzy_n: bool = Field(
        True,
        title="Procedura Marży - Nie",
        description="Czy procedura Marży jest nieaktywna?",
        json_schema_extra={"exclude_from_form": True}
    )

class Tak(BaseModel):
    p_marzy: Literal["tak"] = Field(
        "tak",
        title="Procedura Marży",
        json_schema_extra={"exclude_from_form": True}
    )
    uslugi_turystyki: bool = False
    towary_uzywane: bool = False
    dziela_sztuki: bool = False
    przedm_kolekc_i_antyki: bool = False