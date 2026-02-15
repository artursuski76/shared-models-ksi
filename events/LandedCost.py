from datetime import date
from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import CostTypes, AllocationMethod


class LandedCost(BasicBasic):



    model_name: str = Field(
        "LandedCost",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Twój unikalny identyfikator (A-Z, a-z, 0-9, myślniki, np.: Abc-Sp-zoo-789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    journal_entry_id: str
    source_invoice_id: Optional[str]
    source_invoice_line_id: Optional[str]

    cost_type: CostTypes = Field(
        default=CostTypes.USLUGI_OBCE,
        title="Nazwa",
    )

    total_amount: int
    currency: str

    allocation_method: AllocationMethod = Field(
        default=AllocationMethod.QUANTITY,
    )
    allocation_date: Optional[date]

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "landed_cost"
