from decimal import Decimal
from decimal import Decimal
from typing import Optional, Dict, Any, Set

from pydantic import BaseModel, Field, model_validator

from models.xxx.h_enums import PostingTags


class BaseItemTransactionBean(BaseModel):
    account: str = Field(title="Konto*")
    # narration_p: Optional[str] = Field(default=None, title="Opis")
    total: int = Field(title="Kwota*")
    commodity: str = Field(default="PLN", title="Waluta*")



class SimpleItems(BaseItemTransactionBean):
    pass

# class WithTags(SimpleItem):
#     tags: Set[PostingTags] = Field(
#         default_factory=set,
#         title="Tagi",
#         description="Wybierz jeden lub więcej tagów z dostępnej listy.",
#         json_schema_extra={
#             "form_widget": "checkbox_multiple"
#         }
#     )



# class InventoryPostingBean(BaseItemTransactionBean):
#     unit_price: int = Field(default=100, title="Cena jedn.")
#     quantity: Optional[int] = Field(default=1, title="Ilość")
#     fx_rate: Optional[int] = Field(default=10000, title="Kurs")
#     vat_proc: Optional[int] = Field(default=2300, title="Stawka")
#
#     total: int = Field(title="Kwota", json_schema_extra={"exclude_from_form": True})
#
#     @model_validator(mode='before')
#     @classmethod
#     def calculate_total_cost(cls, values: Dict[str, Any]) -> Dict[str, Any]:
#         # Jeśli total już podany — pozostaw
#         if 'total' in values and values['total'] is not None:
#             return values
#         unit_price = values.get('unit_price')
#         quantity = values.get('quantity')
#         if unit_price is not None and quantity is not None:
#             try:
#                 up = Decimal(str(unit_price))
#                 qty = Decimal(str(quantity))
#                 values['total'] = int((up * qty).quantize(Decimal("1")))
#             except:
#                 pass
#         return values