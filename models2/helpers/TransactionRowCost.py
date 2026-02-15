from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator

from models2.enums import CostRowType
from models2.helpers.money import Money


class TransactionRowBase(BaseModel):
    # cost_account: str = Field(title="Konto")
    row_type: CostRowType = Field(
        CostRowType,
        title="Typ pozycji"
    )
    amount_net: Money = Field(..., title="Netto")
    amount_vat: Money = Field(..., title="VAT")
    amount_gross: Money = Field(..., title="Brutto")
    nkup: bool = Field(False, title="NKUP")

    # @model_validator(mode="after")
    # def validate_math_base(self) -> "TransactionRowBase":
    #     # self.amount_net to np. 10000 (groszy)
    #     # self.amount_vat to np. 2300 (groszy)
    #
    #     if self.amount_net + self.amount_vat != self.amount_gross:
    #         raise ValueError(
    #             f"Suma Netto ({self.amount_net}) i VAT ({self.amount_vat}) != Brutto ({self.amount_gross})")
    #
    #     # Obliczamy VAT: (10000 * 23) / 100 = 2300
    #     # Używamy Decimal dla precyzyjnych obliczeń i zaokrąglania do groszy
    #     expected_vat_decimal = (Decimal(str(self.amount_net)) * Decimal(str(self.vat_rate_doc))) / Decimal("100")
    #     expected_vat = int(expected_vat_decimal.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    #
    #     # Tolerancja: 1 grosz + 0.01% kwoty netto (dla dużych faktur różnice zaokrągleń mogą być większe)
    #     tolerance = 2 + int(self.amount_net * 0.0001)
    #     if abs(self.amount_vat - expected_vat) > tolerance:
    #         raise ValueError(
    #             f"VAT ({self.amount_vat}) niezgodny ze stawką {self.vat_rate_doc}% (oczekiwano ok. {expected_vat}, tolerancja {tolerance})")
    #
    #     return self

class Wybierz(BaseModel):
    vat_category: Literal["wybierz"] = Field("wybierz", title="Wybierz typ pozycji...")

class ImportTow33a(TransactionRowBase):
    vat_category: Literal["import_tow_33a"] = "import_tow_33a"
    description: str = Field(
        None,
        title="Opis"
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportTow33aInwentarz(TransactionRowBase):
    vat_category: Literal["import_tow_33a_inwentarz"] = "import_tow_33a_inwentarz"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportTow33aRelacja(TransactionRowBase):
    vat_category: Literal["import_tow_33a_relacja"] = "import_tow_33a_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslug28B(TransactionRowBase):
    vat_category: Literal["import_uslug_28b"] = "import_uslug_28b"
    description: str = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslug28BRelacja(TransactionRowBase):
    vat_category: Literal["import_uslug_28b_relacja"] = "import_uslug_28b_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslugNie28B(TransactionRowBase):
    vat_category: Literal["import_uslug_nie_28b"] = "import_uslug_nie_28b"
    description: str = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class ImportUslugNie28BRelacja(TransactionRowBase):
    vat_category: Literal["import_uslug_nie_28b_relacja"] = "import_uslug_nie_28b_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class NabycieKrajowe(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe"] = "nabycie_krajowe"
    description: str = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NabycieKrajoweInwentarz(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe_inwentarz"] = "nabycie_krajowe_inwentarz"
    description: str = Field(
        None,
        title="Opis"
    )

    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NabycieKrajoweRelacja(TransactionRowBase):
    vat_category: Literal["nabycie_krajowe_relacja"] = "nabycie_krajowe_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=23, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23 ')
        return v



class NiePodlega(TransactionRowBase):
    vat_category: Literal["nie_podlega"] = "nie_podlega"
    description: str = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class NiePodlegaInwentarz(TransactionRowBase):
    vat_category: Literal["nie_podlega_inwentarz"] = "nie_podlega_inwentarz"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class NiePodlegaRelacja(TransactionRowBase):
    vat_category: Literal["nie_podlega_relacja"] = "nie_podlega_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v



class OOKrajTowar(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar"] = "oo_kraj_towar"
    description: str = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajTowarInwentarz(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar_inwentarz"] = "oo_kraj_towar_inwentarz"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajTowarRelacja(TransactionRowBase):
    vat_category: Literal["oo_kraj_towar_relacja"] = "oo_kraj_towar_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajUsluga(TransactionRowBase):
    vat_category: Literal["oo_kraj_usluga"] = "oo_kraj_usluga"
    description: str = Field(
        None,
        title="Opis"
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class OOKrajUslugaRelacja(TransactionRowBase):
    vat_category: Literal["oo_kraj_usluga_relacja"] = "oo_kraj_usluga_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )
    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 5, 7, 8, 22, 23')
        return v

class WNT(TransactionRowBase):
    vat_category: Literal["wnt"] = "wnt"
    description: str = Field(
        None,
        title="Opis"
    )


    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class WNTInwentarz(TransactionRowBase):
    vat_category: Literal["wnt_inwentarz"] = "wnt_inwentarz"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

class WNTRelacja(TransactionRowBase):
    vat_category: Literal["wnt_relacja"] = "wnt_relacja"
    description: str = Field(
        None,
        title="Opis"
    )
    inventory_item_id: str = Field(
        default=None,
        title="Kod inwent."
    )

    vat_rate_doc: int = Field(default=0, title="VAT_doc %")
    @field_validator('vat_rate_doc')
    @classmethod
    def check_vat_rate_doc(cls, v: float) -> float:
        if v not in [0]:
            raise ValueError('VAT rate must be exactly 0')
        return v

    vat_rate_jpk: Optional[int] = Field(
        default=23,
        title="VAT_jpk %"
    )
    @field_validator('vat_rate_jpk')
    @classmethod
    def check_vat_rate_jpk(cls, v: float) -> float:
        if v not in [0, 5, 7, 8, 22, 23]:
            raise ValueError('VAT rate must be exactly 0, 5, 7, 8, 22, 23')
        return v

#
# class PodatkiOplatyRecyklSrodow(TransactionRowBase):
#     row_type: Literal["podatki_oplaty_recyc_srodow"] = "podatki_oplaty_recyc_srodow"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class PodatkiOplatySadowe(TransactionRowBase):
#     row_type: Literal["podatki_oplaty_sadowe"] = "podatki_oplaty_sadowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class PodatkiOplatySkarbowe(TransactionRowBase):
#     row_type: Literal["podatki_oplaty_skarbowe"] = "podatki_oplaty_skarbowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class PodatkiOplatyTransportowe(TransactionRowBase):
#     row_type: Literal["podatki_transportowe"] = "podatki_transportowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class PodrozeSluzboweInne(TransactionRowBase):
#     row_type: Literal["podroze_sluzbowe_inne"] = "podroze_sluzbowe_inne"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class PodrozeSluzboweNoclegi(TransactionRowBase):
#     row_type: Literal["podroze_sluzbowe_noclegi"] = "podroze_sluzbowe_noclegi"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class PodrozeSluzboweOplatyDrogowe(TransactionRowBase):
#     row_type: Literal["podroze_sluzbowe_oplaty_drogowe"] = "podroze_sluzbowe_oplaty_drogowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class PodrozeSluzboweWyzywienie(TransactionRowBase):
#     row_type: Literal["podroze_sluzbowe_wyzywienie"] = "podroze_sluzbowe_wyzywienie"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class Reklama(TransactionRowBase):
#     row_type: Literal["reklama"] = "reklama"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class Reprezentacja(TransactionRowBase):
#     row_type: Literal["reprezentacja"] = "reprezentacja"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class SwiadczeniaNaRzeczPracownikow(TransactionRowBase):
#     row_type: Literal["swiad_na_rzecz_pracownikow"] = "swiad_na_rzecz_pracownikow"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UbezpMajatkowe(TransactionRowBase):
#     row_type: Literal["ubezpieczenia_majatkowe"] = "ubezpieczenia_majatkowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class UslugiObceDoradcze(TransactionRowBase):
#     row_type: Literal["usl_obce_doradcze"] = "usl_obce_doradcze"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceInformatyczne(TransactionRowBase):
#     row_type: Literal["usl_obce_informatyczne"] = "usl_obce_informatyczne"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceInne(TransactionRowBase):
#     row_type: Literal["usl_obce_inne"] = "usl_obce_inne"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceKsiegowe(TransactionRowBase):
#     row_type: Literal["usl_obce_ksiegowe"] = "usl_obce_ksiegowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceLeasingi(TransactionRowBase):
#     row_type: Literal["usl_obce_leasingi"] = "usl_obce_leasingi"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class UslugiObceNajmyCzynsze(TransactionRowBase):
#     row_type: Literal["usl_obce_najmy_czynsze"] = "usl_obce_najmy_czynsze"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     inventory_item_id: Optional[str] = Field(
#         default=None,
#         title="Kod inwent."
#     )
#
#
# class UslugiObcePrawne(TransactionRowBase):
#     row_type: Literal["usl_obce_prawne"] = "usl_obce_prawne"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceTelekomunikacyjne(TransactionRowBase):
#     row_type: Literal["usl_obce_telekomunikacyjne"] = "usl_obce_telekomunikacyjne"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class UslugiObceTransportowe(TransactionRowBase):
#     row_type: Literal["usl_obce_transportowe"] = "usl_obce_transportowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class WartoscSprzedanychTowarow(TransactionRowBase):
#     row_type: Literal["wartosc_sprzedanych_towarow"] = "wartosc_sprzedanych_towarow"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class ZaliczkiNaDostawy(TransactionRowBase):
#     row_type: Literal["zaliczki_na_dostawy"] = "zaliczki_na_dostawy"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class ZapasyTowarPL(TransactionRowBase):
#     row_type: Literal["zapasy_towar_pl"] = "zapasy_towar_pl"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class ZapasyTowarWDrodze(TransactionRowBase):
#     row_type: Literal["zapasy_towar_w_drodze"] = "zapasy_towar_w_drodze"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
# class ZdarzeniaLosowe(TransactionRowBase):
#     row_type: Literal["zdarzenia_losowe"] = "zdarzenia_losowe"
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#
#
#
# class INWENTARZ(TransactionRowBase):
#     row_type: Literal["inventory"] = "inventory"
#     inventory_item_id: str
#     description: str = Field(
#         None,
#         title="Opis"
#     )
#     quantity: int = Field(title="Ilość")
#     unit_price_net: Money = Field(title="Cena jednostkowa netto")  # Zmieniono na Money!
#
#     @model_validator(mode="after")
#     def validate_inventory_math(self) -> "INWENTARZ":
#         if self.quantity <= 0:
#             raise ValueError("Ilość musi być większa od zera")
#
#         # Wyliczamy cenę jednostkową w groszach
#         implied_net = self.unit_price_net * self.quantity
#         # W handlu często suma netto z pozycji różni się od (cena * ilość) o grosz przez zaokrąglenia
#         if abs(self.amount_net - implied_net) > self.quantity:  # Tolerancja zależna od skali
#             pass  # Tutaj zazwyczaj dopuszcza się korektę
#         return self
#
#


# class LandedCost(TransactionRowBase):
#     row_type: Literal["landed_cost"] = "landed_cost"
#     allocation_method: Literal["quantity", "value", "manual"]
#     allocation_scope: Literal["document", "inventory_item", "batches"]
#     inventory_item_id: Optional[str] = None
#     target_batch_ids: Optional[List[str]] = None