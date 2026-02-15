from datetime import date

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import FinancialTransactionDirection


class FinancialTransactionEvent(BasicBasic):

    model_name: str = Field(
        "FinancialTransaction",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Twój unikalny identyfikator (A-Z, a-z, 0-9, myślniki, np.: Abc-Sp-zoo-789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )


    transaction_date: date

    amount: int
    currency: str

    counterparty_id: str
    direction: FinancialTransactionDirection = Field(
        default=FinancialTransactionDirection,
    )

    bank_account_id: str

    reference: str

    # RELATION:
    # SettlementCalculator
    # OpenItemResolver

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "financial_transactions"