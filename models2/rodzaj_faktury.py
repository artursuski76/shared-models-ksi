from enum import Enum


class RodzajFaktury(str ,Enum):
    VAT = "VAT"
    KOR = "KOR"
    ZAL = "ZAL"
    ROZ = "ROZ"
    UPR = "UPR"
    KOR_ZAL = "KOR_ZAL"
    KOR_ROZ = "KOR_ROZ"