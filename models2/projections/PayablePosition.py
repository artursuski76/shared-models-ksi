class PayablePosition(BaseModel):
    counterparty_id: str
    open_items: list[OpenItem]
