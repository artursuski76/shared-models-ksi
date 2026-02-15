from datetime import date
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field

from models2.enums import Year, Month, Quarter
from models2.literal.typ_integracji import WooCommerce


class StatusyZamowienWooCommerce(str, Enum):
    COMPLETED = "completed"
    PROCESSING = "processing"
    ON_HOLD = "on-hold"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class Monthly(BaseModel):
    year: Year
    month: Month

class Quarterly(BaseModel):
    year: Year
    quarter: Quarter

class FromTo(BaseModel):
    date_from: date
    date_to: date

class FromToWC(BaseModel):
    date_created_from: date
    date_created_to: date
    date_completed_from: date
    date_completed_to: date
    status: StatusyZamowienWooCommerce = StatusyZamowienWooCommerce.COMPLETED


class JpkVat7M(Monthly):
    task_name: Literal["jpkvat7m"] = "jpkvat7m"


class VatOss(Quarterly):
    task_name: Literal["vat_oss"] = "vat_oss"

class PobierzZamowieniaWooCommerce(FromToWC):
    task_name: Literal["pobierz_zamowienia_woo_commerce"] = "pobierz_zamowienia_woo_commerce"
    store_url: str = Field(
        None,
        title="Adres sklepu Woo"
    )
    consumer_key: str = Field(
        None,
        title="Consumer key"
    )
    consumer_secret: str = Field(
        None,
        title="Consumer secret"
    )

class WystawFakturyDlaZamowienWooCommerce(BaseModel):
    task_name: Literal["wystaw_faktury_dla_zamowien_woocommerce"] = "wystaw_faktury_dla_zamowien_woocommerce"
    woo_commerce_api: WooCommerce
    range: FromToWC

