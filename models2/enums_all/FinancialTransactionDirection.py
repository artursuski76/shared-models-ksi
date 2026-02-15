from enum import Enum


class FinancialTransactionDirection(str, Enum):
    IN = "IN"
    OUT = "OUT"