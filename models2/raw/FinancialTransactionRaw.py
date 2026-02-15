from datetime import date
from typing import Optional

from models2.xxx.h_enums import Currency, CurrencyAB
from models2.abase import BasicBasic
from pydantic import Field

from models2.enums_all.FinancialTransactionDirection import FinancialTransactionDirection
from models2.helpers.money import Money


class FinancialTransactionRaw(BasicBasic):

    model_name: str = Field(
        "BankTransactionRaw",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        default="",
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Za-z0-9]+)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    financial_acc: str = Field(
        default=None,
        title="Konto księgowe banku/kasy"
    )

    date_posting: date = Field(
        ...,
        alias="date_posting",  # Wymuszenie poprawnej nazwy
        title="Data transakcji*",
        json_schema_extra={"order": 1}
    )
    date_bookg: date = Field(
        ...,
        alias="date_bookg",  # Wymuszenie poprawnej nazwy
        title="Data księgowania w banku",
        json_schema_extra={"order": 2}
    )
    amount: Money = Field(..., alias="amount", title="Amount*", json_schema_extra={"order": 3})
    ccy: Currency = Field(..., alias="ccy", title="Waluta*", json_schema_extra={"order": 4})
    direction: FinancialTransactionDirection = Field(FinancialTransactionDirection, alias="direction", title="Kierunek*", json_schema_extra={"order": 5})
    cty_bank_acc: Optional[str] = Field(None, alias="cty_bank_acc", title="Konto bankowe kontrahenta", json_schema_extra={"order": 6})
    cty_name: Optional[str] = Field(None, alias="cty_name", title="nazwa kontrahenta", json_schema_extra={"order": 7})
    cty_address: Optional[str] = Field(None, alias="cty_address", title="Adres kontrahenta", json_schema_extra={"order": 8})
    desc: Optional[str] = Field(None, alias="desc", title="Opis")
    desc_type: Optional[str] = Field(None, alias="desc_type", title="Typ transakcji")
    orig_amount: Money = Field(..., alias="orig_amount", title="Kwota zlecenia")
    orig_ccy: CurrencyAB = Field(..., alias="orig_ccy", title="Waluta zlecenia")


    class FormConfig:
        page_title = "Transakcje bankowe"
        header = "Lista Transakcje bankowe"

        list_view_fields = [
            "cparty_acc", "date_posting", "amount", "direction", "cty_name",
            "desc", "desc_type", "ccy"
        ]
        default_sort_field = "date_posting"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "bank_transaction"


