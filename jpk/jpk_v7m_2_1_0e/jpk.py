from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring

from pydantic import BaseModel, Field

from app.models2.jpk.jpk_v7m_2_1_0e.deklaracja import Deklaracja
from app.models2.jpk.jpk_v7m_2_1_0e.naglowek import Naglowek
from app.models2.jpk.jpk_v7m_2_1_0e.podmiot1 import Podmiot1


class JPK(BaseModel):
    """Główny model JPK dla deklaracji VAT (JPK_V7M)."""

    # Atrybuty namespace XML
    xsd: str = Field("http://www.w3.org/2001/XMLSchema", alias="@xmlns:xsd")
    xsi: str = Field("http://www.w3.org/2001/XMLSchema-instance", alias="@xmlns:xsi")
    xmlns: str = Field("http://crd.gov.pl/wzor/2021/12/27/11148/", alias="@xmlns")

    Naglowek: Naglowek

    # Dodany Podmiot1
    Podmiot1: Podmiot1

    # "Deklaracja" w schemie jest opcjonalna (minOccurs="0"), więc w modelu też pozwalamy na None
    Deklaracja: Deklaracja

    # "Ewidencja" w schemie jest opcjonalna (minOccurs="0"), więc w modelu też pozwalamy na None
    # W tym repo nie ma klasy "Ewidencja" (są jedynie wiersze i sumy kontrolne),
    # dlatego tymczasowo używamy typu ogólnego (dict), aby umożliwić walidację/serializację.
    Ewidencja: dict


def _text_or_zero(val) -> str:
    if val is None:
        return "0"
    if isinstance(val, (int, float)):
        # Normalize -0.0 to 0
        if val == 0:
            return "0"
        return ("%s" % val)
    return str(val)


def _append_kv(parent: Element, tag: str, value) -> None:
    el = SubElement(parent, tag)
    el.text = _text_or_zero(value)


def _serialize_naglowek(parent: Element, naglowek: Naglowek) -> None:
    el_n = SubElement(parent, "Naglowek")

    # KodFormularza z atrybutami + wartością tekstową
    kf = naglowek.KodFormularza
    kf_el = SubElement(el_n, "KodFormularza")
    # ustaw atrybuty bezpośrednio z pól modelu
    if getattr(kf, "kodSystemowy", None) is not None:
        kf_el.set("kodSystemowy", str(kf.kodSystemowy))
    if getattr(kf, "wersjaSchemy", None) is not None:
        kf_el.set("wersjaSchemy", str(kf.wersjaSchemy))
    # wartość tekstowa elementu
    kf_el.text = "JPK_VAT"

    SubElement(el_n, "WariantFormularza").text = str(naglowek.WariantFormularza)

    dt = naglowek.DataWytworzeniaJPK
    if isinstance(dt, datetime):
        dt_txt = dt.astimezone().replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        dt_txt = str(dt)
    SubElement(el_n, "DataWytworzeniaJPK").text = dt_txt

    SubElement(el_n, "NazwaSystemu").text = str(naglowek.NazwaSystemu)

    # CelZlozenia z atrybutem poz="P_7"
    cel_el = SubElement(el_n, "CelZlozenia")
    cel_el.set("poz", "P_7")
    cel_el.text = str(naglowek.CelZlozenia)

    SubElement(el_n, "KodUrzedu").text = str(naglowek.KodUrzedu)
    SubElement(el_n, "Rok").text = str(naglowek.Rok)
    SubElement(el_n, "Miesiac").text = str(naglowek.Miesiac)


def _serialize_podmiot1(parent: Element, podmiot1: Podmiot1) -> None:
    el_p = SubElement(parent, "Podmiot1")
    el_p.set("rola", "Podatnik")

    on = podmiot1.OsobaNiefizyczna
    on_el = SubElement(el_p, "OsobaNiefizyczna")
    _append_kv(on_el, "NIP", on.NIP)
    _append_kv(on_el, "PelnaNazwa", on.PelnaNazwa)
    _append_kv(on_el, "Email", on.Email)
    _append_kv(on_el, "Telefon", on.Telefon)


def _serialize_deklaracja(parent: Element, deklaracja: Deklaracja) -> None:
    el_d = SubElement(parent, "Deklaracja")

    if deklaracja.Naglowek is not None:
        d_n = SubElement(el_d, "Naglowek")
        kfd = deklaracja.Naglowek.KodFormularzaDekl
        kfd_el = SubElement(d_n, "KodFormularzaDekl")
        kfd_data = kfd.model_dump(by_alias=True)
        # atrybuty
        for attr in ("@kodSystemowy", "@kodPodatku", "@rodzajZobowiazania", "@wersjaSchemy"):
            if attr in kfd_data:
                k, v = attr.replace("@", ""), kfd_data[attr]
                kfd_el.set(k, v)
        # tekst
        kfd_el.text = str(kfd_data.get("#value", "VAT-7"))
        SubElement(d_n, "WariantFormularzaDekl").text = "22"

    ps = deklaracja.PozycjeSzczegolowe
    ps_el = SubElement(el_d, "PozycjeSzczegolowe")
    ps_data = ps.model_dump(by_alias=True)
    for key, val in ps_data.items():
        _append_kv(ps_el, key, val)

    SubElement(el_d, "Pouczenia").text = "1"


def _serialize_ewidencja(parent: Element, ewidencja: dict) -> None:
    el_e = SubElement(parent, "Ewidencja")

    # SprzedazWiersz - lista słowników
    for w in ewidencja.get("SprzedazWiersz", []) :
        w_el = SubElement(el_e, "SprzedazWiersz")
        for k, v in w.items():
            # Specjalna reguła: jeśli NrKontrahenta == 'brak', to NIE generujemy KodKrajuNadaniaTIN w ogóle
            if k == "KodKrajuNadaniaTIN":
                nr = w.get("NrKontrahenta")
                if (isinstance(nr, str) and nr.strip().lower() == "brak"):
                    continue  # pomiń ten tag całkowicie
                # Dodatkowo nie generuj, jeśli wartość jest pusta/"0"
                if v in (None, "", "0"):
                    continue
            _append_kv(w_el, k, v)

    # SprzedazCtrl
    sctrl = ewidencja.get("SprzedazCtrl")
    if sctrl:
        sc_el = SubElement(el_e, "SprzedazCtrl")
        for k, v in sctrl.items():
            _append_kv(sc_el, k, v)

    # ZakupWiersz - lista słowników
    for w in ewidencja.get("ZakupWiersz", []) :
        w_el = SubElement(el_e, "ZakupWiersz")
        for k, v in w.items():
            _append_kv(w_el, k, v)

    # ZakupCtrl
    zctrl = ewidencja.get("ZakupCtrl")
    if zctrl:
        zc_el = SubElement(el_e, "ZakupCtrl")
        for k, v in zctrl.items():
            _append_kv(zc_el, k, v)


def to_xml(self: JPK, encoding: str = "utf-8", skip_empty: bool = True, pretty_print: bool = True) -> bytes:
    # Root element with namespaces
    root = Element("JPK")
    root.set("xmlns:xsd", self.xsd)
    root.set("xmlns:xsi", self.xsi)
    root.set("xmlns", self.xmlns)

    _serialize_naglowek(root, self.Naglowek)
    _serialize_podmiot1(root, self.Podmiot1)
    if self.Deklaracja is not None:
        _serialize_deklaracja(root, self.Deklaracja)
    if self.Ewidencja is not None:
        _serialize_ewidencja(root, self.Ewidencja)

    raw = tostring(root, encoding=encoding)

    if not pretty_print:
        return raw

    # pretty print using minidom (avoids extra spaces)
    try:
        from xml.dom import minidom
        reparsed = minidom.parseString(raw)
        xml_str = reparsed.toprettyxml(indent="  ", encoding=encoding)
        if isinstance(xml_str, bytes):
            # minidom.toprettyxml with encoding returns bytes
            # we want to ensure it doesn't have multiple declarations or weird starts
            return xml_str.strip()
        return xml_str.strip()
    except Exception:
        return raw


# bind method to class without altering signature
JPK.to_xml = to_xml
