from datetime import date

from pydantic import Field

from models2.xxx.h_enums import Currency
from models2.abase import BasicBasic
from models2.enums import EntryType, SourceDocumentType


class JournalEntry(BasicBasic):

    __auto_id__ = True

    model_name: str = Field(
        "JournalEntry",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )
    my_id: str = Field(
        title="Unikalny ID (A-Z, a-z, 0-9, myślniki, np.: AbcSpZoo:PL789)",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        description="Dozwolone tylko litery A-Z, a-z",
        json_schema_extra={"exclude_from_form": True}
    )
    counter: int = Field(
        default=0,
        json_schema_extra={"exclude_from_form": True}
    )
    date_entry: date
    date_posting: date

    entry_type: EntryType = Field(
        default=EntryType
    )

    source_doc_type: SourceDocumentType = Field(
        default=SourceDocumentType.FV_VAT,
    )
    source_doc_id: str
    source_doc_nr: str


    ccy: Currency = Field(
        Currency.PLN,
        title="Waluta konta"
    )
    is_balanced: bool

    # Posting.journal_entry_id → JournalEntry.my_id
    # InventoryMovement.journal_entry_id → JournalEntry.my_id
    # TaxRecord.journal_entry_id → JournalEntry.my_id



    class Couchbase:
        bucket = "Accounting"
        scope = "events"
        collection = "journal_entry"