from pydantic import Field, BaseModel


class TransactionFiles(BaseModel):
    status: str | None = Field(default=None, description="status", json_schema_extra={"exclude_from_form": True})
    filename: str | None = Field(default=None, description="filename")  # pojawi się w formularzu
    minio_key: str | None = Field(default=None, description="Plik - key")
    minio_bucket: str | None = Field(default=None, description="Plik - bucket", json_schema_extra={"exclude_from_form": True})
    minio_url: str | None = Field(default=None, description="Plik - url", json_schema_extra={"exclude_from_form": True})