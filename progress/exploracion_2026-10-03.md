# Exploración técnica — 3 de octubre de 2026

Pruebas contra APIs reales de Google desde Bogotá. Corridas un sábado en la noche.

## Isochrones API

- Resuelto el 403 (`API_KEY_SERVICE_BLOCKED`) agregando Isochrones a la key.
- `DRIVE`, `WALK` y `TWO_WHEELER` devuelven HTTP 200 con polígono GeoJSON desde
  Chapinero (4.6486, -74.0628).
- Una petición mínima (`location` + `WALK` + `600s`, sin `travelDirection` ni
  `routingPreference`) dio 400 `INVALID_ARGUMENT`. La causa exacta no está aislada:
  `scripts/isocronas_prueba.py` funciona sin `routingPreference` ni `enableSmoothing`.
- Precio: USD 0 mientras esté en preview. Después: gratis hasta 10.000 al mes y
  luego desde USD 3,00 por 1.000.
  Fuente: https://developers.google.com/maps/documentation/isochrones/usage-and-billing
- `TRAFFIC_AWARE` usa el tráfico del momento de la petición; no hay campo de hora de salida.
- Límites: `WALK` y `BICYCLE` hasta 120 min; `DRIVE` y `TWO_WHEELER` hasta 60 min.

## Prueba con Animal Center y CEBA (`scripts/isocronas_prueba.py`)

| Modo | Área por sede | Solapamiento entre sedes |
|---|---|---|
| Carro 15 min, sin tráfico | 134–247 km² | 64–100% (inútil para decidir) |
| Carro 15 min, con tráfico | 15–54 km² | Animal Center Cedritos ↔ Santa Bárbara 94%; Galerías aislada |
| A pie 10 min | 0,6–0,8 km² | 0% |

## Conteo de competidores

- Places Text Search (tope de 20 por consulta) encontró 0–6 veterinarias dentro de las
  áreas a pie: muy subestimado.
- Places Aggregate API (`scripts/conteo_competidores.py`) con la isócrona como polígono
  funciona en Bogotá. Veterinarias operativas a pie 10 min: CEBA Cedritos 29,
  Animal Center Cedritos 15, Animal Center Galerías 14, CEBA Santa Bárbara 7,
  Animal Center Rosales 5, Animal Center Santa Bárbara 4.
- Revisión de las 29 fichas de CEBA Cedritos (`scripts/listar_lugares.py`):
  - CEBA misma no aparece (no está clasificada como `veterinary_care`).
  - 6 fichas duplicadas en la misma dirección; 23 direcciones distintas.
  - No son locales físicos que compitan: a domicilio (1), unidad móvil (1), criadero o tienda (1).
  - 8 fichas con 0 reseñas.
  - 15 con 10 reseñas o más.
- Conclusión: el conteo de Google está inflado. El producto necesita una capa de
  "competencia efectiva" que cruce fuentes.

## Grounding Lite

- Herramientas: buscar lugares, clima y rutas. Endpoint MCP `https://mapstools.googleapis.com/mcp`.
- No se puede guardar nada; la atribución es obligatoria.
- La documentación actual dice que se cobra por petición. La página de precios dio 404; no verificado.

## Places Insights (BigQuery)

- No activado: requiere acceso por ventas. `PLACES_COUNT_CHANGE` devuelve los negocios
  nuevos y los cerrados entre dos meses (base para el producto Vigilancia).
  La cobertura en Colombia no está publicada.
