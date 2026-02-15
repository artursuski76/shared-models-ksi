from enum import Enum


class Expenses(str, Enum):
    PODATKI_OPLATY = "Podatki_Oplaty"
    AKCYZA = "Akcyza"
    POZOSTALE_RODZAJOWE = "Pozostale_Rodzajowe"
    USLUGI_OBCE = "Uslugi_Obce"
    WYNAGRODZENIA = "Wynagrodzenia"
    PALIWO_MATERIALY_ENERGIA = "Paliwo_Materialy_Energia"
    INNE_OPERACYJNE = "Inne_Operacyjne"
    INNE_FINANSOWE = "Inne_Finansowe"
    ODSETKI = "Odsetki"



