"""List the places that Places Aggregate API counts inside one saved isochrone.

Use it to check what Google tags as veterinary_care before trusting a count.
Only prints to the terminal: Google Places content must not be stored.

Reads GOOGLE_MAPS_API_KEY from .env. Standard library only.

Usage: python3 scripts/listar_lugares.py <mode> "<location name fragment>"
Example: python3 scripts/listar_lugares.py a_pie_10 "CEBA - Cedritos"
"""
import json
import sys

from conteo_competidores import DATA, TIPO, area_m2, AREA_MINIMA_M2, nombre, poligonos, preparar, request


def ids_en(ring):
    body = {
        "insights": ["INSIGHT_PLACES"],
        "filter": {
            "locationFilter": {"customArea": {"polygon": {"coordinates": [
                {"latitude": y, "longitude": x} for x, y in ring]}}},
            "typeFilter": {"includedTypes": [TIPO]},
            "operatingStatus": ["OPERATING_STATUS_OPERATIONAL"],
        },
    }
    r = request("https://areainsights.googleapis.com/v1:computeInsights", body)
    return [p["place"].split("/", 1)[1] for p in r.get("placeInsights", [])]


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    modo, fragmento = sys.argv[1], sys.argv[2].lower()
    archivo = next((a for a in sorted((DATA / modo).glob("*.geojson"))
                    if fragmento in nombre(a.stem).lower()), None)
    if not archivo:
        raise SystemExit(f"No encontré una sede con '{sys.argv[2]}' en {DATA / modo}")

    ids = []
    for poly in poligonos(json.loads(archivo.read_text())):
        ring = preparar(poly[0])
        if area_m2(ring) >= AREA_MINIMA_M2:
            ids += ids_en(ring)

    campos = "displayName,primaryTypeDisplayName,types,formattedAddress,rating,userRatingCount"
    print(f"{nombre(archivo.stem)} — {modo}: {len(ids)} lugares\n")
    for i, pid in enumerate(ids, 1):
        p = request(f"https://places.googleapis.com/v1/places/{pid}?languageCode=es", fields=campos)
        otros = [t for t in p.get("types", []) if t not in (TIPO, "point_of_interest", "establishment")]
        print(f"{i:>2}. {p.get('displayName', {}).get('text', pid)}")
        print(f"    tipo principal: {p.get('primaryTypeDisplayName', {}).get('text', 'no publicado')}"
              f" | otros: {', '.join(otros) or '—'}")
        print(f"    {p.get('formattedAddress', '')} | {p.get('rating', '—')}★ "
              f"({p.get('userRatingCount', 0)} reseñas)")


if __name__ == "__main__":
    main()
