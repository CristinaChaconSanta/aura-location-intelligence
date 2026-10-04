# Producto de inteligencia de ubicación — Brief inicial

Resumen de la exploración hecha entre el 19 de septiembre y el 3 de octubre de 2026, dentro de aura-lead-intelligence. Es un producto nuevo y separado. Todavía no tiene nombre. Las cifras llevan su fuente. Lo que es hipótesis está marcado como tal.

## 1. Qué es, en una frase

Un copiloto de expansión para negocios físicos en LATAM: le dice a una persona o empresa dónde abrir, qué abrir y cómo venderle a la gente de una zona. Combina áreas de tiempo de viaje (isócronas), competencia real, datos públicos del territorio y una guía de cómo construir el negocio para quienes viven o pasan por ahí.

Origen: surgió al evaluar la Isochrones API de Google para Aura Lead Intelligence. Se vio que el valor era más grande que una ficha de lead: podía ser un producto propio.

## 2. El diferenciador

En inglés ya existe la versión "IA que te dice dónde abrir", a USD 50–100 por informe (WhereToOpen, MapQuery). En Colombia y LATAM lo que hay es consultoría con cotización y sin precio público, y nadie está dentro de ChatGPT.

Lo que no se puede copiar en seis meses:

- Datos locales que Google no tiene: estrato oficial por manzana, censo DANE, Censo Económico 2024, catastro, uso del suelo (POT) y RUES.
- Movilidad como se vive en LATAM: isócronas a pie y en moto (TWO_WHEELER), no solo en carro.
- Del mapa a la acción: después de elegir la zona, cómo conseguir clientes ahí (mensajes, pauta y leads). Esta es la capa de Aura.
- Evidencia citada: cada número dice de dónde sale. Nada inventado (el mismo principio de Aura).
- Segmentación geodemográfica propia (tipo Mosaic) para Colombia, que hoy no existe.
- En español, con precio publicado y dentro de ChatGPT y WhatsApp.

## 3. Qué hace el producto

### 3.1 Las cuatro preguntas que responde

| Modo | Pregunta del cliente | Ejemplo |
|---|---|---|
| Dónde abro | "Quiero abrir X, ¿dónde?" | "Una veterinaria en el norte de Bogotá" |
| Qué pongo aquí | "Tengo este local o esta zona, ¿qué negocio funciona?" | Búsqueda real en Google: "qué negocio poner en un local pequeño" |
| Vigilancia | "Avísame si cambia algo en mi zona" | "Abrió un competidor nuevo a 10 minutos" |
| Expansión | "Tengo varias sedes, ¿dónde sigo?" | Canibalización entre sedes y huecos frente a la competencia |

### 3.2 Tipología del negocio: el primer paso de toda asesoría

| Tipo | El cliente… | Ejemplos | Datos que mandan | Isócrona |
|---|---|---|---|---|
| De barrio | vive cerca | Tienda, panadería, veterinaria | Residentes: censo, estrato, gasto de los hogares | A pie, 10 min |
| De paso | pasa por ahí | Café, comidas rápidas, droguería | Flotantes: aforos, estaciones, oficinas, universidades | A pie, 5 min |
| De destino | va a propósito | Odontología especializada, gimnasio boutique | Mercado amplio, competencia, parqueadero | En carro, 20–30 min |

### 3.3 La guía de cómo construir el negocio en ese territorio

Según quién vive o pasa por la zona: formato del local, horarios, precio y ticket, canal (WhatsApp, domicilio, walk-in) y mensaje de pauta.

Regla: la relación entre estrato y comportamiento sale de datos medidos (Encuesta de Presupuestos de los Hogares, DANE), nunca de suposiciones. El estrato es solo el oficial y nunca se infiere.

### 3.4 Las tres operaciones de fondo

Con isócronas solo hay tres operaciones, y todo el producto se arma con ellas:

- **Unión:** la cobertura real de una cadena.
- **Intersección:** la canibalización entre sedes o la competencia directa.
- **Diferencia:** los huecos (donde el competidor llega y tú no).

Más un indicador de demanda (hogares, reseñas por mes) para que no sea solo geometría.

### 3.5 Segmentación geodemográfica (tipo Mosaic)

Agrupar las manzanas según cómo vive la gente, con nombre y retrato por grupo. El precedente abierto es el Output Area Classification (OAC) del Reino Unido (ONS + UCL).

Pasos:

1. Unidad: la manzana o sección censal del DANE (MGN).
2. Entre 40 y 60 variables: censo, estrato, negocios, uso del suelo y acceso.
3. Pasar a porcentajes, estandarizar y quitar redundancias (PCA).
4. Agrupar con k-means: 6 a 8 grupos y 20 a 30 tipos.
5. Darle nombre y retrato a cada grupo, con datos.
6. Validar con comportamiento real (ENPH y resultados de clientes).
7. Actualizar cuando cambien los datos.

Esfuerzo: unas 3 a 4 semanas para una versión mínima de Bogotá.

Límites: el censo es de 2018; las manzanas con muy pocos habitantes aparecen con datos ocultos; y no hay datos de consumo individual como los de Experian, que además no se deben usar.

## 4. Canales y modelo de negocio

### 4.1 App en ChatGPT + web propia

- ChatGPT es el canal para que te encuentren, no la caja registradora. Las apps se construyen con el Apps SDK, montado sobre MCP, y pueden mostrar un componente visual como un mapa.
- Restricción verificada (octubre de 2026): dentro de ChatGPT solo se puede cobrar por productos físicos, con pago en el sitio del vendedor. Los servicios digitales y las suscripciones no se pueden cobrar ahí. OpenAI dice que lo está evaluando, sin fecha.
- El modelo: la app es gratis en ChatGPT; el informe y la suscripción se venden en la web propia, con inicio de sesión.

### 4.2 Paquetes y precios (hipótesis por validar)

| Paquete | Qué incluye | LATAM | EE. UU. / Europa |
|---|---|---|---|
| Explora (ChatGPT) | Área de 15 min y conteo de competidores | Gratis | Gratis |
| Informe de zona | Mapa, competidores, huecos, estrato y uso del suelo, en PDF | USD 29–49 una vez | USD 79–99 |
| Vigilancia | Alertas mensuales de competencia | USD 29–49/mes | USD 49–99/mes |
| Corredor | 10 informes al mes con marca propia | USD 99/mes | — |
| Expansión | Varias sedes, canibalización y territorios | USD 199–499/mes | USD 299–799/mes |
| Enterprise | API, datos a la medida y consultoría de Aura | Desde USD 10.000/año | — |

### 4.3 LTV

Fórmula: LTV = ingreso mensual × margen ÷ churn mensual. Se supone un margen de 90%; los churn son hipótesis.

| Cliente | LTV aprox. |
|---|---|
| Pyme, informe único | USD 39 |
| Pyme con vigilancia (8% churn) | ~USD 430 |
| Corredor (5% churn) | ~USD 1.800 |
| Cadena o franquicia (3% churn) | ~USD 9.000 |
| Industria grande | ~USD 80.000 |

Hallazgo clave: "¿dónde abro?" se pregunta una vez. Lo recurrente es vigilar (competidores nuevos, cambios en la zona) y atender a cadenas, franquicias, corredores e industrias grandes.

## 5. APIs y fuentes de datos

### 5.1 Google Maps Platform

| API | Para qué | Estado / precio |
|---|---|---|
| Isochrones API | Áreas de tiempo de viaje | Versión preliminar. Gratis hasta 10.000 al mes; luego USD 3,00 por 1.000 (10.000–100.000), 2,40 (hasta 500.000), 1,80 (hasta 1 M), 0,90 (hasta 5 M) y 0,24 (más de 5 M). Calculado con USD 1 = COP 3.144,9. |
| Places API (New) | Competidores: calificación, reseñas, horarios, web | Es el costo principal por informe (estimado entre USD 0,10 y 0,30; confirmar en facturación) |
| Maps Grounding Lite | MCP oficial para agentes: buscar lugares (con resúmenes IA), clima y rutas | Versión preliminar, gratis durante la preview |
| Places Aggregate API | Contar lugares por tipo dentro de un área | Por probar |
| Routes API | Tiempos entre puntos | Ya existe en Aura, apagada |

Detalles de Isochrones (`POST https://isochrones.googleapis.com/v1/isochrones:generate`):

- Origen: coordenadas o `places/{place_id}`.
- `travelDuration`: hasta 7.200 s; en carro y moto, hasta 3.600 s.
- `travelMode`: `DRIVE`, `WALK`, `BICYCLE`, `TWO_WHEELER`.
- `travelDirection`: `FROM` ("a dónde llego") o `TO` ("quién llega a mí"). No es simétrico.
- `routingPreference`: `TRAFFIC_UNAWARE` (por defecto) o `TRAFFIC_AWARE`.
- Respuesta: un polígono en GeoJSON.

### 5.2 Reglas de Google que condicionan el diseño

- Solo el `place_id` se puede guardar indefinidamente. Calificaciones, reseñas y fotos no se pueden guardar en una base propia.
- Atribución obligatoria: logo o texto "Google Maps", enlaces a la ficha original, autores de reseñas y aviso en los resúmenes generados por IA.
- Grounding Lite solo se puede usar con modelos que cumplan los términos de Google, y su contenido no se puede guardar ni usar para entrenar.
- Consecuencia: la app funciona consultando en vivo. Una alerta de "competidor nuevo" funciona guardando solo IDs. Seguir los cambios de calificación es una zona gris que hay que revisar antes de prometerla.
- Los datos propios tienen que salir de fuentes públicas y de los resultados de los clientes, no de Google.

### 5.3 Datos públicos de Colombia (verificados en octubre de 2026)

**Población:**

- Censo DANE 2018: el último. El próximo está planeado para 2030; el conteo de 2025 no tiene resultados publicados que haya encontrado. Sirve para la estructura de cada manzana.
- Proyecciones de población del DANE (posCOVID): anuales, por municipio.
- Registro Estadístico Base de Población (DANE): población desde registros administrativos. Hay que revisar a qué nivel de detalle llega.
- Pobreza multidimensional por manzana (DANE).
- Encuesta Multipropósito Bogotá: trabajo de campo entre noviembre de 2025 y febrero de 2026, por UPZ. Ingresos, gastos y movilidad.

**Competencia y negocios:**

- Censo Económico Nacional Urbano 2024: 2.005.613 negocios contados manzana a manzana, con geovisor del DANE. Es público y sí se puede guardar: el reemplazo de Places para contar competidores.
- RUES en datos.gov.co (dataset `nb3d-v3n7`, API Socrata): 6,39 millones de registros, actualizado el 2 de octubre de 2026. Trae actividad (CIIU), fecha de matrícula y estado, pero no trae dirección ni coordenadas. Sirve para tendencias de aperturas.
- Direcciones de negocios: las venden las cámaras de comercio como servicio de bases de datos.

**Territorio (Bogotá):**

- Catastro, Predios: uso de cada predio y estrato. Anual; último el 30 de agosto de 2026.
- Mediana del avalúo catastral por manzana: un indicador de riqueza más reciente que el censo.
- Estratificación por manzana: ya está en `aura-lead-intelligence/src/estrato.py`.
- IDECA: ordenamiento territorial y POT.

**Población flotante:**

- Aforos vehiculares y peatonales de la Secretaría de Movilidad (datos abiertos, ArcGIS).
- Entradas por estación de TransMilenio: por confirmar.
- Aproximaciones: reseñas por mes y anclas cercanas (universidades, hospitales, oficinas, estaciones).
- Comerciales: datos de celulares de los operadores (PREDIK los usa) y datos de tarjetas (Mastercard, Visa).
- Google no entrega por API el horario de mayor afluencia.

**Comportamiento de consumo:** Encuesta Nacional de Presupuestos de los Hogares y GEIH (DANE).

### 5.4 Otros países

| País | Población | Negocios | Nivel socioeconómico |
|---|---|---|---|
| México | INEGI por manzana / AGEB | DENUE (público, con API) | NSE de la AMAI |
| Chile | INE por manzana | SII | GSE |
| Brasil | IBGE por setor censitário | CNPJ | Clases ABCDE |
| EE. UU. | Census ACS por block group; LEHD (dónde trabaja la gente) | Registros comerciales | Ingreso por zona |
| España | INE por sección censal | Catastro | Renta por sección |

Esta tabla sale de lo que sé de cada fuente, no de una revisión actual: hay que confirmar el acceso antes de construir. México es el siguiente país natural.

### 5.5 Alternativas abiertas, para no depender de Google

OpenRouteService y Valhalla calculan isócronas sobre OpenStreetMap. Google se queda para Places, que es lo difícil de reemplazar.

### 5.6 ¿Scraping?

Casi nunca hace falta. Todo lo demás llega por API, por descargas programadas o por servicios ArcGIS.

- Arriendos (Fincaraíz, Metrocuadrado): mejor por alianza; sus términos suelen prohibir el scraping.
- Direcciones de negocios: comprarlas a la cámara de comercio.
- Redes sociales: no.
- Noticias de proyectos: RSS y alertas.

## 6. Competencia

| Segmento | Quiénes | Precio | Para quién |
|---|---|---|---|
| Enterprise | Placer.ai, Esri Business Analyst, Buxton, SiteZeus | USD 10.000–100.000+ al año | Cadenas grandes |
| Pymes con suscripción | Smappen (Francia), Mapchise | Smappen: gratis y luego USD 99 / 199 / 399 al mes; Mapchise ~USD 149 al mes | Pymes y franquicias |
| IA por informe | WhereToOpen.ai, MapQuery | €99 por informe; USD 79 por informe o USD 49 al mes | Dueños de un local y corredores |
| APIs | TravelTime, Targomo, Mapbox | Por consumo | Desarrolladores |
| Colombia y LATAM | GeoMarketing Colombia SAS, PREDIK, inAtlas, Georesearch, GeoAdvisors (Chile), Datlas (México), North Alpha (México), Pickgeo (España) | Consultoría, sin precio público | Retail y cadenas medianas |
| Dentro de ChatGPT | TomTom, MixerBox ChatMap | — | Búsqueda de lugares y rutas, no análisis de mercado |
| Google | Maps Grounding Lite | Gratis en preview | La capa genérica para agentes |

Hueco: autoservicio para pymes, con precio publicado, en español, para LATAM y dentro de ChatGPT.

## 7. Tamaño del mercado

### 7.1 Cifras globales (contexto, no para decidir)

| Región | Tamaño | Crecimiento anual |
|---|---|---|
| Global | USD 21.200 M (2024) → 53.600 M (2030) | 16,8% |
| Norteamérica | USD 6.800 M (2024) | 14,9% |
| Europa | USD 5.600 M (2023) → 18.700 M (2032) | 14,3% |
| LATAM | USD 1.800 M (2025) | 15,7% |

Son cifras de consultoras (Grand View Research, Zion) que incluyen GIS de gobierno y logística. El mercado alcanzable real es mucho menor.

### 7.2 Cálculo de abajo hacia arriba (Colombia)

| Variable | Dato | Para qué |
|---|---|---|
| Empresas creadas al año | 297.475 (2024); 173.907 solo en el primer semestre de 2025 | Cuántos deciden ubicación cada año |
| Supervivencia a 5 años | 33,5% (micro 33,4%; pequeñas 60,9%; OCDE más de 40%) | El dolor y el argumento de venta |
| Comercio | 39% de las nuevas que generan empleo | Qué parte necesita un local |
| Franquicias | 542 marcas, ~18.000 puntos | El segmento de mayor valor |
| Cadenas con 3+ sedes | Se cuentan con Places por rubro y ciudad | El segmento Expansión |
| Unidades económicas urbanas | 2.005.613 (Censo Económico 2024) | El universo de negocios físicos |
| Corredores inmobiliarios | Por buscar (lonjas, Fedelonjas) | El segmento Corredor |
| Disposición a pagar | USD 49–99 en comparables | El precio |
| Penetración de ChatGPT en pymes | Por medir | El tamaño del canal |
| Conversión y churn | Por medir con las primeras ventas | Convierten el TAM en ingresos |

Ejemplo: 15% de las empresas nuevas abren local (~45.000) × 1% compra × USD 39 ≈ USD 17.500 al año. 5% de las franquicias × USD 299 al mes ≈ USD 97.000 al año. Una sola industria grande a USD 15.000 al año equivale a ~400 informes de pyme.

Conclusión: la pyme da volumen y marca; las cadenas, franquicias e industrias grandes pagan las cuentas.

## 8. ICPs

**Quienes van a abrir o expandir un local**

1. Emprendedores que abren su primer local
2. Clínicas veterinarias y odontológicas
3. Gimnasios y estudios boutique
4. Restaurantes y dark kitchens
5. Farmacias y droguerías independientes

**Cadenas y redes**

6. Cadenas con 3 a 30 sedes
7. Franquiciantes (territorios exclusivos)
8. Franquiciados que evalúan una zona
9. Colegios, jardines e institutos de idiomas
10. Laboratorios clínicos y centros de imágenes

**Quienes asesoran o venden a otros**

11. Corredores e inmobiliarias de locales comerciales
12. Desarrolladores de centros comerciales y locales de primer piso
13. Agencias de marketing local
14. Consultores de franquicias y de expansión
15. Bancos y fintech que dan crédito a pymes

**Operación y servicios**

16. Domicilios y última milla
17. Servicios técnicos a domicilio
18. Aseguradoras y redes de salud

**Industrias grandes:** consumo masivo (tiendas de barrio), bancos y cooperativas, cadenas de farmacias, telcos y salud (EPS, IPS, cajas de compensación).

Nota: en servicios de confianza (veterinaria, odontología) la cercanía pesa menos que la relación. Ahí el ángulo es la canibalización entre sedes, no la captación. La herramienta es más fuerte en compras frecuentes y de poca lealtad.

### Primer lote real (Bogotá, Chapinero a Usaquén, 19 de septiembre de 2026)

Archivo: `aura-lead-intelligence/data/busquedas/veterinarias_norte_bogota_2026-09-19.csv`. Cadenas con 3 o más sedes:

- Petplus: 9 sedes, calificaciones entre 3,8 y 5,0
- Movet: 5 sedes, 3.534 reseñas
- Animal Center: 4 sedes
- Vetas: 4 sedes, dentro de tiendas Laika
- CPA: 3 sedes, urgencias 24 horas

## 9. Dolores con respaldo

- Solo el 33,5% de las empresas colombianas sobrevive 5 años (Confecámaras).
- Las microempresas sobreviven la mitad que las pequeñas: 33,4% frente a 60,9%.
- La mala ubicación está entre las principales causas de cierre (estudios de la SBA).
- La pyme no puede pagar un consultor de ubicación (UNC School of Government).
- Las herramientas profesionales cuestan USD 10.000–100.000 al año y requieren GIS.
- Los datos están dispersos, desactualizados y no coinciden entre fuentes.
- El tiempo de viaje es el factor de mayor impacto en negocios de cara al cliente (Area Development).
- La invasión de territorio es una de las principales fuentes de conflicto en franquicias (Krispy Kreme es el caso más citado).
- La disponibilidad de mano de obra es el factor número 1 para el 54% de las empresas que se expanden (Area Development). La isócrona `TO` lo responde.
- Escasean los locales de calidad: es el segundo factor más citado.

Con menos respaldo: "60% de quienes eligen mal la ubicación pierden ingresos el primer año" viene de un blog de un proveedor. No usarlo sin la fuente original.

## 10. Intenciones de búsqueda (autocompletado de Google Colombia, 3 de octubre de 2026)

- Buscan guía, no un mapa: "dónde asesorarme para abrir un negocio", "por dónde empezar", "a dónde acudir".
- La pregunta al revés: "qué negocio poner en un barrio humilde / en un local pequeño / enfrente de una escuela".
- Competencia: "cuántas veterinarias hay en Bogotá".
- Por rubro: "estudio de mercado para una cafetería".
- Rentabilidad: "qué negocio es rentable en Bogotá 2025".
- Inmobiliario: "local comercial en arriendo" + ciudad.
- Profesional: "geomarketing colombia", "geomarketing gratis".

Falta: volúmenes, que se miden con Keyword Planner o con el crédito gratis de DataForSEO.

## 11. Cómo te encuentran

- El directorio de apps de ChatGPT, con nombre y descripción buscables.
- Contenido SEO/AEO por rubro y ciudad (conecta con Aura Organic Growth).
- Una herramienta gratis en la web: el mapa de 15 minutos sin registro.
- Estudios públicos ("Las 10 zonas de Bogotá sin veterinaria a 15 minutos").
- Aliados: cámaras de comercio, Colfranquicias, iNNpulsa, bancos para pymes, inmobiliarias y portales de arriendo.

## 12. Defensa frente a Google

- Google hace la capa genérica (Grounding Lite). No va a hacer el informe de una veterinaria en Cedritos con estrato y POT.
- Defensas: datos locales, datos propios de resultados de clientes, múltiples proveedores (OpenRouteService y Valhalla), el flujo completo hasta el plan comercial, y relaciones con aliados.
- Si Google lanza algo gratis: educa al mercado. La posición es "copiloto de expansión en LATAM": decisión, contexto local y plan de clientes, no "el mapa".

## 13. Lo que falta o hay que validar

**Técnico:**

- [x] Resolver el 403 de Isochrones (`API_KEY_SERVICE_BLOCKED`). La key del `.env` funciona con Places, pero no tiene Isochrones en sus restricciones de API. Revisar qué key es (sus últimos caracteres) y agregarle el permiso.
  - Resultados: `progress/exploracion_2026-10-03.md`.
- [x] Correr la prueba con Animal Center y CEBA (`scripts/isocronas_prueba.py`).
  - Resultados: `progress/exploracion_2026-10-03.md`.
- [ ] Confirmar el costo real de Places por informe en la facturación.
- [ ] Revisar los términos de Google para mostrar resultados dentro de ChatGPT y para guardar polígonos de isócronas.
- [ ] Confirmar si el seguimiento de calificaciones cumple los términos.

**Datos:**

- [ ] Descargar y revisar las variables reales del censo 2018 por manzana (Bogotá).
- [ ] Revisar el Censo Económico 2024: nivel de detalle y si se puede descargar o solo consultar en el geovisor.
- [ ] Catastro (predios y avalúo), aforos de Movilidad y TransMilenio.
- [ ] Resultados de la Encuesta Multipropósito 2025–2026.
- [ ] Datos de demanda por rubro (por ejemplo, hogares con mascota).
- [ ] Precios de arriendo, por alianza.

**Negocio:**

- [ ] Volúmenes de búsqueda.
- [ ] Disposición a pagar en Colombia: entrevistas con 5 a 10 ICPs.
- [ ] Churn y conversión reales.
- [ ] Cuántos corredores e inmobiliarias comerciales hay.
- [ ] Un nombre para el producto.

## 14. Lo que ya existe (en aura-lead-intelligence)

- `scripts/isocronas_prueba.py`: prueba con Animal Center y CEBA. Calcula el área, el solapamiento entre sedes y los competidores dentro de cada área. Se corre desde la terminal (Claude no puede leer el `.env`).
- `data/busquedas/veterinarias_norte_bogota_2026-09-19.csv`: 10 cadenas veterinarias calificadas.
- `src/estrato.py`: estrato oficial por manzana para Bogotá y Medellín.
- `src/places.py`: integración con Google Places.

## 15. Próximos pasos

1. Crear la carpeta del producto nuevo y mover este brief ahí.
2. Resolver el 403 y correr la prueba de isócronas.
3. Descargar los datos de Catastro, el Censo Económico 2024 y el censo 2018 de Bogotá.
4. Entrevistar a 5 ICPs (dos cadenas veterinarias, una inmobiliaria, un franquiciante y un emprendedor) antes de construir la app.
5. Programar el agente "Radar de ubicación" (sección 16).

## 16. Prompt del agente "Radar de ubicación"

Un agente programado una vez por semana. Solo investiga y reporta cambios nuevos.

```markdown
# Role
You are the Location Intelligence Radar for Aura Studio. Your only job is to
watch for NEW, verifiable information relevant to a location-intelligence
product (isochrones + Google Maps + public data, sold as a ChatGPT app and a
web product, starting in Colombia and expanding to LATAM). You research and
report. You never build, buy, sign up, send messages, or change anything
outside your own report and ledger files.

# Cadence and memory
- You run on a schedule. Each run, read `research/radar/ledger.json` first.
  It lists every item already reported (url, title, date_seen, hash of the key fact).
- Report only items that are new or materially changed since the last run.
- After reporting, append new items to the ledger. Never delete ledger entries.

# Watch list (check every run, in this order)
1. Google Maps Platform: Isochrones API (launch stage, pricing, quotas,
   terms), Maps Grounding Lite, Places API and Places Aggregate API (pricing,
   caching/storage terms, attribution rules), any new location/agent product.
2. ChatGPT apps: Apps SDK changes, app directory rules, monetization
   (especially digital goods/subscriptions), how apps get discovered or suggested.
3. Competitors: Smappen, WhereToOpen.ai, MapQuery, Placer.ai, Esri Business
   Analyst, TravelTime, Targomo, PREDIK, GeoMarketing Colombia, inAtlas,
   Georesearch, GeoAdvisors, Datlas, Pickgeo. Track launches, pricing,
   new countries, Spanish/LATAM versions, ChatGPT apps. Also search for NEW
   entrants ("site selection AI", "dónde abrir mi negocio IA", "geomarketing
   pymes", "isochrone ChatGPT app").
4. Public data, Colombia first: DANE (population count, Censo Económico
   Nacional Urbano final results, Registro Estadístico Base de Población,
   ENPH, GEIH, new block-level releases), Datos Abiertos Bogotá (Catastro
   predios, avalúo por manzana, estratificación, POT/IDECA, Movilidad aforos),
   Encuesta Multipropósito Bogotá 2025–2026 results, datos.gov.co RUES
   dataset nb3d-v3n7, Medellín open data. Then Mexico (INEGI DENUE, census by
   AGEB), Chile, Peru, Brazil.
5. Market signals: Confecámaras business creation/survival reports,
   Colfranquicias, Bogotá Metro progress by corridor, announced expansions of
   chains in Colombia (these are potential customers), new studies on why
   small businesses fail or how they choose locations.
6. Open-source alternatives: OpenRouteService, Valhalla, OpenStreetMap
   changes that affect isochrone quality or cost in LATAM.

# Rules
- Primary sources first: official docs, government portals, company pricing
  pages, press releases. Use news or blogs only to discover leads, then verify.
- Every item must cite a URL and the publication or update date. If you cannot
  verify a claim, label it "sin verificar" and say what would verify it.
- Never invent numbers, dates, prices or quotes. A missing value is written
  as "no publicado".
- Do not scrape sites whose terms forbid it, do not log in anywhere, do not
  bypass paywalls or CAPTCHAs, and do not collect personal data.
- Budget: at most 25 searches and 15 page fetches per run. If you hit the
  limit, stop and list what you did not check.
- If nothing new or material appears, write a one-line report saying so.
  Silence is a valid result.

# Triage each item
- ALTA: changes what Aura can build, charge or promise (pricing or terms
  change, new dataset at block level, competitor launches in Spanish/LATAM
  or inside ChatGPT, ChatGPT allows digital-goods monetization).
- MEDIA: useful context for product, pricing or sales.
- BAJA: worth knowing, no action.

# Output
Write `research/radar/YYYY-MM-DD.md` in Spanish, in this format:

## Radar de ubicación — {fecha}
**Resumen:** one sentence with the most important change, or "Sin novedades".

### ALTA
- **{Título}** — qué cambió, en una o dos frases.
  - Fuente: {URL} ({fecha de publicación o actualización})
  - Por qué importa para Aura: …
  - Acción sugerida: one concrete step (verificar, probar, ajustar precio,
    contactar como lead, ignorar).

### MEDIA
(same format)

### BAJA
(one line each, with URL)

### No revisado en esta corrida
(items skipped because of budget or errors)
```

## 17. Fuentes

**OpenAI / ChatGPT**

- https://openai.com/index/introducing-apps-in-chatgpt/
- https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/
- https://developers.openai.com/apps-sdk/build/monetization

**Google**

- https://developers.google.com/maps/documentation/isochrones/overview
- https://developers.google.com/maps/documentation/isochrones/reference/rest/v1/isochrones/generate
- https://developers.google.com/maps/ai/grounding-lite
- https://developers.google.com/maps/documentation/places/web-service/policies

**Competencia**

- https://www.smappen.com/travel-time-map/ · https://www.trustradius.com/products/smappen/pricing
- https://wheretoopen.ai/alternatives/esri-business-analyst
- https://mapquery.ai/blog/placer-ai-alternatives-for-small-business
- https://www.growthfactor.ai/resources/blog/retail-site-selection-software
- https://www.targomo.com/products/targomo-api/ · https://symaps.io/isochrone-map/
- https://connectamericas.com/es/company/geomarketing-colombia-sas · https://geomarketing.co/
- https://predikdata.com/es/ · https://www.datlas.mx/ · https://www.northalpha.com/ · https://pickgeo.com/ · https://www.geoadvisors.cl/
- https://www.tomtom.com/newsroom/product-focus/location-informed-chatgpt-plugin/

**Mercado**

- https://www.grandviewresearch.com/horizon/outlook/location-intelligence-market-size/global
- https://www.grandviewresearch.com/horizon/outlook/location-intelligence-market/latin-america
- https://www.grandviewresearch.com/horizon/outlook/location-intelligence-market/north-america
- https://www.zionmarketresearch.com/report/location-analytics-market

**Colombia**

- https://confecamaras.org.co/en-2024-se-crearon-en-el-pais-297-475-empresas-senala-informe-de-confecamaras/
- https://confecamaras.org.co/wp-content/uploads/2025/08/dinamica-de-creacion-de-empresas-en-colombia-op2-web.pdf
- https://confecamaras.org.co/segun-estudio-de-confecamaras-el-33-5-de-las-empresas-del-pais-sobreviven-al-termino-de-5-anos/
- https://www.semana.com/economia/capsulas/articulo/mas-de-540-marcas-impulsan-el-negocio-de-franquicias-en-colombia/202615/
- https://www.dane.gov.co/index.php/actualidad-dane/5878-el-dane-presento-los-resultados-preliminares-del-censo-economico-nacional-urbano
- https://geoportal.dane.gov.co/geovisores/economia/resultados-conteo/
- https://www.elpais.com.co/economia/habra-nuevo-censo-de-poblacion-el-dane-confirmo-las-fechas-para-esta-labor-0829.html
- https://datosabiertos.bogota.gov.co/dataset/predios-bogota
- https://datosabiertos.bogota.gov.co/dataset/mediana-del-avaluo-catastral-por-manzana/resource/0cdd251e-cd01-4829-ab3c-6bdaa94db13a
- https://www.sdp.gov.co/content/resultados-encuesta-multiproposito
- https://datosabiertos-movilidadbogota.hub.arcgis.com/
- https://www.datos.gov.co/en/Comercio-Industria-y-Turismo/Establecimientos-Agencias-Sucursales/nb3d-v3n7

**Dolores**

- https://www.entrepreneur.com/encyclopedia/location
- https://ced.sog.unc.edu/2025/11/07/perspectives-on-the-business-location-and-site-selection-process/
- https://www.areadevelopment.com/Corporate-Consultants-Survey-Results/q1-2026/40th-annual-corporate-22nd-annual-consultants-survey-results.shtml
- https://www.growthfactor.ai/resources/blog/franchise-territory-design-cannibalization

**Segmentación**

- https://en.wikipedia.org/wiki/Mosaic_(geodemography)
- https://en.wikipedia.org/wiki/Geodemographic_segmentation
