from typing import Union, Optional

from pydantic import Field, computed_field

from models2.abase import BasicBasic
from models2.enums import InventoryItemUnit, SymbolGTU, InventoryItemActive, \
    VatOssCategory
from models2.helpers.FlattenMixin import FlattenMixin
from models2.helpers.form_type_ii import Prosty, Rozbudowany
from models2.helpers.item_type import PozycjaMagazynowa, Usluga, Produkt, SrodekTrwaly


class InventoryItem(BasicBasic, FlattenMixin):
    model_name: str = Field(
        "InventoryItem",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    form_type_ii: Union[
        Prosty,
        Rozbudowany
    ] = Field(
        ...,
        discriminator='form_type_ii',
        exclude=True,
        title="Rodzaj formularza*",
        json_schema_extra={"flatten": True}
    )

    item_type: Union[
        PozycjaMagazynowa,
        SrodekTrwaly,
        Usluga,
        Produkt
    ] = Field(
        ...,
        discriminator='item_type',
        exclude=True,
        title="Typ rekordu*",
        json_schema_extra={"flatten": True}
    )


    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331 *",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )
    name: str = Field(
        title="Nazwa*"
    )

    description: Optional[str] = Field(
        None,
        title="Opis"
    )

    gtu: SymbolGTU = Field(
        None,
        title="GTU"
    )

    vat_oss_category: VatOssCategory = Field(
        VatOssCategory.OTHER_ARTICLES,
        alias="vat_oss_category",
        title="Kategoria dla VAT-OSS*"
    )

    unit: InventoryItemUnit = Field(
        InventoryItemUnit,
        title="Jednostka miary*"
    )


    active: InventoryItemActive = Field(
        InventoryItemActive.BOTH,
        title="Aktywny w*"
    )

    class FormConfig:
        list_view_fields = [
            "my_id", "name", "gtu",
            "vat_oss_category", "unit", "active"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "inventory_item"