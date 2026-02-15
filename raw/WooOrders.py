from datetime import date
from typing import Optional, List, Any

from pydantic import Field

from models2.abase import BasicBasic
from models2.helpers.WooOrdersHelpers import WooBillingAndShipping, WooLineItems, WooShippingLines, WooMetaData



class WooOrders(BasicBasic):
    model_name: str = Field(
        "WooOrders",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331 *",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )


    id: Optional[int] = None
    parent_id: Optional[int] = None
    status: Optional[str] = None
    currency: Optional[str] = None
    version: Optional[str] = None
    prices_include_tax: Optional[bool] = None
    date_created: Optional[str] = None
    date_modified: Optional[str] = None
    discount_total: Optional[str] = None
    discount_tax: Optional[str] = None
    shipping_total: Optional[str] = None
    shipping_tax: Optional[str] = None
    cart_tax: Optional[str] = None
    total: Optional[str] = None
    total_tax: Optional[str] = None
    customer_id: Optional[int] = None
    order_key: Optional[str] = None

    billing: Optional[WooBillingAndShipping] = None
    shipping: Optional[WooBillingAndShipping] = None

    payment_method: Optional[str] = None
    payment_method_title: Optional[str] = None
    transaction_id: Optional[str] = None
    customer_ip_address: Optional[str] = None
    customer_user_agent: Optional[str] = None
    created_via: Optional[str] = None
    customer_note: Optional[str] = None
    date_completed: Optional[str] = None
    date_paid: Optional[str] = None
    cart_hash: Optional[str] = None
    number: Optional[str] = None

    meta_data: List[WooMetaData] = Field(default_factory=list)
    line_items: List[WooLineItems] = Field(default_factory=list)
    tax_lines: List[Any] = Field(default_factory=list)
    shipping_lines: List[WooShippingLines] = Field(default_factory=list)
    fee_lines: List[Any] = Field(default_factory=list)
    coupon_lines: List[Any] = Field(default_factory=list)
    refunds: List[Any] = Field(default_factory=list)

    payment_url: Optional[str] = None
    is_editable: Optional[bool] = None
    needs_payment: Optional[bool] = None
    needs_processing: Optional[bool] = None
    date_created_gmt: Optional[str] = None
    date_modified_gmt: Optional[str] = None
    date_completed_gmt: Optional[str] = None
    date_paid_gmt: Optional[str] = None
    currency_symbol: Optional[str] = None
    _links: Optional[Any] = None
    processed_at: Optional[date] = Field(
        None,
        title="Data przetworzenia zamówienia",
        json_schema_extra={"exclude_from_form": True}
    )

    inv_gen_at: Optional[date] = Field(
        None,
        title="Data przetworzenia zamówienia",
        json_schema_extra={"exclude_from_form": True}
    )

    class FormConfig:
        page_title = "Zlecenia WooCommerce"
        header = "Lista zleceń pobranych z WooCommerce"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "id", "number", "status", "total", "currency", 
            "date_created", "date_completed", "billing", "shipping", "payment_method_title",
            "last_sync", "my_id"
        ]
        default_sort_field = "date_completed"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "woo_orders_2"

