from enum import Enum


class GrupySrodkowTrwalych(str, Enum):
    INNE_WART_NIEMAT_I_PRAW = "inne_artosci_niematerialne_i_prawne"
    GRUNTY = "grunty"
    BUDYNKI_LOKALE = "budynki_lokale_i_inne_obiekty"
    URZADZENIA_TECHNICZNE = "urzadzenia_techniczne"
    SRODKI_TRANSPORTU = "srodki_transportu"
    INNE_SRODKI_TRWALE = "inne_srodki_trwale"

class MetodyAmortyzacji(str, Enum):
    LINIOWA = "liniowa"
    ZMIANA_STAWKI = "wartosc_rezydualna"
    ODPIS_JEDNORAZOWY = "odpis_jednorazowy"
    

