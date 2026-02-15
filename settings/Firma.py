from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic


class Firma(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "Firma",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        default="Settings:Firma",
        title="Unikalny ID, np.: Settings:Firma",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )
    nip: str = Field()
    nazwa: str = Field()
    regon: Optional[str] = Field()
    krs: Optional[str] = Field()
    adr_ulica_nr_domu: str = Field()
    adr_kod_i_poczta: str = Field()
    dek_imie: str = Field()
    dek_nazwisko: str = Field()
    dek_tel: str = Field()
    dek_email: str = Field()
    dek_kod_us: str = Field()
    dek_nazwa_us: str = Field()

    ksef_token: Optional[str] = Field(default="")


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
        collection = "firma"