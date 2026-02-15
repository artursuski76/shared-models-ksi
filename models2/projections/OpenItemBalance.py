class OpenItemBalance(BaseModel):
    counterparty_id: str
    total_open_amount: Decimal
    currency: str
