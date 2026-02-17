from typing import Optional

from pydantic import Field

from models2.abase import BasicBasic


class IdentifierKsefCost(BasicBasic):
    type: str  # np. "Nip", "VatUe", "Other"
    value: str


class SellerKsefCostDoc(BasicBasic):
    nip: str
    name: Optional[str] = None


class BuyerKsefCostDoc(BasicBasic):
    identifier: IdentifierKsefCost
    name: Optional[str] = None


class KSeFCostDoc(BasicBasic):
    model_name: str = Field(
        "KSeFCostDoc",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        title="Unikalny ID (np. Numer KSeF)",
        pattern=r"^[A-Z0-9\-]+$",
        json_schema_extra={"exclude_from_form": True}
    )

    # KLUCZOWE POPRAWKI TYPÓW:
    ksefNumber: str = Field(title="Pełny numer KSeF")  # To jest string, np. "5265877635-20240321-..."
    invoiceNumber: str = Field(title="Numer faktury sprzedawcy")  # Może zawierać litery i ukośniki

    issueDate: str  # Format "YYYY-MM-DD"
    invoicingDate: str  # Format ISO "YYYY-MM-DDTHH:MM:SSZ"
    acquisitionDate: str
    permanentStorageDate: Optional[str] = None  # To jest data (string), nie bool!

    seller: SellerKsefCostDoc
    buyer: BuyerKsefCostDoc

    # Kwoty w JSON KSeF to liczby (number/double)
    netAmount: float = 0.0
    grossAmount: float = 0.0
    vatAmount: float = 0.0

    currency: str = "PLN"
    invoicingMode: Optional[str] = None  # "Online" / "Offline"
    invoiceType: Optional[str] = None  # "Vat", "Kor", "Zal"

    isSelfInvoicing: bool = False  # W JSON to boolean
    hasAttachment: bool = False  # W JSON to boolean
    invoiceHash: str

    class FormConfig:
        page_title = "Faktury kosztowe KSeF"
        header = "Lista faktur kosztowych KSeF"
        list_view_fields = [
            "seller.name", "issueDate", "invoiceNumber", "grossAmount",
            "currency", "invoiceType", "ksefNumber", "my_id", "status"
        ]
        default_sort_field = "issueDate"
        default_sort_dir = "DESC"

    class Couchbase:
        bucket = "Accounting"
        scope = "raw"
        collection = "ksef_cost"