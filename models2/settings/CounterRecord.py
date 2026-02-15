from pydantic import Field

from models2.abase import BasicBasic


class CounterRecord(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "Counter",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        default="Settings:CounterRecord",
        title="Unikalny ID, np.: Settings:Firma",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    saleinvoice: int


    class FormConfig:
        prefill_initial_data = True

        list_view_fields = [
            "last_sync", "my_id", "sync_status"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "settings"
        collection = "counter_record"