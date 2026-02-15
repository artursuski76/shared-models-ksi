from typing import Optional, Union, List

from pydantic import Field

from models2.abase import BasicBasic
from models2.helpers.settings_api import WooCommerce, KSeFToken


class Api(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "Api",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        default="Settings:Api",
        title="Unikalny ID, np.: Settings:Firma",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    woo_apis: List[WooCommerce] = Field(
        None,
        alias="WooCommerceApis",
        title="WooCommerce APIs"
    )

    ksef_token: Optional[str] = Field(
        None,
        alias="KSeFToken",
        title="KSeF Token"
    )


    class FormConfig:
        prefill_initial_data = True

        list_view_fields = [
            "id", "name", "status", "tax_id", "currency",
            "date_created", "open_date", "tags",
            "last_sync", "my_id", "sync_status"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "settings"
        collection = "api"