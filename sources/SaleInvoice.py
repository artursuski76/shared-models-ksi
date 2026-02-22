from typing import Annotated, Union

from pydantic import Field, computed_field, model_validator

from models2.basic.SaleInvoiceBasic import SaleInvoiceBasic
from models2.helpers.sale_invoice_type import Podstawowa, Zaliczkowa, Rozliczeniowa, Korekta

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


class SaleInvoice(SaleInvoiceBasic):
    rodzaj_fv: RodzajFV = Field(
        default=Podstawowa,
        discriminator='rodzaj_fv',
        alias="TypTransakcji",
        title="Typ transakcji",
        exclude=True
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



    @model_validator(mode="after")
    def validate_totals_integrity(self) -> "SaleInvoice":
        """
        Sprawdza czy sumy w nagłówku (z SaleInvoiceBasic)
        zgadzają się z sumą poszczególnych wierszy.
        """
        # Dla korekty sprawdzamy sumy jako różnicę między 'after' a 'before'
        if self.rodzaj_fv.rodzaj_fv == "Korekta":
            items_before = getattr(self.rodzaj_fv, "transaction_items", [])
            items_after = getattr(self.rodzaj_fv, "transaction_items_after", [])

            sum_net = sum(row.amount_net for row in items_after) - sum(row.amount_net for row in items_before)
            sum_vat = sum(row.amount_vat for row in items_after) - sum(row.amount_vat for row in items_before)
            sum_gross = sum(row.amount_gross for row in items_after) - sum(row.amount_gross for row in items_before)
        else:
            items = getattr(self.rodzaj_fv, "transaction_items", [])
            if not items:
                return self

            # Obliczamy sumy z wierszy
            sum_net = sum(row.amount_net for row in items)
            sum_vat = sum(row.amount_vat for row in items)
            sum_gross = sum(row.amount_gross for row in items)

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
            "counterparty_id", "currency", "my_id", "date_posting", "total_net",
            "total_vat", "total_gross", "rodzaj_fv_flat", "original_payload_ref", "status",
            "transaction_items", "transaction_items_after", "transaction_items_count"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "sale_invoice"