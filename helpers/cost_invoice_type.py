
from typing import Literal, List, Annotated, Union

from pydantic import BaseModel
from pydantic import Field, AliasChoices

from models2.enums_all.dane_fa_korygowanej import DaneFaKorygowanej
from models2.enums_all.typy_korekty import SkutekPodatkowyKorekty
from models2.helpers.TransactionRowCost import ImportTow33a, ImportTow33aInwentarz, ImportTow33aRelacja, ImportUslug28B, \
    ImportUslug28BRelacja, ImportUslugNie28B, ImportUslugNie28BRelacja, NabycieKrajowe, NabycieKrajoweInwentarz, \
    NabycieKrajoweRelacja, NiePodlega, NiePodlegaInwentarz, NiePodlegaRelacja, OOKrajTowar, OOKrajTowarInwentarz, \
    OOKrajTowarRelacja, OOKrajUsluga, OOKrajUslugaRelacja, WNT, WNTInwentarz, WNTRelacja, Wybierz


TransactionRow = Annotated[
    Union[
        Wybierz,
        ImportTow33a,
        ImportTow33aInwentarz,
        ImportTow33aRelacja,
        ImportUslug28B,
        ImportUslug28BRelacja,
        ImportUslugNie28B,
        ImportUslugNie28BRelacja,
        NabycieKrajowe,
        NabycieKrajoweInwentarz,
        NabycieKrajoweRelacja,
        NiePodlega,
        NiePodlegaInwentarz,
        NiePodlegaRelacja,
        OOKrajTowar,
        OOKrajTowarInwentarz,
        OOKrajTowarRelacja,
        OOKrajUsluga,
        OOKrajUslugaRelacja,
        WNT,
        WNTInwentarz,
        WNTRelacja,
    ],
    Field(discriminator="vat_category"),
]

class CostTransactionItemsBasic(BaseModel):
    transaction_items: List[TransactionRow] = Field(
        default_factory=list,
        alias="WierszTransakcji",
        title="Pozycje księgowania",
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        serialization_alias="transaction_items",
    )


class Podstawowa(CostTransactionItemsBasic):
    rodzaj_fv: Literal["Podstawowa"] = Field(
        "Podstawowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class Zaliczkowa(CostTransactionItemsBasic):
    rodzaj_fv: Literal["Zaliczkowa"] = Field(
        "Zaliczkowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )


class Rozliczeniowa(CostTransactionItemsBasic):
    rodzaj_fv: Literal["Rozliczeniowa"] = Field(
        "Rozliczeniowa",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

class Korekta(CostTransactionItemsBasic):
    rodzaj_fv: Literal["Korekta"] = Field(
        "Korekta",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )
    transaction_items_after: List[TransactionRow] = Field(
        default_factory=list,
        alias="WierszTransakcji",
        title="Pozycje księgowania",
        validation_alias=AliasChoices("transaction_items", "WierszTransakcji"),
        serialization_alias="transaction_items",
    )
    przyczyna_korekty: str = Field(
        default=None,
        alias="PrzyczynaKorekty",
        title="Przyczyna korekty"
    )
    typ_korekty: SkutekPodatkowyKorekty = Field(
        default=None,
        alias="TypKorekty",
        title="Typ korekty"
    )
    dane_fa_korygowanej: DaneFaKorygowanej = Field(
        default=None,
        alias="DaneFAKorygowane",
        title="Dane FA korygowane"
    )

