from typing import List

from pydantic import BaseModel, Field

from models2.enums import AccountingTargetJPK


class JPKMapping(BaseModel):
    net: List[AccountingTargetJPK] = Field(
        default_factory=list,
        title="Netto",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )
    vat_due: List[AccountingTargetJPK] = Field(
        default_factory=list,
        title="vat_due",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )
    vat_input: List[AccountingTargetJPK] = Field(
        default_factory=list,
        title="vat_input",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )