
from decimal import Decimal, ROUND_HALF_UP
from typing import Any

from pymongo.errors import InvalidOperation


def to_grosze(v: Any) -> int:
    if v is None:
        return 0

    # ZMIANA: jeżeli frontend wysyła 100 jako JSON number (int),
    # to interpretujemy to jako 100 zł, czyli 10000 groszy.
    if isinstance(v, int):
        return v * 100

    try:
        clean_v = str(v).replace(",", ".").strip()
        d = Decimal(clean_v)
        return int((d * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    except (ValueError, TypeError, InvalidOperation):
        return 0