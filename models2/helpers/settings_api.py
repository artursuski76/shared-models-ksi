from typing import Literal, List

from pydantic import BaseModel, Field




class WooCommerceShop(BaseModel):
    name: str = Field(None, title="Nazwa")
    url: str = Field(None, title="URL")
    consumer_key: str = Field(None, title="Consumer Key")
    consumer_secret: str = Field(None, title="Consumer Secret")

class WooCommerce(BaseModel):
    api: Literal["woo_commerce"] = Field(
        "woo_commerce",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

    apis: List[WooCommerceShop] = Field(default_factory=list, description="Lista sklepów WooCommerce")

class KSeFToken(BaseModel):
    api: Literal["ksef_token"] = Field(
        "ksef_token",
        title="Rodzaj",
        json_schema_extra={"exclude_from_form": True}
    )

    token: str = Field(None, title="Token")