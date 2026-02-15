from pydantic import BaseModel, model_serializer
from typing import Any


class FlattenMixin(BaseModel):
    @model_serializer(mode='wrap')
    def serialize_flattened(self, handler) -> dict[str, Any]:
        # 1. Pobierz standardowy słownik (szanuje exclude=True)
        data = handler(self)

        # 2. Przejdź po wszystkich polach modelu
        for field_name, field_info in self.model_fields.items():
            # Sprawdzamy, czy pole ma nasz autorski znacznik "flatten"
            if field_info.json_schema_extra and field_info.json_schema_extra.get("flatten"):
                obj = getattr(self, field_name)
                if obj and isinstance(obj, BaseModel):
                    # Najpierw usuń pierwotne, zagnieżdżone pole (alias lub nazwa),
                    # aby nie nadpisać płasko zserializowanych kluczy (np. "task_name").
                    alias = field_info.alias or field_name
                    if alias in data:
                        del data[alias]
                    elif field_name in data:
                        del data[field_name]

                    # Pobieramy dane z zagnieżdżonego modelu (z jego aliasami)
                    extra_data = obj.model_dump(by_alias=True)
                    # Łączymy z głównym słownikiem
                    data.update(extra_data)

        return data