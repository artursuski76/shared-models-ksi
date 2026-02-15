from typing import List, Set, Dict, Any

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import AccountingRuleTrigger, VatCategoryTargetType, AccountingRuleAction


class AccountingRule(BasicBasic):
    model_name: str = Field(
        "AccountingRule",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="ID reguły",
        description="Unikalne ID reguły"
    )

    trigger: AccountingRuleTrigger = Field(
        title="Trigger reguły"
    )

    vat_categories: Set[VatCategoryTargetType] = Field(
        default_factory=set,
        title="Kategorie VAT",
    )

    conditions: Dict[str, Any] = Field(
        default_factory=dict,
        title="Warunki zastosowania reguły",
        description="Warunki WHEN (np. row.transaction_rows == ...)"
    )

    actions: List[AccountingRuleAction] = Field(
        None,
        title="actions",
        json_schema_extra={
            "form_widget": "select_multiple"
        }
    )

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "accounting_rule"