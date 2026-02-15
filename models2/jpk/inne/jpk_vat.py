# app/models/jpk/jpk_vat.py

from pydantic import BaseModel, Field




class JpkBase(BaseModel):

    naglowek: Naglowek
    podmiot1: Podmiot1
    deklaracja: Deklaracja
    ewidencja: Ewidencja
