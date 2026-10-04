"""Exact veterinary counts inside each saved isochrone, using Places Aggregate API.

Reads the polygons that isocronas_prueba.py saved in data/isocronas/<mode>/ and
asks Places Aggregate API (computeInsights, INSIGHT_COUNT) how many operational
places of type veterinary_care fall inside each one. This replaces the Text
Search approach, which is capped at 20 results per query.

The count includes the chain's own location. A MultiPolygon is counted part by
part and summed; holes are ignored, so the count can be slightly high.

Reads GOOGLE_MAPS_API_KEY from .env. Standard library only.

Usage: python3 scripts/conteo_competidores.py
"""
import json
import math
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "isocronas"
TIPO = "veterinary_care"
MAX_VERTICES = 7000
AREA_MINIMA_M2 = 1557


def key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("GOOGLE_MAPS_API_KEY"):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("GOOGLE_MAPS_API_KEY no está en .env")


KEY = key()


def request(url, body=None, fields=None):
    headers = {"Content-Type": "application/json", "X-Goog-Api-Key": KEY}
    if fields:
        headers["X-Goog-FieldMask"] = fields
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data, headers, method="POST" if body is not None else "GET")
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} en {url}:\n{e.read().decode()[:500]}")


def nombre(place_id):
    r = request(f"https://places.googleapis.com/v1/places/{place_id}", fields="displayName")
    return r.get("displayName", {}).get("text", place_id)


def poligonos(geo):
    g = geo.get("geometry", geo)
    if g["type"] == "Polygon":
        return [g["coordinates"]]
    if g["type"] == "MultiPolygon":
        return g["coordinates"]
    raise ValueError(f"geometría no soportada: {g['type']}")


def area_firmada(ring):
    """Shoelace area in degrees²; positive means counterclockwise."""
    return sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(ring, ring[1:])) / 2


def area_m2(ring):
    lat = sum(p[1] for p in ring) / len(ring)
    return abs(area_firmada(ring)) * 111320 ** 2 * math.cos(math.radians(lat))


def preparar(ring):
    ring = [tuple(p[:2]) for p in ring]
    if ring[0] != ring[-1]:
        ring.append(ring[0])
    if area_firmada(ring) < 0:
        ring.reverse()
    if len(ring) > MAX_VERTICES:
        paso = len(ring) // (MAX_VERTICES - 1) + 1
        ring = ring[:-1:paso] + [ring[0]]
    return ring


def contar(ring):
    body = {
        "insights": ["INSIGHT_COUNT"],
        "filter": {
            "locationFilter": {"customArea": {"polygon": {"coordinates": [
                {"latitude": y, "longitude": x} for x, y in ring]}}},
            "typeFilter": {"includedTypes": [TIPO]},
            "operatingStatus": ["OPERATING_STATUS_OPERATIONAL"],
        },
    }
    r = request("https://areainsights.googleapis.com/v1:computeInsights", body)
    return int(r.get("count", 0))


def main():
    carpetas = sorted(p for p in DATA.iterdir() if p.is_dir()) if DATA.exists() else []
    if not carpetas:
        raise SystemExit("No hay isócronas guardadas. Corre primero scripts/isocronas_prueba.py")
    nombres = {}
    for carpeta in carpetas:
        print(f"\n--- {carpeta.name} ({TIPO}, operativas, incluye la propia sede) ---")
        for archivo in sorted(carpeta.glob("*.geojson")):
            place_id = archivo.stem
            if place_id not in nombres:
                nombres[place_id] = nombre(place_id)
            total = 0
            for poly in poligonos(json.loads(archivo.read_text())):
                ring = preparar(poly[0])
                if area_m2(ring) < AREA_MINIMA_M2:
                    continue
                total += contar(ring)
            print(f"  {nombres[place_id]}: {total}")


if __name__ == "__main__":
    main()
