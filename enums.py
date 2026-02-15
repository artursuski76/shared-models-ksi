from enum import Enum


class StatusBaseBase(str, Enum):
    POSTED = "POSTED"
    DRAFT = "DRAFT"
    VOID = "VOID"
    PROCESSED = "PROCESSED"

class ValuationMethod(str, Enum):
    FIFO = "FIFO"
    ND = "ND"


class EntryType(str, Enum):
    INVENTORY_SALE = "INVENTORY_SALE"
    INVOICE_PURCHASE = "INVOICE_PURCHASE"
    INVENTORY_RECEIPT = "INVENTORY_RECEIPT"
    INVENTORY_ISSUE = "INVENTORY_ISSUE"
    PAYMENT = "PAYMENT"
    IMPORT = "IMPORT"
    VAT = "VAT"
    ADJUSTMENT = "ADJUSTMENT"

class SourceDocumentType(str, Enum):
    FV_VAT = "FV_VAT"
    FV_NO_VAT = "FV_NO_VAT"
    RECEIPT = "RECEIPT"
    WZ = "WZ"
    PZ = "PZ"
    SAD = "SAD"


class MovementType(str, Enum):
    RECEIPT = "RECEIPT"
    ISSUE = "ISSUE"
    ADJUSTMENT = "ADJUSTMENT"
    TRANSFER = "TRANSFER"

class CostTypes(str, Enum):
    AMORTYZACJA = "AMORTYZACJA"
    PODATKI_OPLATY = "PODATKI_OPLATY"
    AKCYZA = "AKCYZA"
    POZOSTALE_RODZAJOWE = "POZOSTALE_RODZAJOWE"
    UBEZPIECZENIA_SPOLECZNE = "UBEZPIECZENIA_SPOLECZNE"
    UBEZPIECZENIA_EMERYTALNE ="UBEZPIECZENIA_EMERYTALNY"
    USLUGI_OBCE ="USLUGI_OBCE"
    WART_SPRZ_TOWAROW ="WART_SPRZ_TOWAROW"
    WYNAGRODZENIA = "WYNAGRODZENIA"
    ZUZYCIE_MATERIALOW_ENERGII ="ZUZYCIE_MATERIALOW_ENERGII"
    AKTU_WART_AKT_NIEFIN = "AKTU_WART_AKT_NIEFIN"
    INNE_OPERACYJNE ="INNE_OPERACYJNE"
    STRATA_ZE_ZBYCIA_NIEF_AKT_TRW ="STRATA_ZE_ZBYCIA_NIEF_AKT_TRW"
    AKTU_WART_AKT_FIN = "AKTU_WART_AKT_FIN"
    INNE_KOSZTY_FINANSOWE ="INNE_KOSZTY_FINANSOWE"
    ODSETKI ="ODSETKI"
    STRATA_Z_TYT_ROZCH_AKT_FIN = "STRATA_Z_TYT_ROZCH_AKT_FIN"

class AllocationMethod(str, Enum):
    QUANTITY = "QUANTITY"
    VALUE = "VALUE"
    WEIGHT = "WEIGHT"

class FinancialTransactionDirection(str, Enum):
    IN = "IN"
    OUT = "OUT"

class TaxRecordRegister(str, Enum):
    sales = "sales"
    purchase = "purchase"

class TaxRecordType(str, Enum):
    VAT = "VAT"
    WHT = "WHT"
    CUSTOMS = "CUSTOMS"

class InventoryItemUnit(str, Enum):
    SZT = "Szt"
    H = "H"
    JEDN = "Jedn"
    KG = "Kg"
    KM = "Km"
    KWH = "KWH"
    LTR = "Ltr"
    M2 = "M2"
    M3 = "M3"
    MIES = "Mies"

class CounterpartyType(str, Enum):
    CUSTOMER = "CUSTOMER",          # odbiorca (sprzedaż)
    VENDOR = "VENDOR",          # dostawca (zakup)
    BOTH = "BOTH",              # klient i dostawca
    # BANK = "BANK",              # bank / rachunek bankowy
    # TAX_OFFICE = "TAX_OFFICE",        # US / urząd celny
    # CUSTOMS_BROKER = "CUSTOMS_BROKER",    # agencja celna
    # LOGISTICS = "LOGISTICS",         # firma transportowa / spedycja
    # INSURANCE = "INSURANCE",         # ubezpieczyciel
    # EMPLOYEE = "EMPLOYEE",          # pracownik
    # CONTRACTOR = "CONTRACTOR",        # zleceniobiorca / B2B
    # OWNER = "OWNER",             # właściciel / wspólnik
    # INTERNAL = "INTERNAL",          # podmiot wewnętrzny (inne spółki)
    # MANAGER = "MANAGER",
    # OTHER = "OTHER"




class SymbolGTU(str, Enum):
    GTU_01 = "GTU_01"
    GTU_02 = "GTU_02"
    GTU_03 = "GTU_03"
    GTU_04 = "GTU_04"
    GTU_05 = "GTU_05"
    GTU_06 = "GTU_06"
    GTU_07 = "GTU_07"
    GTU_08 = "GTU_08"
    GTU_09 = "GTU_09"
    GTU_10 = "GTU_10"
    GTU_11 = "GTU_11"
    GTU_12 = "GTU_12"
    GTU_13 = "GTU_13"


class InventoryItemType(str, Enum):
    POZYCJA_MAGAZYNOWA = "Pozycja_Magazynowa"
    USLUGA = "Usluga"
    PRODUKT = "Produkt"
    # PODZIAL_KOSZTU_NA_POZ_MAG = "PODZIAL_KOSZTU_NA_POZ_MAG"
    # USLUGI_BUDOWLANE_EU = "USLUGI_BUDOWLAE_EU"
    # IMPORT_USLUG_SPOZA_EU = "IMPORT_USLUG_SPOZA_EU"

class InventoryItemActive(str, Enum):
    SALES = "SALES"
    PURCHASE = "PURCHASES"
    BOTH = "BOTH"
    ARCHIVED = "ARCHIVED"


class VatOssCategory(str, Enum):
    MEDICINES_URPL_ORAL = "Medicines_URPL_Oral"
    MEDICINES_URPL_TYPICAL = "Medicines_URPL_Typical"
    MEDICAL_DEVICES_MDR_CE = "MedicalDevices_MDR_CE"
    SUPPLEMENTS_CN2106 = "Supplements_CN2106"
    HYGIENE_PRODUCTS_CN9619 = "FeminineHygiene_CN9619"
    OTHER_ARTICLES = "Other_Articles"

class AccountingTargetType(str, Enum):
    SALES = "SALES"
    PURCHASE = "PURCHASES"

class VatCategoryTargetType(str, Enum):
    DELIVERY_DOMESTIC_EXEMPT = "DELIVERY_DOMESTIC_EXEMPT"
    DELIVERY_VAT_OUTSIDE = "DELIVERY_VAT_OUTSIDE"
    DELIVERY_EU_SERVICES_ART100 = "DELIVERY_EU_SERVICES_ART100"

    DELIVERY_DOMESTIC_0 = "DELIVERY_DOMESTIC_0"
    DELIVERY_DOMESTIC_0_ART129 = "DELIVERY_DOMESTIC_0_ART129"

    DELIVERY_DOMESTIC_5 = "DELIVERY_DOMESTIC_5"
    DELIVERY_DOMESTIC_8 = "DELIVERY_DOMESTIC_8"
    DELIVERY_DOMESTIC_STD = "DELIVERY_DOMESTIC_STD "

    DELIVERY_VAT_OSS = "DELIVERY_VAT_OSS"

    ICS_WDT = "ICS_WDT"
    EXPORT_GOODS = "EXPORT_GOODS"

    ICA_WNT = "WNT"
    ICA_WNT_GOODS = "WNT_MAG"
    ICA_WNT_FIXED_ASSET = "WNT_SR_TRW"
    ICA_WNT_FIXED_ASSET_TRANSPORT = "WNT_SR_TRW_TRANS"

    ACQUISITION_DOMESTIC = "NABYCIE_KRAJOWE"
    ACQUISITION_DOMESTIC_FIXED_ASSET = "NABYCIE_KRAJOWE_SR_TRW"

    IMPORT_GOODS_ART33A = "IMPORT_TOWAR_ART33A"
    IMPORT_GOODS_ART33A_WARE = "IMPORT_TOWAR_ART33A_MAG"
    IMPORT_SERVICES_NON_28B = "IMPORT_USL_NIE_28B"
    IMPORT_SERVICES_28B = "IMPORT_USL_28B"

    REVERSE_CHARGE_DOMESTIC_GOODS = "ODWROTNE_OBCIAZENIE_KRAJ_TOWAR"
    REVERSE_CHARGE_DOMESTIC_SERVICES = "ODWROTNE_OBCIAZENIE_KRAJ_USLUGI"

    VAT_ADJUSTMENT_ART14_INVENTORY = "VAT_ADJUSTMENT_ART14_INVENTORY" # spis z natury, remament
    VAT_ADJUSTMENT_CASH_REGISTER_REFUND = "VAT_ADJUSTMENT_CASH_REGISTER_REFUND" # odpis za zakup kasy fiskalnej

#####################################################################

class VatCostCategoryTargetType(str, Enum):

    NIE_PODLEGA = "NIE_PODLEGA"
    NABYCIE_KRAJOWE = "NABYCIE_KRAJOWE"
    NABYCIE_KRAJOWE_SR_TRW = "NABYCIE_KRAJOWE_SR_TRW"

    IMPORT_USL_NIE_28B = "IMPORT_USL_NIE_28B"
    IMPORT_USL_28B = "IMPORT_USL_28B"

    WNT = "WNT"
    WNT_SR_TRW = "WNT_SR_TRW"
    WNT_SR_TRW_TRANS = "WNT_SR_TRW_TRANS"

    IMPORT_TOW_ART33A = "IMPORT_TOW_ART33A"
    IMPORT_TOW_ART33A_SR_TRW = "IMPORT_TOW_ART33A_SR_TRW"


    NABYCIE_OO_KRAJ_TOWAR = "NABYCIE_OO_KRAJ_TOWAR"
    NABYCIE_OO_KRAJ_USLUGI = "NABYCIE_OO_KRAJ_USLUGI"

class CostRowType(str, Enum):
    DAROWIZNY = "darowizny"
    ENERGIA_CIEPLNA = "energia_cieplna"
    ENERGIA_GAZ = "energia_gaz"
    ENERGIA_INNA = "energia_inna"
    ENERGIA_OLEJ_OPALOWY = "energia_olej_opalowy"
    ENERGIA_PALIWA_SILNIKOWE = "energia_paliwa_silnikowe"
    ENERGIA_PRAD_ELEKTRYCZNY = "energia_prad_elektryczny"
    ENERGIA_WODA_SCIEKI = "energia_woda_scieki"
    INNE_FINANSOWE = "inne_finansowe"
    INNE_OPERACYJNE = "inne_operacyjne"
    INNE_RODZAJOWE = "inne_rodzajowe"
    KARY_GRZYWNY_MANDATY = "kary_grzywny_mandaty"
    MATERIALY_BIUROWE = "materialy_biurowe"
    MATERIALY_CZESCI_ZAMIENNE = "materialy_czesci_zamienne"
    MATERIALY_PRODUKCYJNE = "materialy_produkcyjne"
    ODSETKI_BANKOWE = "odsetki_bankowe"
    ODSETKI_BUDZETOWE = "odsetki_budzetowe"
    ODSETKI_HANDLOWE = "odsetki_handlowe"
    PODATKI_AKCYZOWE = "podatki_akcyzowe"
    PODATKI_OD_NIERUCHOMOSCI = "podatki_od_nieruchomosci"
    PODATKI_OPLATY_INNE = "podatki_oplaty_inne"
    PODATKI_OPLATY_RECYC_SRODOW = "podatki_oplaty_recyc_srodow"
    PODATKI_OPLATY_SADOWE = "podatki_oplaty_sadowe"
    PODATKI_OPLATY_SKARBOWE = "podatki_oplaty_skarbowe"
    PODATKI_TRANSPORTOWE = "podatki_transportowe"
    PODROZE_SLUZBOWE_INNE = "podroze_sluzbowe_inne"
    PODROZE_SLUZBOWE_NOCLEGI = "podroze_sluzbowe_noclegi"
    PODROZE_SLUZBOWE_OPLATY_DROGOWE = "podroze_sluzbowe_oplaty_drogowe"
    PODROZE_SLUZBOWE_WYZYWIENIE = "podroze_sluzbowe_wyzywienie"
    REKLAMA = "reklama"
    REPREZENTACJA = "reprezentacja"
    SWIAD_NA_RZECZ_PRACOWNIKOW = "swiad_na_rzecz_pracownikow"
    UBEZPIECZENIA_MAJATKOWE = "ubezpieczenia_majatkowe"
    USL_OBCE_DORADCZE = "usl_obce_doradcze"
    USL_OBCE_INFORMATYCZNE = "usl_obce_informatyczne"
    USL_OBCE_INNE = "usl_obce_inne"
    USL_OBCE_KSIEGOWE = "usl_obce_ksiegowe"
    USL_OBCE_LEASINGI = "usl_obce_leasingi"
    USL_OBCE_NAJMY_CZYNSZE = "usl_obce_najmy_czynsze"
    USL_OBCE_PRAWNE = "usl_obce_prawne"
    USL_OBCE_TELEKOMUNIKACYJNE = "usl_obce_telekomunikacyjne"
    USL_OBCE_TRANSPORTOWE = "usl_obce_transportowe"
    WARTOSC_SPRZEDANYCH_TOWAROW = "wartosc_sprzedanych_towarow"
    ZALICZKI_NA_DOSTAWY = "zaliczki_na_dostawy"
    ZAPASY_MATERIALY = "zapasy_materialy"
    ZAPASY_TOWARY = "zapasy_towary"
    ZAPASY_TOWARY_W_DRODZE = "zapasy_towary_w_drodze"
    ZDARZENIA_LOSOWE = "zdarzenia_losowe"



class OkresDeklaracji(str, Enum):
    MIES = "mies"
    KWAR = "kwart"

class VatSaleCategoryTargetType(str, Enum):
    DOSTAWA_KRAJOWA = "dostawa_krajowa"
    # DELIVERY_VAT_OUTSIDE = "DELIVERY_VAT_OUTSIDE"
    # DELIVERY_EU_SERVICES_ART100 = "DELIVERY_EU_SERVICES_ART100"
    #
    # DELIVERY_DOMESTIC_0 = "DELIVERY_DOMESTIC_0"
    # DELIVERY_DOMESTIC_0_ART129 = "DELIVERY_DOMESTIC_0_ART129"
    #
    # DELIVERY_DOMESTIC_5 = "DELIVERY_DOMESTIC_5"
    # DELIVERY_DOMESTIC_8 = "DELIVERY_DOMESTIC_8"
    # DELIVERY_DOMESTIC_STD = "DELIVERY_DOMESTIC_STD "

    VAT_OSS = "VAT_OSS"

    # ICS_WDT = "ICS_WDT"
    # EXPORT_GOODS = "EXPORT_GOODS"
    #
    # ICA_WNT = "WNT"
    # ICA_WNT_GOODS = "WNT_MAG"
    # ICA_WNT_FIXED_ASSET = "WNT_SR_TRW"
    # ICA_WNT_FIXED_ASSET_TRANSPORT = "WNT_SR_TRW_TRANS"
    #
    # ACQUISITION_DOMESTIC = "NABYCIE_KRAJOWE"
    # ACQUISITION_DOMESTIC_FIXED_ASSET = "NABYCIE_KRAJOWE_SR_TRW"
    #
    # IMPORT_GOODS_ART33A = "IMPORT_TOWAR_ART33A"
    # IMPORT_GOODS_ART33A_WARE = "IMPORT_TOWAR_ART33A_MAG"
    # IMPORT_SERVICES_NON_28B = "IMPORT_USL_NIE_28B"
    # IMPORT_SERVICES_28B = "IMPORT_USL_28B"
    #
    # REVERSE_CHARGE_DOMESTIC_GOODS = "ODWROTNE_OBCIAZENIE_KRAJ_TOWAR"
    # REVERSE_CHARGE_DOMESTIC_SERVICES = "ODWROTNE_OBCIAZENIE_KRAJ_USLUGI"
    #
    # VAT_ADJUSTMENT_ART14_INVENTORY = "VAT_ADJUSTMENT_ART14_INVENTORY" # spis z natury, remament
    # VAT_ADJUSTMENT_CASH_REGISTER_REFUND = "VAT_ADJUSTMENT_CASH_REGISTER_REFUND" # odpis za zakup kasy fiskalnej

class JPKAmountType(str, Enum):
    NET = "NET"
    VAT_DUE = "VAT_DUE"
    VAT_INPUT = "VAT_INPUT"
    VAT_ADJUSTMENT = "VAT_ADJUSTMENT"

class AssetPurchaseCategory(str, Enum):
    FIXED_ASSET = "FIXED_ASSET"
    OTHER = "OTHER"

class AccountingTargetJPK(str, Enum):
    K_10 = "K_10"
    K_11 = "K_11"
    K_12 = "K_12"
    K_13 = "K_13"
    K_14 = "K_14"
    K_15 = "K_15"
    K_16 = "K_16"
    K_17 = "K_17"
    K_18 = "K_18"
    K_19 = "K_19"
    K_20 = "K_20"
    K_21 = "K_21"
    K_22 = "K_22"
    K_23 = "K_23"
    K_24 = "K_24"
    K_25 = "K_25"
    K_26 = "K_26"
    K_27 = "K_27"
    K_28 = "K_28"
    K_29 = "K_29"
    K_30 = "K_30"
    K_31 = "K_31"
    K_32 = "K_32"
    K_33 = "K_33"
    K_34 = "K_34"
    K_35 = "K_35"
    K_36 = "K_36"

class AccountingRuleAction(str, Enum):
    CREATE_VAT_POSTINGS = "CREATE_VAT_POSTINGS"  # klasyczne księgowanie VAT
    CREATE_ASSET_ENTRY = "CREATE_ASSET_ENTRY"    # księgowanie środków trwałych
    CREATE_PURCHASE_ENTRY = "CREATE_PURCHASE_ENTRY"  # księgowanie zakupu towaru/usługi
    CREATE_REVERSE_CHARGE_ENTRY = "CREATE_REVERSE_CHARGE_ENTRY"  # mechanizm odwrotnego obciążenia
    CREATE_VAT_ADJUSTMENT = "CREATE_VAT_ADJUSTMENT"  # korekty VAT (np. art.14, kasowe)
    CREATE_IMPORT_ENTRY = "CREATE_IMPORT_ENTRY"  # księgowanie importu towarów/usług

class AccountingRuleTrigger(str, Enum):
    # Zakupy krajowe
    INVOICE_PURCHASE_DOMESTIC = "INVOICE_PURCHASE_DOMESTIC"
    INVOICE_PURCHASE_DOMESTIC_FIXED_ASSET = "INVOICE_PURCHASE_DOMESTIC_FIXED_ASSET"

    # Import towarów / usług
    INVOICE_PURCHASE_IMPORT_GOODS_ART33A = "INVOICE_PURCHASE_IMPORT_GOODS_ART33A"
    INVOICE_PURCHASE_IMPORT_SERVICES_NON_28B = "INVOICE_PURCHASE_IMPORT_SERVICES_NON_28B"
    INVOICE_PURCHASE_IMPORT_SERVICES_ART28B = "INVOICE_PURCHASE_IMPORT_SERVICES_ART28B"

    # Wewnątrzwspólnotowe nabycie
    INVOICE_PURCHASE_EU_GOODS = "INVOICE_PURCHASE_EU_GOODS"

    # Reverse charge krajowy
    INVOICE_PURCHASE_RC_DOMESTIC_GOODS = "INVOICE_PURCHASE_RC_DOMESTIC_GOODS"
    INVOICE_PURCHASE_RC_DOMESTIC_SERVICES = "INVOICE_PURCHASE_RC_DOMESTIC_SERVICES"

    # Korekty VAT
    VAT_ADJUSTMENT_ART14_INVENTORY = "VAT_ADJUSTMENT_ART14_INVENTORY"
    VAT_ADJUSTMENT_CASH_REGISTER_REFUND = "VAT_ADJUSTMENT_CASH_REGISTER_REFUND"

class InvoiceType(str, Enum):
    SALES = "SALES"
    PURCHASE = "PURCHASE"

class SalesInvoiceType(str, Enum):
    SALES = "SALES"
    PURCHASE = "PURCHASE"

class SourceInvoiceSource(str, Enum):
    MANUAL = "MANUAL"
    KSEF = "KSEF"
    IMPORT = "IMPORT"

class SourceInvoiceStatus(str, Enum):
    DRAFT = "draft",
    VERIFIED = "verified",
    APPROVED = "approved",
    BOOKED = "booked"

class VatDirection(str, Enum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"
    BOTH = "BOTH"
    NONE = "NONE"

class TaskDateFirst(str, Enum):
    DATE_POSTING = "date_posting"
    DATE_VAT = "date_vat"
    DATE_CIT = "date_cit"
    DATE_SUPPLY = "date_supply"
    DATE_SETTLEMENT = "date_settlement"
    DATE_ISSUE = "date_issue"
    DATE_RECEIVED = "date_received"
    DATE_GOODS_RECEIPT = "date_goods_receipt"

class TaskStatus(str, Enum):
    PENDING = "PENDING"        # utworzony, nie uruchomiony
    RUNNING = "RUNNING"        # w trakcie
    SUCCESS = "SUCCESS"        # wykonany poprawnie
    FAILED = "FAILED"          # błąd

class Year(str, Enum):
    Y_2025 = "2025"
    Y_2026 = "2026"
    Y_2027 = "2027"

class Month(str, Enum):
    M_1 = "1"
    M_2 = "2"
    M_3 = "3"
    M_4 = "4"
    M_5 = "5"
    M_6 = "6"
    M_7 = "7"
    M_8 = "8"
    M_9 = "9"
    M_10 = "10"
    M_11 = "11"
    M_12 = "12"

class Quarter(str, Enum):
    Q_1 = "1"
    Q_2 = "2"
    Q_3 = "3"
    Q_4 = "4"

class SaleAccounts(str, Enum):
    TOWARY = "Income:A:SprzedazTowarow"
    USLUGI_PRODUKTY = "Income:A:SprzedazUslugProduktow"
    ODSETKI = "Income:G:Odsetki"


class TowarUsluga(str, Enum):
    T = "T"
    U = "U"
