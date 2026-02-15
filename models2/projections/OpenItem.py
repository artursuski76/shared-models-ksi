from datetime import date

from pydantic import Field

from models.xxx.h_enums import CurrencyAB
from models2.abase import BasicBasic


class OpenItem(BasicBasic):
    model_name: str = Field(
        "JournalEntry",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="ID (A-Z,a-z,0-9,:, np.: Abc-sp-zoo:NIP789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )
    source_document_id: str
    counterparty_id: str

    original_amount: int
    open_amount: int

    currency: CurrencyAB = Field(
        CurrencyAB.PLN,
        title="Waluta"
    )
    due_date: date
