from datetime import date
from typing import Annotated, Optional

from pydantic import BaseModel, Field, conint, StringConstraints, model_validator, root_validator

# --- Definicja typu dla kwot z ułamkiem (często 2 miejsca po przecinku) ---
KwotaPLN_Decimal = float



class SprzedazWiersz(BaseModel):
    """
    Model Pydantic dla pojedynczego wiersza ewidencji sprzedaży (JPK_V7),
    specyficzny dla transakcji z osobami fizycznymi (gdzie NrKontrahenta jest 'brak').
    Nazwa 'LFIZ' dodana dla odróżnienia.
    """

    # Numer kolejny wiersza
    LpSprzedazy: conint(ge=1)

    KodKrajuNadaniaTIN: Optional[
        Annotated[str, StringConstraints(min_length=2, max_length=2, pattern=r"[A-Z]{2}")]
    ] = None

    # W JPK_V7 dla osób fizycznych (sprzedaż paragonowa bez NIP) używana jest wartość "brak"
    NrKontrahenta: str

    # Nazwa lub Imię i Nazwisko kontrahenta
    NazwaKontrahenta: Annotated[str, StringConstraints(max_length=240)]

    # Numer faktury lub innego dowodu sprzedaży
    DowodSprzedazy: Annotated[str, StringConstraints(max_length=50)]

    # Data wystawienia dowodu sprzedaży
    DataWystawienia: date

    # Pola kwotowe (K_15 do K_32)
    # W deklaracji VAT-7/JPK_V7 M/K te pola oznaczają Podstawę Opodatkowania (K_15, K_17, K_19, K_21...)
    # i Podatek Należny (K_16, K_18, K_20, K_22...)

    K_15: KwotaPLN_Decimal = Field(..., alias="K_15")
    K_16: KwotaPLN_Decimal = Field(..., alias="K_16")
    K_17: KwotaPLN_Decimal = Field(..., alias="K_17")
    K_18: KwotaPLN_Decimal = Field(..., alias="K_18")
    K_19: KwotaPLN_Decimal = Field(..., alias="K_19", description="Podstawa opodatkowania 8%")
    K_20: KwotaPLN_Decimal = Field(..., alias="K_20", description="Podatek należny 8%")
    K_21: KwotaPLN_Decimal = Field(..., alias="K_21")
    K_22: KwotaPLN_Decimal = Field(..., alias="K_22")
    K_23: KwotaPLN_Decimal = Field(..., alias="K_23")
    K_24: KwotaPLN_Decimal = Field(..., alias="K_24")
    K_25: KwotaPLN_Decimal = Field(..., alias="K_25")
    K_26: KwotaPLN_Decimal = Field(..., alias="K_26")
    K_27: KwotaPLN_Decimal = Field(..., alias="K_27")
    K_28: KwotaPLN_Decimal = Field(..., alias="K_28")
    K_29: KwotaPLN_Decimal = Field(..., alias="K_29")
    K_30: KwotaPLN_Decimal = Field(..., alias="K_30")
    K_31: KwotaPLN_Decimal = Field(..., alias="K_31")
    K_32: KwotaPLN_Decimal = Field(..., alias="K_32")

    @model_validator(mode='before')
    def _normalize_and_enforce_b2c_rule(cls, data):
        # data może być dictem wejściowym do modelu (Pydantic v2)
        if isinstance(data, dict):
            nr = data.get('NrKontrahenta')
            kod = data.get('KodKrajuNadaniaTIN')

            # Normalizacja kodu: trim + upper
            if isinstance(kod, str):
                kod = kod.strip().upper()
                # Zamień puste/"0" na brak
                if kod == '' or kod == '0':
                    kod = None

            # Reguła: gdy NrKontrahenta == 'brak' → brak KodKrajuNadaniaTIN
            if isinstance(nr, str) and nr.strip().lower() == 'brak':
                data['KodKrajuNadaniaTIN'] = None
            else:
                # Dla B2B: jeżeli kod nie jest poprawny 2-literowy, ustaw brak
                if not (isinstance(kod, str) and len(kod) == 2 and kod.isalpha()):
                    kod = None
                data['KodKrajuNadaniaTIN'] = kod
        return data

    # Kompatybilność wsteczna z Pydantic v1
    @root_validator(pre=True)
    def _normalize_and_enforce_b2c_rule_v1(cls, values):
        if isinstance(values, dict):
            nr = values.get('NrKontrahenta')
            kod = values.get('KodKrajuNadaniaTIN')
            if isinstance(kod, str):
                kod = kod.strip().upper()
                if kod == '' or kod == '0':
                    kod = None
            if isinstance(nr, str) and nr.strip().lower() == 'brak':
                values['KodKrajuNadaniaTIN'] = None
            else:
                if not (isinstance(kod, str) and len(kod) == 2 and kod.isalpha()):
                    kod = None
                values['KodKrajuNadaniaTIN'] = kod
        return values





class SprzedazCtrl(BaseModel):
    LiczbaWierszySprzedazy: int
    PodatekNalezny: int


class ZakupWiersz(BaseModel):
    """
    Model Pydantic dla pojedynczego wiersza ewidencji zakupu (JPK_V7),
    dotyczący transakcji z firmami.
    """

    # Numer kolejny wiersza zakupu
    LpZakupu: conint(ge=1)

    # Kod Kraju Nadania NIP (TIN)
    KodKrajuNadaniaTIN: Annotated[str, StringConstraints(min_length=2, max_length=2, pattern=r"[A-Z]{2}")]

    # NIP dostawcy
    NrDostawcy: Annotated[str, StringConstraints(pattern=r"^[A-Z]{0,2}[A-Z0-9]{5,20}$")]

    # Pełna Nazwa dostawcy
    NazwaDostawcy: Annotated[str, StringConstraints(max_length=240)]

    # Numer dowodu zakupu (faktury)
    DowodZakupu: Annotated[str, StringConstraints(max_length=50)]

    # Data dokonania zakupu (lub otrzymania faktury)
    DataZakupu: date

    # Pola kwotowe (K_40 do K_43)

    K_40: KwotaPLN_Decimal = Field(..., alias="K_40",
                                   description="Podstawa opodatkowania 23% dla nabycia towarów/usług - odliczenie pełne")
    K_41: KwotaPLN_Decimal = Field(..., alias="K_41",
                                   description="Podatek naliczony 23% dla nabycia towarów/usług - odliczenie pełne")
    K_42: KwotaPLN_Decimal = Field(..., alias="K_42",
                                   description="Podstawa opodatkowania 8% dla nabycia towarów/usług - odliczenie pełne")
    K_43: KwotaPLN_Decimal = Field(..., alias="K_43",
                                   description="Podatek naliczony 8% dla nabycia towarów/usług - odliczenie pełne")



class ZakupCtrl(BaseModel):
    # Możesz chcieć użyć LiczbaWierszyZakupu, aby było zgodne z JPK:
    LiczbaWierszyZakupow: int

    # ZMIEŃ TO: NAZWA MUSI BYĆ ZGODNA Z DANYMI WEJŚCIOWYMI LUB JPK
    PodatekNaliczony: int  # Zmienione z PodatekNalezny na PodatekNaliczony




