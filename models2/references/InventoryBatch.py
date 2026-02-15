from datetime import date
from typing import Optional

from pydantic import Field

from models.xxx.h_enums import Currency
from models2.abase import BasicBasic


class InventoryBatch(BasicBasic):
    model_name: str = Field(
        "BBaseBase",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Twój unikalny identyfikator (A-Z, a-z, 0-9, myślniki, np.: Abc-Sp-zoo-789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    inventory_item_id: str

    received_date: date
    expiration_date: Optional[date]  # FEFO

    initial_quantity: int
    remaining_quantity: int

    initial_unit_cost: int
    current_unit_cost: int  # po landed cost
    allocated_total: int = 0

    ccy: Currency = Field(
        Currency.PLN,
        title="Waluta konta"
    )


# InventoryMovement.inventory_batch_id
# LandedCost → InventoryBatch
# CostAllocation → InventoryBatch

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "inventory_batch"
