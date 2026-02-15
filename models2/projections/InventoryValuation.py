class InventoryValuation(BaseModel):
    item_id: str
    batch_id: str
    quantity_remaining: Decimal
    unit_cost: Decimal
    total_value: Decimal

    inventory_item_id: str
    total_quantity: Decimal
    total_value: Decimal
    valuation_method: str