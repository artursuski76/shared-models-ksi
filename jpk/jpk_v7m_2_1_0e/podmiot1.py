from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class OsobaNiefizyczna(BaseModel):
    """Model dla elementu OsobaNiefizyczna (dane firmy)."""

    # NIP: Należy zmienić z 'int' na 'str' z walidacją wzorca
    NIP: str

    # PelnaNazwa: Nazwa podmiotu, max 240 znaków
    PelnaNazwa: str = Field(..., max_length=240) # Dodano max_length dla lepszej walidacji

    # Email: Standardowy format
    Email: EmailStr

    # Telefon: Numer telefonu, max 35 znaków
    Telefon: str = Field(..., max_length=35)

# ---------------------------------------------------------------------

class Podmiot1(BaseModel):
    """Model Pydantic dla sekcji Podmiot1 (Podatnik)."""

    # 1. Użycie Literal["Podatnik"] Zapewnia, że jedyną dozwoloną wartością jest ta z XML.
    # 2. Field(default="Podatnik") Gwarantuje, że pole jest automatycznie ustawione.
    # 3. Field(alias="@rola") Jest konieczne do poprawnej serializacji XML.
    rola: Literal["Podatnik"] = Field("Podatnik", alias="@rola")

    # Właściwe dane podmiotu
    OsobaNiefizyczna: OsobaNiefizyczna