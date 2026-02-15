class VATRegister(BaseModel):
    journal_entry_id: str
    counterparty_id: str
    vat_rate: Decimal
    net_amount: Decimal
    vat_amount: Decimal
