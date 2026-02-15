from typing import Optional

from models2.abase import BasicBasic
from models2.enums import AllocationMethod


class CostAllocation(BasicBasic):

    allocation_id: str
    landed_cost_id: str

    inventory_batch_id: str

    allocated_amount: int
    currency: str
    allocation_method: Optional[AllocationMethod]
    basis_quantity: Optional[int]
    basis_value: Optional[int]
    basis_weight: Optional[int]

    # batch..

# InventoryBatch.current_unit_cost

    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "cost_allocation"
