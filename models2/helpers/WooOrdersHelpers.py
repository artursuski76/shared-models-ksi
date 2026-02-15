from typing import Optional, List, Any, Union
from pydantic import BaseModel, Field


class WooMetaData(BaseModel):
    id: Optional[int] = None
    key: Optional[str] = None
    value: Any = None
    display_key: Optional[str] = None
    display_value: Any = None


class WooBillingAndShipping(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company: Optional[str] = None
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postcode: Optional[str] = None
    country: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class WooLineItemsImage(BaseModel):
    id: Optional[Union[str, int]] = None
    src: Optional[str] = None


class WooLineItems(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    product_id: Optional[int] = None
    variation_id: Optional[int] = None
    quantity: Optional[int] = None
    tax_class: Optional[str] = None
    subtotal: Optional[str] = None
    subtotal_tax: Optional[str] = None
    total: Optional[str] = None
    total_tax: Optional[str] = None
    taxes: List[Any] = Field(default_factory=list)
    meta_data: List[WooMetaData] = Field(default_factory=list)
    sku: Optional[str] = None
    global_unique_id: Optional[str] = None
    price: Optional[Any] = None
    image: Optional[WooLineItemsImage] = None
    parent_name: Optional[str] = None


class WooShippingLines(BaseModel):
    id: Optional[int] = None
    method_title: Optional[str] = None
    method_id: Optional[str] = None
    instance_id: Optional[str] = None
    total: Optional[str] = None
    total_tax: Optional[str] = None
    taxes: List[Any] = Field(default_factory=list)
    meta_data: List[WooMetaData] = Field(default_factory=list)
    tax_status: Optional[str] = None

