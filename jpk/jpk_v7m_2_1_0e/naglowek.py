from datetime import datetime
from typing import Literal, Annotated

from pydantic import conint, StringConstraints
from pydantic_xml import BaseXmlModel, attr, element

# Stałe (bez zmian)
KodFormularzaValue = Literal["JPK_VAT"]
WariantFormularzaValue = Literal[2]
CelZlozeniaValue = Literal[1, 2]


class KodFormularzaElement(BaseXmlModel, tag="KodFormularza"):
    """
    Generuje <KodFormularza kodSystemowy="..." wersjaSchemy="...">JPK_VAT</KodFormularza>
    """
    kodSystemowy: str = attr(default="JPK_V7M (2)", pattern=r"JPK_V7M \(2\)")
    wersjaSchemy: str = attr(default="1-0E", pattern=r"1-0E")

    # W tej wersji pydantic-xml nie ma helpera `content`, więc ustawiamy tekst ręcznie
    def to_xml_tree(self, *, skip_empty: bool = False, exclude_none: bool = False, exclude_unset: bool = False):
        root = super().to_xml_tree(skip_empty=skip_empty, exclude_none=exclude_none, exclude_unset=exclude_unset)
        # Ustawiamy tekst elementu na stałą wartość
        root.text = "JPK_VAT"
        return root


# KLUCZOWA ZMIANA: Naglowek dziedziczy z BaseXmlModel i używa element()
class Naglowek(BaseXmlModel, tag="Naglowek"):
    KodFormularza: KodFormularzaElement = element()  # Użycie element()
    WariantFormularza: WariantFormularzaValue = element()
    DataWytworzeniaJPK: datetime = element()
    NazwaSystemu: Annotated[str, StringConstraints(max_length=255)] = element()

    # CelZlozenia z aliasem na potrzebę serializacji XML
    CelZlozenia: CelZlozeniaValue = element(tag="CelZlozenia")

    KodUrzedu: conint(ge=1000, le=9999) = element()
    Rok: conint(ge=2000) = element()
    Miesiac: conint(ge=1, le=12) = element()

