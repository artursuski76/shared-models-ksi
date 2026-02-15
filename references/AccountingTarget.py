# from pydantic import Field
#
# from models2.abase import BasicBasic
# from models2.enums import VatCategoryTargetType, VatDirection
#
#
#
# class AccountingTarget(BasicBasic):
#     model_name: str = Field(
#         "AccountingTarget",
#         title="Nazwa Modelu",
#         json_schema_extra={"exclude_from_form": True}
#     )
#     my_id: VatCategoryTargetType = Field(
#         VatCategoryTargetType,
#         title="Kategoria VAT"
#     )
#
#     name: str = Field(title="Nazwa księgowa")
#
#     # 1️⃣ JPK VAT
#     jpk_v7: JPKMapping = Field(
#         default_factory=JPKMapping,
#         title="Mapowanie JPK_V7",
#         description="Mapowanie rodzajów kwot na pola JPK",
#         json_schema_extra={"required": False}  # Sygnał dla generatora formularzy
#     )
#
#     vat_direction: VatDirection
#
#     class Couchbase:
#         bucket = "Accounting"
#         scope = "references"
#         collection = "accounting_target"