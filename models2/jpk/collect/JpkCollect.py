from datetime import date
from typing import List

from pydantic import BaseModel, Field

from models2.abase import BasicBasic

class JpkSalesLine(BaseModel):
    lp: int
    tin: str
    tax_id: str
    counterparty_name: str
    counterparty_id: str
    inv_nr: str
    date_issue: date
    currency: str
    exchange_rate: float
    exchange_rate_date: date
    K_15: int
    K_16: int
    K_17: int
    K_18: int
    K_19: int
    K_20: int
    K_21: int
    K_22: int
    K_23: int
    K_24: int
    K_25: int
    K_26: int
    K_27: int
    K_28: int
    K_29: int
    K_30: int
    K_31: int
    K_32: int

class JpkSalesSummary(BaseModel):
    rows: int = 0
    net: int = 0
    tax: int = 0

class JpkPurchasesLine(BaseModel):
    lp: int
    tin: str
    tax_id: str
    counterparty_name: str
    counterparty_id: str
    inv_nr: str
    date_issue: date
    currency: str
    exchange_rate: float
    exchange_rate_date: date
    K_40: int
    K_41: int
    K_42: int
    K_43: int


class JpkPurchasesSummary(BaseModel):
    rows: int = 0
    net: int = 0
    tax: int = 0



class JpkSummary(BaseModel):
    P_10: int = 0
    P_11: int = 0
    P_12: int = 0
    P_13: int = 0
    P_14: int = 0
    P_15: int = 0
    P_16: int = 0
    P_17: int = 0
    P_18: int = 0
    P_19: int = 0
    P_20: int = 0
    P_21: int = 0
    P_22: int = 0
    P_23: int = 0
    P_24: int = 0
    P_25: int = 0
    P_26: int = 0
    P_27: int = 0
    P_28: int = 0
    P_29: int = 0
    P_30: int = 0
    P_31: int = 0
    P_32: int = 0
    P_33: int = 0
    P_34: int = 0
    P_35: int = 0
    P_36: int = 0
    P_37: int = 0
    P_38: int = 0
    P_39: int = 0
    P_40: int = 0
    P_41: int = 0
    P_42: int = 0
    P_43: int = 0
    P_44: int = 0
    P_45: int = 0
    P_46: int = 0
    P_47: int = 0
    P_48: int = 0
    P_49: int = 0
    P_50: int = 0
    P_51: int = 0
    P_52: int = 0
    P_53: int = 0
    P_62: int = 0

class JpkCollect(BaseModel):
    period_year: int
    period_month: int
    summary: JpkSummary = Field(default_factory=JpkSummary)
    sales: List[JpkSalesLine] = Field(default_factory=list)
    sales_summary: JpkSalesSummary = Field(default_factory=JpkSummary)
    purchases: List[JpkPurchasesLine] = Field(default_factory=list)
    purchases_summary: JpkPurchasesSummary = Field(default_factory=JpkSummary)

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "id", "period_year", "period_month", "total", "my_id"
        ]
        default_sort_field = "my_id"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "projections"
        collection = "jpk_collect"