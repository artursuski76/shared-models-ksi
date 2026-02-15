from typing import Literal

from pydantic import BaseModel, Field



class OsobaNiefizyczna(BaseModel):

    nip: str
    pelna_nazwa: str
    email: str
    telefon: str

# ---------------------------------------------------------------------

class Podmiot1(BaseModel):

    rola: Literal["Podatnik"] = Field("Podatnik", alias="@rola")

    OsobaNiefizyczna: OsobaNiefizyczna