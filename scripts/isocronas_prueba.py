"""Isochrones API test for Animal Center and CEBA, compared across travel modes.

Copied from aura-lead-intelligence/scripts/isocronas_prueba.py. The original
used a 15-minute drive without traffic, which covered a third of Bogotá per
location and made overlap and competitor counts meaningless. This version runs
each chain in several modes so they can be compared side by side.

Prints numbers only: area per location, overlap between locations of the
same chain, and competitors inside each area. Polygons are saved to
data/isocronas/<mode>/ for a map later. Reads GOOGLE_MAPS_API_KEY from .env.
Standard library only.

Note: TRAFFIC_AWARE uses traffic at the moment of the request (the API has no
departure time field), so results change with the hour and day it runs.

Usage: python3 scripts/isocronas_prueba.py
"""
import json
import math
import pathlib
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "isocronas"

# (label, travelMode, minutes, routingPreference or None)
MODOS = [
    ("a_pie_10", "WALK", 10, None),
    ("carro_15_trafico", "DRIVE", 15, "TRAFFIC_AWARE"),
]

SEDES = {
    "Animal Center": ["Animal Center Rosales", "Animal Center Cedritos",
                      "Animal Center Santa Bárbara", "Animal Center Galerias"],
    "CEBA": ["CEBA Cedritos veterinaria", "CEBA Santa Bárbara veterinaria"],
}


def key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("GOOGLE_MAPS_API_KEY"):
            return line.split("=", 1)[1].strip().strip('"')
    raise SystemExit("GOOGLE_MAPS_API_KEY no está en .env")


KEY = key()


def post(url, body, fields=None):
    headers = {"Content-Type": "application/json", "X-Goog-Api-Key": KEY}
    if fields:
        headers["X-Goog-FieldMask"] = fields
    req = urllib.request.Request(url, json.dumps(body).encode(), headers)
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP {e.code} en {url}:\n{e.read().decode()[:500]}")


def buscar(texto, limite=1, rect=None):
    body = {"textQuery": texto, "languageCode": "es", "maxResultCount": limite}
    if rect:
        body["locationRestriction"] = {"rectangle": rect}
    else:
        body["locationBias"] = {"circle": {"center": {"latitude": 4.68, "longitude": -74.05},
                                           "radius": 8000}}
    r = post("https://places.googleapis.com/v1/places:searchText", body,
             "places.id,places.displayName,places.location,places.rating,places.userRatingCount")
    return r.get("places", [])


def isocrona(place_id, modo, minutos, preferencia):
    body = {
        "place": f"places/{place_id}",
        "travelDuration": f"{minutos * 60}s",
        "travelMode": modo,
        "travelDirection": "TO",
    }
    if preferencia:
        body["routingPreference"] = preferencia
    r = post("https://isochrones.googleapis.com/v1/isochrones:generate", body)
    return r["isochrone"]["geoJson"]


def anillos(geo):
    g = geo.get("geometry", geo)
    if g["type"] == "Polygon":
        return [g["coordinates"]]
    if g["type"] == "MultiPolygon":
        return g["coordinates"]
    if g["type"] in ("Feature",):
        return anillos(g["geometry"])
    if g["type"] == "FeatureCollection":
        return [p for f in g["features"] for p in anillos(f)]
    raise ValueError(f"geometría no soportada: {g['type']}")


def dentro_anillo(x, y, ring):
    ins = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            ins = not ins
    return ins


def dentro(lng, lat, polys):
    # polygon = [outer ring, holes...]
    return any(dentro_anillo(lng, lat, [tuple(p[:2]) for p in poly[0]])
               and not any(dentro_anillo(lng, lat, [tuple(p[:2]) for p in h]) for h in poly[1:])
               for poly in polys)


def bbox(polys):
    xs = [p[0] for poly in polys for p in poly[0]]
    ys = [p[1] for poly in polys for p in poly[0]]
    return min(xs), min(ys), max(xs), max(ys)


def muestreo(polys_list, paso=0.002):
    """Grid points (~220 m) covering every polygon; returns per-point membership."""
    x0, y0, x1, y1 = bbox([p for ps in polys_list for p in ps])
    celda_km2 = (paso * 111.32) * (paso * 111.32 * math.cos(math.radians((y0 + y1) / 2)))
    puntos = []
    y = y0
    while y <= y1:
        x = x0
        while x <= x1:
            puntos.append(tuple(dentro(x, y, ps) for ps in polys_list))
            x += paso
        y += paso
    return puntos, celda_km2


def analizar(marca, lugares, etiqueta, modo, minutos, preferencia):
    print(f"\n--- {etiqueta} ({modo}, {minutos} min, {preferencia or 'sin tráfico'}) ---")
    carpeta = OUT / etiqueta
    carpeta.mkdir(parents=True, exist_ok=True)
    sedes = []
    for p in lugares:
        geo = isocrona(p["id"], modo, minutos, preferencia)
        (carpeta / f"{p['id']}.geojson").write_text(json.dumps(geo))
        sedes.append((p["displayName"]["text"], p, anillos(geo)))

    puntos, celda = muestreo([s[2] for s in sedes])
    for i, (nombre, p, _) in enumerate(sedes):
        area = sum(pt[i] for pt in puntos) * celda
        print(f"  {nombre}: {area:.1f} km² "
              f"({p.get('rating')}★, {p.get('userRatingCount')} reseñas)")

    print("  Solapamiento (% del área de la primera que comparte con la segunda):")
    for i in range(len(sedes)):
        for j in range(i + 1, len(sedes)):
            a = sum(pt[i] for pt in puntos)
            ab = sum(pt[i] and pt[j] for pt in puntos)
            pct = 100 * ab / a if a else 0
            print(f"    {sedes[i][0]} ↔ {sedes[j][0]}: {pct:.0f}%")
    union = sum(any(pt) for pt in puntos) * celda
    print(f"  Cobertura total de la cadena: {union:.1f} km²")

    x0, y0, x1, y1 = bbox([p for s in sedes for p in s[2]])
    rect = {"low": {"latitude": y0, "longitude": x0}, "high": {"latitude": y1, "longitude": x1}}
    competidores = {}
    for q in ("clínica veterinaria", "veterinaria", "hospital veterinario"):
        for c in buscar(q, limite=20, rect=rect):
            if marca.split()[0].lower() not in c["displayName"]["text"].lower():
                competidores[c["id"]] = c
    print(f"  Competidores encontrados en la zona (máx. 60, límite de Places): {len(competidores)}")
    for nombre, _, polys in sedes:
        n = sum(dentro(c["location"]["longitude"], c["location"]["latitude"], polys)
                for c in competidores.values())
        print(f"    dentro del área de {nombre}: {n}")


def main():
    for marca, consultas in SEDES.items():
        print(f"\n=== {marca} ===")
        lugares = []
        for q in consultas:
            res = buscar(q + " Bogotá")
            if not res:
                print(f"  sin resultado: {q}")
                continue
            lugares.append(res[0])
        for etiqueta, modo, minutos, preferencia in MODOS:
            analizar(marca, lugares, etiqueta, modo, minutos, preferencia)


if __name__ == "__main__":
    main()
