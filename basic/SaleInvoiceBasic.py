from __future__ import annotations

import secrets
from datetime import datetime, date, timezone
from typing import Union, Optional

from pydantic import ConfigDict
from pydantic import Field, model_validator, computed_field

from models2.abase import BasicBasic
from models2.enums import SourceInvoiceSource, SourceInvoiceStatus
from models2.helpers.forms_type_sales_inv import DostawaWDacieWystawienia, WspolnaDataDostawy, DostawaWOkresieCzasu
from models2.helpers.money import Money
from models2.helpers.procedury_marzy import Nie, Tak
from models2.xxx.h_enums import CurrencyAB


class SaleInvoiceBasic(BasicBasic):
    # files: List[TransactionFiles] = Field(default_factory=list)

    model_config = ConfigDict(populate_by_name=True, title="Formularz Dodawania Sale Invoice")

    date_sale: Union[
        DostawaWDacieWystawienia,
        DostawaWOkresieCzasu,
        WspolnaDataDostawy
    ] = Field(
        ...,
        discriminator='date_sale',
        alias="DataSprzedazy",
        title="Data sprzedaży",
        exclude=True
    )

    @computed_field(alias="date_sale")
    @property
    def date_sale_flat(self) -> str:
        return self.date_sale.date_sale

    @computed_field
    @property
    def common_date_sale(self) -> date | None:
        return getattr(self.date_sale, "common_date_sale", None)

    @computed_field
    @property
    def date_sale_from(self) -> date | None:
        return getattr(self.date_sale, "date_sale_from", None)

    @computed_field
    @property
    def date_sale_to(self) -> date | None:
        return getattr(self.date_sale, "date_sale_to", None)

    cash_method: bool = False
    self_billing: bool = False
    reverse_charge: bool = False
    split_payment: bool = False
    ec_simplified: bool = False

    p_marzy: Union[
        Nie,
        Tak
    ] = Field(
        ...,
        discriminator='p_marzy',
        alias="ProceduraMarzy",
        title="Procedura Marży",
        exclude=True
    )

    my_id: str = Field(  # Zmieniono z UUID na str
        default_factory=lambda: secrets.token_urlsafe(16),
        json_schema_extra={"exclude_from_form": True}
    )

    status: SourceInvoiceStatus = Field(
        SourceInvoiceStatus.DRAFT,
        title="Status",
        json_schema_extra = {"exclude_from_form": True}
    )

    source: SourceInvoiceSource = Field(
        SourceInvoiceSource.MANUAL,
        title="Zródło",
        json_schema_extra={"exclude_from_form": True}
    )

    counter: int = Field(
        default=0,
        json_schema_extra={"exclude_from_form": True}
    )

    date_posting: date = Field(
        default_factory=date.today,
        title="Data wystawienia",
        json_schema_extra={"exclude_from_form": True}
    )

    counterparty_id: str = Field(
        title="Kontrahent",
    )

    currency: CurrencyAB = Field(
        CurrencyAB,
        alias="Waluta",
        title="Waluta",
    )

    total_net: Money = Field(title="Razem Netto")
    total_vat: Money = Field(title="Razem VAT")
    total_gross: Money = Field(title="Razem Brutto")

    @model_validator(mode="after")
    def validate_totals(self) -> "SourceInvoice":
        # 1. Sprawdzenie równania: Netto + VAT = Brutto (z tolerancją 1 grosza)
        # Tutaj definiujemy zmienną pomocniczą:
        calculated_gross = self.total_net + self.total_vat

        if abs(self.total_gross - calculated_gross) > 1:
            raise ValueError(
                f"Błąd sumaryczny: Netto ({self.total_net}) + VAT ({self.total_vat}) "
                f"daje {calculated_gross}, a w Brutto wpisano {self.total_gross}. "
                f"Różnica przekracza 1 grosz."
            )

        return self



    ksef_ref: Optional[str] = Field(
        None,
        alias="KsefRef"
    )

    original_payload_ref: str = Field(
        None,
        title="Oryg Payload Ref",
        json_schema_extra = {"exclude_from_form": True}

    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # Dodaj import timezone z datetime
        json_schema_extra={"exclude_from_form": True}
    )