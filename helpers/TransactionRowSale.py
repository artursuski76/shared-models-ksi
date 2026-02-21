from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator

from models2.xxx.h_enums import EuropeLandsEnum
from models2.enums import TowarUsluga, InventoryItemUnit
from models2.helpers.money import Money


class TransactionRowBaseSale(BaseModel):
    tu: TowarUsluga = Field(
        default=None,
        title="T/U"
    )
    inventory_item_id: Optional[str] = Field(
        default=None,
        title="Kod inwent."
    )
    quantity: float = Field(title="Ilość")
    uom: InventoryItemUnit = Field(title="Jednostka miary")
    unit_price_net: Money = Field(title="Cena jednostkowa netto")  # Zmieniono na Money!

    description: str = Field(
        None,
        title="Opis"
    )
    amount_net: Money = Field(..., title="Netto")
    amount_vat: Money = Field(..., title="VAT")
    amount_gross: Money = Field(..., title="Brutto")

    @model_validator(mode="after")
    def validate_math_base(self) -> "TransactionRowBaseSale":
        # 1. Sprawdzenie Netto + VAT = Brutto
        if self.amount_net + self.amount_vat != self.amount_gross:
            raise ValueError(
                f"Suma Netto ({self.amount_net}) i VAT ({self.amount_vat}) != Brutto ({self.amount_gross})"
            )

        # 2. Sprawdzenie wyliczenia VAT na podstawie stawki, jeśli stawka jest dostępna
        vat_rate = getattr(self, "vat_rate_doc", None)
        if vat_rate is not None:
            # Obliczamy VAT: (netto * stawka) / 100
            expected_vat = (self.amount_net * vat_rate) / 100

            # Dopuszczamy błąd zaokrągleń - np. 2 grosze lub 1% przy dużych kwotach
            # (przy liczeniu od brutto mogą wystąpić większe różnice)
            tolerance = max(2, abs(expected_vat * 0.01))

            if abs(self.amount_vat - expected_vat) > tolerance:
                raise ValueError(
                    f"VAT ({self.amount_vat}) niezgodny ze stawką {vat_rate}% (oczekiwano ok. {expected_vat})"
                )

        return self


class Kraj5(TransactionRowBaseSale):
    vat_category: Literal["kraj_5"] = "kraj_5"

    # sale_account: SaleAccounts = Field(SaleAccounts, title="Konto")
    vat_rate_doc: int = Field(default=5, title="VAT_doc %")

    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [5]:
            raise ValueError('VAT rate must be exactly 5')
        return v

class Kraj8(TransactionRowBaseSale):
    vat_category: Literal["kraj_8"] = "kraj_8"

    vat_rate_doc: int = Field(default=8, title="VAT_doc %")

    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [7, 8]:
            raise ValueError('VAT rate must be exactly 7 or 8')
        return v

class KrajSTD(TransactionRowBaseSale):
    vat_category: Literal["kraj_std"] = "kraj_std"

    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [23, 22]:
            raise ValueError('VAT rate must be exactly 23 or 22')
        return v

class Kraj0(TransactionRowBaseSale):
    vat_category: Literal["kraj_0"] = "kraj_0"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class Kraj0Art129(TransactionRowBaseSale):
    vat_category: Literal["kraj_0_art129"] = "kraj_0_art129"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class KrajZW(TransactionRowBaseSale):
    vat_category: Literal["kraj_zw"] = "kraj_zw"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v


class PozaKrajem(TransactionRowBaseSale):
    vat_category: Literal["poza_krajem"] = "poza_krajem"

    # inventory_item_id: str
    # quantity: int = Field(title="Ilość")
    # unit_price_net: Money = Field(title="Cena jednostkowa netto")  # Zmieniono na Money!
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class WDU(TransactionRowBaseSale):
    vat_category: Literal["wdu"] = "wdu"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class EksportTowarow(TransactionRowBaseSale):
    vat_category: Literal["eksport_towarow"] = "eksport_towarow"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class KrajOdwObc(TransactionRowBaseSale):
    vat_category: Literal["kraj_odw_obc"] = "kraj_odw_obc"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class Marza(TransactionRowBaseSale):
    vat_category: Literal["marza"] = "marza"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

class OSS(TransactionRowBaseSale):
    vat_category: Literal["oss"] = "oss"

    vat_rate_doc: float = Field(
        default=0,
        title="VAT_doc %",
        json_schema_extra={"exclude_from_form": True}
    )
    vat_rate_oss: float = Field(default=..., title="VAT_OSS %")
    ctry_oss: EuropeLandsEnum = Field(default="", title="Kraj OSS")

class WDT(TransactionRowBaseSale):
    vat_category: Literal["wdt"] = "wdt"

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v
