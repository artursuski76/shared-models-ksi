from typing import Union

from pydantic import Field

from models2.abase import BasicBasic
from models2.literal.typ_integracji import WooCommerce, FakturowniaPl


class Integration(BasicBasic):

    model_name: str = Field(
        "Counterparty",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
    )
    typ_integracji: Union[
        WooCommerce,
        FakturowniaPl
    ] = Field(
        ...,
        discriminator='typ_integracji',
        alias="typ_integracji",
        title="typ_integracji"
    )

    class Couchbase:
        bucket = "Accounting"
        scope = "references"
        collection = "integration"