from datetime import date
from typing import Optional, Dict, Any

from pydantic import Field

from models.xxx.h_enums import RodzjaKontaKsiegowego, Currency
from models2.abase import BasicBasic
from models2.enums import ValuationMethod


class BookCostInvoice(BasicBasic):
    model_name: str = Field(
        "LedgerAccount",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    open_date: date = Field(
        title="Data ważności konta od w formacie: RRRR-MM-DD",
        description="Data otwarcia konta księgowego w formacie RRRR-MM-DD. Nie zmieniaj!",
        default="2025-01-01"
    )
    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )
    account_type: RodzjaKontaKsiegowego = Field(
        title="Prefiks/typ konta",
    )
    ccy: Currency = Field(
        Currency.PLN,
        title="Waluta konta"
    )
    is_inventory: bool

    valuation_method: ValuationMethod = Field(
        default=ValuationMethod.ND,
    )

    metadata: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        title="Metadane transakcji"

    )

    # Posting.account_id → LedgerAccount.my_id
    # InventoryMovement.inventory_account_id → LedgerAccount.my_id



    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "ledger_account"


