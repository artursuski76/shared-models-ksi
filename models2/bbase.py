from typing import Optional, Dict, Any
from pydantic import Field
from models2.abase import BasicBasic


class BBaseBase(BasicBasic):
    model_name: str = Field(
        "BBaseBase",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Twój unikalny identyfikator (A-Z, a-z, 0-9, myślniki, np.: Abc-Sp-zoo-789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )

    description: str = Field(
        default=None,
    )

    metadata: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        title="Metadane transakcji"

    )


    class Config:
        title = "Formularz Dodawania BBaseBase"

    # ✅ WEWNĘTRZNA KLASA DO KONFIGURACJI FORMULARZA
    class FormConfig:
        """Metadane używane przez router do generowania widoku formularza."""
        page_title = "Nowy BBaseBase"
        header = "Utwórz nowe konto księgowe dla BBaseBase"

    class Couchbase:
        bucket = "Accounting"
        scope = "test"
        collection = "test"
