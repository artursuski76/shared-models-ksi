from typing import Annotated, Union, List

from pydantic import Field, AliasChoices, model_validator, computed_field

from models2.basic.CostInvoiceBasic import CostInvoiceBasic
from models2.helpers.cost_invoice_type import Podstawowa, Zaliczkowa, Rozliczeniowa, Korekta

RodzajFV = Annotated[
    Union[
        Podstawowa,
        Zaliczkowa,
        Rozliczeniowa,
        Korekta
    ],
    Field(
        discriminator="rodzaj_fv"
    )
]


class CostInvoice(CostInvoiceBasic):
    rodzaj_fv: RodzajFV = Field(
        default=Podstawowa,
        discriminator='rodzaj_fv',
        alias="TypTransakcji",
        title="Typ transakcji",
    )


    @computed_field(alias="rodzaj_fv")
    @property
    def rodzaj_fv_flat(self) -> str:
        return self.rodzaj_fv.rodzaj_fv

    model_name: str = Field(
        "CostInvoice",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    inv_type: str = Field(
        default="PURCHASE",
        json_schema_extra = {"exclude_from_form": True}
    )



    @model_validator(mode="after")
    def validate_totals_integrity(self) -> "CostInvoice":
        """
        Sprawdza czy sumy w nagłówku (z SourceInvoice)
        zgadzają się z sumą poszczególnych wierszy.
        """
        # 1. Najpierw wywołujemy walidację z klasy bazowej (Netto + VAT = Brutto)
        # Pydantic robi to automatycznie, ale tutaj skupiamy się na relacji nagłówek-wiersze.

        if not self.transaction_items:
            return self

        # Obliczamy sumy z wierszy
        sum_net = sum(row.amount_net for row in self.transaction_items)
        sum_vat = sum(row.amount_vat for row in self.transaction_items)
        sum_gross = sum(row.amount_gross for row in self.transaction_items)

        # 2. Porównanie z nagłówkiem (tolerancja 0, bo to liczby całkowite - grosze)
        if sum_net != self.total_net:
            raise ValueError(f"Suma Netto wierszy ({sum_net}) != Razem Netto ({self.total_net})")

        if sum_vat != self.total_vat:
            raise ValueError(f"Suma VAT wierszy ({sum_vat}) != Razem VAT ({self.total_vat})")

        if sum_gross != self.total_gross:
            raise ValueError(f"Suma Brutto wierszy ({sum_gross}) != Razem Brutto ({self.total_gross})")

        return self

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "counterparty_id", "inv_nr", "currency", "my_id", "date_posting", "total_net",
            "total_vat", "total_gross", "transaction_items"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "cost_invoice"

