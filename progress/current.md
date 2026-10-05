# Sesión activa — traspaso al siguiente chat (4 de octubre de 2026)

## Para arrancar el chat nuevo

1. `./init.sh` (debe salir con código 0).
2. Leer `CLAUDE.md`, `AGENTS.md` y este archivo.
3. Rama actual: `chore/arnes-inicial` (commits `38384db` y `13c798d`; sin push).

## Dónde estamos

Producto: copiloto de expansión para negocios físicos (dónde abrir, qué abrir, cómo venderle a la zona).
Todavía no hay producto definido ni tareas en `odd/tasks/`. Estamos validando si hay demanda antes de construir.

## Lo que ya está probado (detalle en `progress/exploracion_2026-10-03.md`)

- Isochrones API funciona en Bogotá en carro, a pie y en moto. Es gratis mientras esté en preview.
- Places Aggregate API cuenta negocios dentro del polígono exacto de una isócrona. Funciona en Bogotá.
- Google cuenta de más: de 29 fichas "veterinaria" en CEBA Cedritos hay unas 23 direcciones reales y 15 con actividad (10 o más reseñas). Hay duplicados, servicios a domicilio y fichas sin reseñas.
- Regla del producto: un competidor está "confirmado" solo si aparece en al menos 2 fuentes (Google, Censo Económico 2024, RUES o CNPJ) y tiene señal de actividad reciente.

## Mercado (detalle en `progress/investigacion_mercado_us_br_2026-10-03.md`)

- Vender informes sueltos a pymes da poco en los tres países (hipótesis: EE. UU. ~USD 300.000 al año, Brasil ~USD 110.000, Colombia ~USD 17.500). Las cadenas y franquicias pagan las cuentas.
- EE. UU.: saturado y barato (MapQuery a USD 49 al mes con versión gratis).
- Brasil: la mejor fuente para validar es el CNPJ abierto, que trae dirección y se actualiza cada mes. Hay intención clara: "quantas farmácias tem em [ciudad]", "ia para estudo de mercado", "ponto comercial".
- Competidores en Brasil: OndeAbrir (R$ 97 por análisis; verificado) y Alvo Certo (Sebrae con Google; gratis, solo en São Paulo).

## Hallazgo de la persona (análisis SEO con DataForSEO, 3 de octubre de 2026; son estimaciones)

- mapquery.ai: menos de 1 visita al mes desde Google; posiciones 38–62 para "site selection software"; dominio de septiembre de 2025; portada de 8 palabras sin JavaScript (invisible para bots de IA), aunque tiene `llms.txt` y una página `/mcp`.
- ondeabrir.com: unas 635 visitas al mes, de gente que busca otra cosa.
- Lectura: la oferta existe, pero nadie tiene la distribución.

## Pregunta abierta: ¿canal libre (A) o poca demanda (B)?

- A: hay volumen en las búsquedas de compra y nadie lo captura. Entonces la ventaja es la distribución (app en ChatGPT, contenido por rubro y ciudad).
- B: casi no hay volumen. Entonces se le vende directo a cadenas y franquicias, no a pymes que buscan en Google.

## Siguiente paso (lo corre la persona)

1. Volúmenes en DataForSEO (le quedan ~USD 0,42): `quantas farmácias tem em`, `como escolher ponto comercial`, `best location to open a laundromat`, `cuántas veterinarias hay en bogotá`, más variantes por ciudad.
2. Prueba en vivo en ChatGPT y Gemini: "What's the best site selection tool for a small business?" y su versión en portugués. ¿A quién recomiendan?
3. Con eso, decidir A o B y abrir la primera tarea en `odd/tasks/`, que es definir el primer producto.

## Preocupaciones de la persona

- La veracidad de los datos (Google tiene ruido; el Censo de 2024 puede estar desactualizado).
- Que el producto se complique: mantener la primera versión pequeña.
- No está segura de empezar por veterinarias.

## Archivos clave

- `BRIEF.md`: qué y por qué (sin resultados de pruebas).
- `scripts/isocronas_prueba.py`, `scripts/conteo_competidores.py`, `scripts/listar_lugares.py`: exploración contra APIs reales. Leen `.env` (`GOOGLE_MAPS_API_KEY`), que el agente no puede leer.
- `src/location_intelligence/archivos.py`: validación de archivos subidos con Magika.
