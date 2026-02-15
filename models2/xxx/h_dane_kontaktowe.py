from typing import Optional

from pydantic import BaseModel, Field


class DaneKontaktoweX(BaseModel):
    email: Optional[str] = Field(
        None,
        alias="Email",
        title="Email",
        max_length=100
    )
    telefon: Optional[str] = Field(
        None,
        alias="Telefon",
        title="Telefon",
        max_length=100
    )