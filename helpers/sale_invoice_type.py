
from typing import Literal, List, Annotated, Union

from pydantic import BaseModel
from pydantic import Field, AliasChoices
from models2.helpers.TransactionRowSale import (EksportTowarow, Kraj0, Kraj0Art129, KrajSTD, Kraj5, Kraj8,
                                                KrajOdwObc, KrajZW, Marza, OSS, PozaKrajem, WDT, WDU)


SaleTransactionRows = Annotated[
    Union[
        KrajSTD,
        Kraj8,
        Kraj5,
        KrajZW,
        Kraj0,
        Kraj0Art129,
        KrajOdwObc,
        EksportTowarow,
        Marza,
        OSS,
        PozaKrajem,
        WDT,
        WDU
    ],
    Field(discriminator="vat_category"),
]

class TransactionItemsBasic(BaseModel):
    transaction_items: List[SaleTransactionRows] = Field(
        default_factory=list,
        alias="WierszTransakcji",
        title="Pozycje księgowania",
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        serialization_alias="transaction_items",
    )


class Podstawowa(TransactionItemsBasic):
    rodzaj_fv: Literal["Podstawowa"] = Field(
        "Podstawowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class Zaliczkowa(TransactionItemsBasic):
    rodzaj_fv: Literal["Zaliczkowa"] = Field(
        "Zaliczkowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class Rozliczeniowa(TransactionItemsBasic):
    rodzaj_fv: Literal["Rozliczeniowa"] = Field(
        "Rozliczeniowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Korekta(TransactionItemsBasic):
    rodzaj_fv: Literal["Korekta"] = Field(
        "Korekta",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    transaction_items_after: List[SaleTransactionRows] = Field(
        default_factory=list,
        alias="WierszTransakcjiPoKorekcie",
        title="Pozycje księgowania po korekcie",
        validation_alias=AliasChoices("transaction_items_after", "WierszTransakcjiPoKorekcie"),
        serialization_alias="transaction_items_after",
    )

