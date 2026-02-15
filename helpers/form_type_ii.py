from typing import Literal, Optional

from pydantic import BaseModel, Field



class Prosty(BaseModel):
    form_type_ii: Literal["prosty"] = Field(
        "prosty",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Rozbudowany(BaseModel):
    form_type_ii: Literal["rozbudowany"] = Field(
        "rozbudowany",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )



    suppliers_product_id: Optional[str] = Field(
        None,
        alias="suppliers_product_id"
    )

    shops_product_id: Optional[str] = Field(
        None,
        alias="shops_product_id"
    )

    ean: Optional[str] = Field(
        None,
        alias="ean13"
    )
    gtin: Optional[str] = Field(
        None,
        alias="gtin14"
    )
    isbn: Optional[str] = Field(
        None,
        alias="isbn13"
    )
    upc: Optional[str] = Field(
        None,
        alias="upc"
    )
    pkwiu2025: Optional[str] = Field(
        None,
        alias="pkwiu2025"
    )

    cn: Optional[str] = Field(
        None,
        alias="cn"
    )
