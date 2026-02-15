from datetime import date
from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import MovementType



class InventoryMovement(BasicBasic):
    movement_id: str
    journal_entry_id: str

    movement_type: MovementType = Field(
        default = MovementType.RECEIPT
    )

    inventory_item_id: str
    inventory_batch_id: Optional[str]

    quantity: int
    unit: str

    inventory_account_id: str  # LedgerAccount

    movement_date: date

    # InventoryBatch ← InventoryMovement
    # FIFO / FEFO liczone na odstawie movement_date

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "inventory_movement"