from datetime import date
from typing import Optional, Literal, Union, Dict, Any, Annotated

from pydantic import Field, BaseModel, model_serializer

from models2.xxx.h_enums import Currency, CurrencyAB
from models2.abase import BasicBasic
from models2.enums_all.FinancialTransactionDirection import FinancialTransactionDirection
from models2.helpers.money import Money



class FinancialTransactionSource(BasicBasic):

    model_name: str = Field(
        "FinancialTransactionSource",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        default="",
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Za-z0-9]+)*$",
        json_schema_extra={"exclude_from_form": True}
    )


    direct_checking_account: Optional[str] = Field(
        default=None,
        alias="direct_checking_account",
        title="Rozliczenie inne"
    )

    counterparty_id: Optional[str] = Field(
        default=None,
        alias="counterparty_id",
        title="Rozliczenie z kontrahentem"
    )

    financial_acc: str = Field(
        default=None,
        title="Konto księgowe"
    )

    date_posting: date = Field(
        ...,
        alias="date_posting",  # Wymuszenie poprawnej nazwy
        title="Data transakcji*"
    )

    amount: Money = Field(..., alias="amount", title="Amount*")
    ccy: Currency = Field(..., alias="ccy", title="Waluta*")
    direction: FinancialTransactionDirection = Field(FinancialTransactionDirection, alias="direction")
    cty_bank_acc: Optional[str] = Field(None, alias="cty_bank_acc", title="Konto bankowe kontrahenta", json_schema_extra={"exclude_from_form": True})
    cty_name: Optional[str] = Field(None, alias="cty_name", title="nazwa kontrahenta", json_schema_extra={"exclude_from_form": True})
    cty_address: Optional[str] = Field(None, alias="cty_address", title="Adres kontrahenta", json_schema_extra={"exclude_from_form": True})
    desc: Optional[str] = Field(None, title="Opis")
    desc_type: Optional[str] = Field(None, json_schema_extra={"exclude_from_form": True})
    orig_amount: Money = Field(..., alias="orig_amount", json_schema_extra={"exclude_from_form": True})
    orig_ccy: CurrencyAB = Field(..., alias="orig_ccy", json_schema_extra={"exclude_from_form": True})

    is_reconciled: bool = Field(default=False, title="Rozliczone")
    reconciliation_date: Optional[date] = Field(None, title="Data rozliczenia")
    source_raw_id: Optional[str] = Field(None, title="Link do Raw")

    class FormConfig:
        page_title = "Transakcje bankowe"
        header = "Lista Transakcje bankowe"

        list_view_fields = [
            "date_posting", "amount", "direction", "cty_name",
            "desc", "desc_type", "ccy"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "sources"
        collection = "bank_transaction"


