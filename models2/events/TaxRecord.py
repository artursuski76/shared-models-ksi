# from pydantic import Field
#
# from models2.abase import BasicBasic
# from models2.enums import TaxRecordType, TaxRecordRegister
#
#
# class TaxRecord(BasicBasic):
#
#     model_name: str = Field(
#         "BBaseBase",
#         title="Nazwa Modelu",
#         json_schema_extra={"exclude_from_form": True}
#     )
#     my_id: str = Field(
#         title="Twój unikalny identyfikator (A-Z, a-z, 0-9, myślniki, np.: Abc-Sp-zoo-789)",
#         pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
#         description="Dozwolone tylko litery A-Z, a-z, cyfry 0-9 oraz myślniki. Zalecamy tax-id, pesel, ewentualnie nr-telefonu lub nazwę. Podana treść będzie głównym indeksem wyszukiwania klienta. Podanie istniejącego identyfikatora nadpisze dane w kartotece."
#     )
#
#     journal_entry_id: str
#
#     tax_type: TaxRecordType = Field(TaxRecordType, alias="type")
#     vat_rate: int
#
#     net_amount: int
#     tax_amount: int
#     gross_amount: int
#
#     register: TaxRecordRegister = Field(TaxRecordRegister, alias="register")
#     period_year: int
#     period_month: int
#
#     class Couchbase:
#         bucket = "Accounting"
#         scope = "events"
#         collection = "ledger_account"