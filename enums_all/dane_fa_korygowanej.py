from datetime import date

from pydantic import Field, BaseModel


class DaneFaKorygowanej(BaseModel):
    data_wyst_fa_korygowanej: date = Field(
        default=None,
        alias="DataWystFaKorygowanej",
        title="Data wystawienia faktury korygowanej"
    )
    nr_fa_korygowanej: str = Field(
        default=None,
        alias="NrFAKorygowanej",
        title="Numer faktury korygowanej"
    )
    nr_ksef_fa_korygowanej: str = Field(
        default=None,
        alias="NrKsefFAKorygowanej",
        title="Numer Ksef faktury korygowanej"
    )
    nr_fa_korygowanej_w_ksef: str = Field(
        default=None,
        alias="NrFAKorygowanejWKsef",
        title="Numer faktury korygowanej w Ksef"
    )