from enum import Enum


class SkutekPodatkowyKorekty(str, Enum):
    """Enum for different types of corrections in invoices."""

    W_DACIE_FA_PIERW = "W dacie faktury pierwotnej"
    W_DACIE_FA_KOR = "W dacie faktury korygującej"
    W_DACIE_INNEJ = "W innej dacie"