import secrets
from typing import List

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import SourceInvoiceStatus, InvoiceType, SourceInvoiceSource
from models2.xxx.h_files import TransactionFiles


class FileCost(BasicBasic):
    model_name: str = Field(
        "FileCost",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(  # Zmieniono z UUID na str
        default_factory=lambda: secrets.token_urlsafe(16),
        json_schema_extra={"exclude_from_form": True}
    )

    inv_type: InvoiceType = Field(
        InvoiceType.PURCHASE,
        alias="TypFaktury",
        json_schema_extra={"exclude_from_form": True}
    )

    files: List[TransactionFiles] = Field(default_factory=list)

    status: SourceInvoiceStatus = Field(
        SourceInvoiceStatus.DRAFT,
        title="Status",
        json_schema_extra = {"exclude_from_form": True}
    )

    source: SourceInvoiceSource = Field(
        SourceInvoiceSource.MANUAL,
        title="Zródło",
        json_schema_extra={"exclude_from_form": True}
    )

    class FormConfig:
        page_title = "Koszty FileCost"
        header = "Lista kosztów FileCost"
        # Optymalizacja N1QL: pobieraj tylko te pola do listy
        list_view_fields = [
            "model_name", "my_id", "files", "created_at"
        ]
        default_sort_field = "created_at"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "file_cost"

