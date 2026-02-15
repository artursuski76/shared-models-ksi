
from typing import Literal, Optional, Annotated
from pydantic import BaseModel, Field, StringConstraints

# Definicje typów pomocniczych
KodPodatkuValue = Literal["VAT"]
RodzajZobowiazaniaValue = Literal["Z"]  # Z - zobowiązanie

PouczeniaValue = Literal[1]


class KodFormularzaDekl(BaseModel):
    """Model dla elementu KodFormularzaDekl (specyficzny dla deklaracji, np. VAT-7)."""

    # Atrybuty XML
    kodSystemowy: Annotated[str, StringConstraints(pattern=r"VAT-7 \(22\)")] = Field(..., alias="@kodSystemowy")
    kodPodatku: KodPodatkuValue = Field(..., alias="@kodPodatku")
    rodzajZobowiazania: RodzajZobowiazaniaValue = Field(..., alias="@rodzajZobowiazania")
    wersjaSchemy: Annotated[str, StringConstraints(pattern=r"1-0E")] = Field(..., alias="@wersjaSchemy")

    # Wartość tekstowa elementu
    value: Literal["VAT-7"] = Field(..., alias="#value")


class NaglowekDeklaracji(BaseModel):
    """Model Pydantic dla sekcji Naglowek specyficznej dla deklaracji VAT-7 w JPK_V7 (część deklaracyjna)."""

    KodFormularzaDekl: KodFormularzaDekl

    # Wariant Formularza, np. 22
    WariantFormularzaDekl: Literal[22]


# Wartości w polach deklaracji JPK_V7 są kwotami wyrażonymi w PLN,
# zaokrąglonymi do liczby całkowitej.
KwotaPLN = int


class PozycjeSzczegolowe(BaseModel):
    """
    Model Pydantic dla sekcji PozycjeSzczegolowe (sekcja Deklaracji)
    w JPK_V7M/K. Pola zawierają kwoty VAT i podstawy opodatkowania.
    """

    # Podatnik posiada prawo do obniżenia kwoty podatku należnego
    P_10: KwotaPLN = Field(..., alias="P_10", description="WDT")
    P_11: KwotaPLN = Field(..., alias="P_11",
                           description="Dostawa towarów oraz świadczenie usług na terytorium kraju, zwolnione")
    P_12: KwotaPLN = Field(..., alias="P_12")
    P_13: KwotaPLN = Field(..., alias="P_13")
    P_14: KwotaPLN = Field(..., alias="P_14")
    P_15: KwotaPLN = Field(..., alias="P_15")
    P_16: KwotaPLN = Field(..., alias="P_16")
    P_17: KwotaPLN = Field(..., alias="P_17", description="Podstawa opodatkowania 5%")
    P_18: KwotaPLN = Field(..., alias="P_18", description="Podatek należny 5%")
    P_19: KwotaPLN = Field(..., alias="P_19", description="Podstawa opodatkowania 8%")
    P_20: KwotaPLN = Field(..., alias="P_20", description="Podatek należny 8%")
    P_21: KwotaPLN = Field(..., alias="P_21")
    P_22: KwotaPLN = Field(..., alias="P_22")
    P_23: KwotaPLN = Field(..., alias="P_23")
    P_24: KwotaPLN = Field(..., alias="P_24")
    P_25: KwotaPLN = Field(..., alias="P_25")
    P_26: KwotaPLN = Field(..., alias="P_26")
    P_27: KwotaPLN = Field(..., alias="P_27")
    P_28: KwotaPLN = Field(..., alias="P_28")
    P_29: KwotaPLN = Field(..., alias="P_29")
    P_30: KwotaPLN = Field(..., alias="P_30")
    P_31: KwotaPLN = Field(..., alias="P_31")
    P_32: KwotaPLN = Field(..., alias="P_32")
    P_33: KwotaPLN = Field(..., alias="P_33")
    P_34: KwotaPLN = Field(..., alias="P_34")
    P_35: KwotaPLN = Field(..., alias="P_35")
    P_36: KwotaPLN = Field(..., alias="P_36")
    P_37: KwotaPLN = Field(..., alias="P_37", description="Podstawa opodatkowania 23%")
    P_38: KwotaPLN = Field(..., alias="P_38", description="Podatek należny 23%")
    P_39: KwotaPLN = Field(..., alias="P_39", description="Łączna kwota podstawy opodatkowania")
    P_40: KwotaPLN = Field(..., alias="P_40")
    P_41: KwotaPLN = Field(..., alias="P_41")
    P_42: KwotaPLN = Field(..., alias="P_42", description="WNT")
    P_43: KwotaPLN = Field(..., alias="P_43", description="Podatek należny od WNT")
    P_44: KwotaPLN = Field(..., alias="P_44")
    P_45: KwotaPLN = Field(..., alias="P_45")
    P_46: KwotaPLN = Field(..., alias="P_46")
    P_47: KwotaPLN = Field(..., alias="P_47")
    P_48: KwotaPLN = Field(..., alias="P_48",
                           description="WNT - import usług/dostawa, dla której podatnikiem jest nabywca")
    P_49: KwotaPLN = Field(..., alias="P_49")
    P_50: KwotaPLN = Field(..., alias="P_50")
    P_51: KwotaPLN = Field(..., alias="P_51")
    P_52: KwotaPLN = Field(..., alias="P_52")
    P_53: KwotaPLN = Field(..., alias="P_53", description="Kwota do zapłaty (P-53)")

    # P_62 jest często używane do podsumowania kwot do zwrotu/zapłaty.
    P_62: KwotaPLN = Field(..., alias="P_62", description="Kwota do zwrotu/przeniesienia (P-62)")


# --- Przykład użycia ---

# dane_pozycji = {
#     "P_10": 0, "P_11": 15000, "P_12": 0, "P_13": 0, "P_14": 0, "P_15": 0, "P_16": 0,
#     "P_17": 6089, "P_18": 487, "P_19": 9823, "P_20": 2259, "P_21": 0, "P_22": 0,
#     "P_23": 0, "P_24": 0, "P_25": 0, "P_26": 0, "P_27": 0, "P_28": 0, "P_29": 0,
#     "P_30": 0, "P_31": 0, "P_32": 0, "P_33": 0, "P_34": 0, "P_35": 0, "P_36": 0,
#     "P_37": 30912, "P_38": 2746, "P_39": 3584, "P_40": 0, "P_41": 0, "P_42": 13136,
#     "P_43": 2329, "P_44": 0, "P_45": 0, "P_46": 0, "P_47": 0, "P_48": 5913,
#     "P_49": 0, "P_50": 0, "P_51": 0, "P_52": 0, "P_53": 3167, "P_62": 3167,
# }
#
# # Walidacja danych
# try:
#     pozycje_model = PozycjeSzczegolowe(**dane_pozycji)
#     print("\n✅ Model PozycjeSzczegolowe został pomyślnie zweryfikowany.")
#     # print(pozycje_model.P_11) # 15000
# except Exception as e:
#     print(f"\n❌ Błąd walidacji: {e}")


class Deklaracja(BaseModel):
    """Model Pydantic dla deklaracji VAT-7 w JPK_V7M/K."""
    Naglowek: Optional[NaglowekDeklaracji] = None
    PozycjeSzczegolowe: PozycjeSzczegolowe
    Pouczenia: PouczeniaValue = Field(1, description="Pole informacyjne, zawsze równe 1.")



