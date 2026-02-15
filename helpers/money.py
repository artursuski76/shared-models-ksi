from typing import Annotated  # Dodano Annotated

from pydantic import BeforeValidator, PlainSerializer, \
    WithJsonSchema

from models2.helpers.to_grosze import to_grosze

Money = Annotated[
    int,
    BeforeValidator(to_grosze),
    PlainSerializer(lambda v: float(v / 100), return_type=float, when_used='json'),
    WithJsonSchema({"type": "number", "format": "decimal"})
]