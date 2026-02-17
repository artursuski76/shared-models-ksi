import datetime
from enum import Enum
from pydantic import Field
from typing import Optional

# Zakładam, że BasicBasic dostarcza podstawowej funkcjonalności modelu
from models2.abase import BasicBasic


class SyncStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    PENDING = "PENDING"


class KsefEnvironment(str, Enum):
    PROD = "PROD"
    TEST = "TEST"
    DEMO = "DEMO"


class KsefToken(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "KsefToken",
        json_schema_extra={"exclude_from_form": True}
    )

    # Rozszerzony wzorzec, by opcjonalnie zawierał NIP
    my_id: str = Field(
        default="Settings:KsefToken",
        title="Unikalny ID",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    nip: str = Field(..., title="NIP Firmy", pattern=r"^\d{10}$")
    ksef_token: str = Field(..., title="Token KSeF", description="Token autoryzacyjny wygenerowany w aplikacji KSeF")
    environment: KsefEnvironment = Field(default=KsefEnvironment.TEST, title="Środowisko")

    last_sync: Optional[datetime.datetime] = Field(None, title="Data ostatniej synchronizacji")
    sync_status: SyncStatus = Field(default=SyncStatus.PENDING, title="Status synchronizacji")
    last_error: Optional[str] = Field(None, title="Ostatni błąd", description="Treść błędu z API KSeF, jeśli wystąpił")

    class FormConfig:
        prefill_initial_data = True
        list_view_fields = [
            "nip", "environment", "last_sync", "sync_status"
        ]

    class Couchbase:
        bucket = "Accounting"
        scope = "settings"
        collection = "ksef_token"