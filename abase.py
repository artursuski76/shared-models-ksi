from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from models2.enums import StatusBaseBase


class BasicBasic(BaseModel):
    __auto_id__ = True

    company_uuid: str = Field(
        json_schema_extra={"exclude_from_form": True}
    )
    company_id: str = Field(
        json_schema_extra={"exclude_from_form": True}
    )
    model_name: str = Field(
        json_schema_extra={"exclude_from_form": True}
    )
    created_at: datetime = Field(
        json_schema_extra={"exclude_from_form": True}
    )
    last_sync: datetime = Field(
        default_factory=datetime.now,
        json_schema_extra={"exclude_from_form": True}
    )
    status: Optional[StatusBaseBase] = Field(
        default=None,
        json_schema_extra={"exclude_from_form": True}
    )
    sha: Optional[str] = Field(
        default=None,
        json_schema_extra={"exclude_from_form": True}
    )

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Pobieramy nazwę klasy (np. "Posting")
        model_name = cls.__name__

        # 1. Automatyzacja pola model_name (domyślna wartość w Field)
        # Nadpisujemy pole w klasie potomnej, by domyślnie miało nazwę klasy
        if "model_name" in cls.__annotations__:
            cls.model_name = Field(
                model_name,
                title="Nazwa Modelu",
                json_schema_extra={"exclude_from_form": True}
            )

        # 2. Automatyzacja class Config
        if not hasattr(cls, "Config"):
            class Config: pass

            cls.Config = Config

        if not hasattr(cls.Config, "title") or "<<ModelName>>" in cls.Config.title:
            cls.Config.title = f"Formularz Dodawania {model_name}"

        # 3. Automatyzacja class FormConfig
        if not hasattr(cls, "FormConfig"):
            class FormConfig: pass

            cls.FormConfig = FormConfig

        # Dynamiczne ustawianie nagłówków
        cls.FormConfig.page_title = f"Nowy {model_name}"
        cls.FormConfig.header = f"Utwórz nowe konto księgowe dla {model_name}"

        # NOWE: domyślnie nie robimy prefill (żeby nie spowalniać zwykłych formularzy)
        if not hasattr(cls.FormConfig, "prefill_initial_data"):
            cls.FormConfig.prefill_initial_data = False