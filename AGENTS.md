# AGENTS.md — Mapa del repositorio de aura-location-intelligence

Este archivo es un mapa, no un reglamento. Dice dónde está cada cosa y cuándo
leerla. Las reglas del proyecto viven en `CLAUDE.md` y `docs/`.

## 1. Antes de empezar

1. Ejecuta `./init.sh`. Si sale con código distinto de 0, para y arréglalo.
2. Lee el documento activo en `odd/tasks/` (estado real de la tarea).
3. Trabaja una tarea a la vez; no abras la siguiente sin cerrar la actual.

## 2. Mapa del repositorio

| Archivo o carpeta | Qué contiene | Cuándo leerlo |
|---|---|---|
| `CLAUDE.md` | Identidad, propósito y arranque (carga en cada sesión) | Siempre |
| `odd/tasks/` | Documentos de tarea (estado, checklist, evidencias) | Al empezar y al cerrar cada tarea |
| `progress/` | `current.md` (sesión activa) e `history.md` (bitácora) | Al delegar o cerrar sesión |
| `init.sh` | Puerta de inicio y cierre (entorno, archivos, pruebas, seguridad) | Al empezar y antes de dar algo por hecho |
| `.claude/` | `harness.env`, `settings.json` y hooks | Al ajustar el arnés |
| `CHECKPOINTS.md` | Lista verificable de cierre | Antes de cerrar la sesión |
| `BRIEF.md` | Qué es el producto, por qué, mercado, fuentes y pendientes | Antes de decidir alcance o prioridades |
| `src/location_intelligence/` | Código del producto (hoy: `archivos.py`, validación de archivos subidos) | Al implementar |
| `tests/` | Pruebas con pytest (sin llamadas a APIs reales) | Al cambiar código |
| `scripts/` | Pruebas exploratorias contra APIs reales de Google (isócronas, conteo y listado de competidores) | Para repetir una exploración; no es código de producto |
| `progress/exploracion_*.md` | Resultados de las exploraciones con sus límites | Antes de repetir una prueba o citar un número |
| `data/` | Polígonos generados por los scripts (ignorado en git) | Solo lo leen los scripts |
| `.env` | `GOOGLE_MAPS_API_KEY` (ignorado en git; el agente no puede leerlo) | Nunca: lo edita la persona |

## 3. Reglas duras

- Ninguna tarea está terminada sin `./init.sh` en verde.
- Cero secretos en commits: `.env` está en `.gitignore`.
- Nunca inventar datos.
- Todo archivo subido se valida por contenido con Magika (`location_intelligence.archivos.validar_archivo`) antes de procesarlo; nunca confiar en la extensión.
- Cada número del producto cita su fuente y su fecha. Un dato sin fuente se escribe como "no publicado".
- Ninguna fuente sola es verdad: un competidor se da por confirmado solo si aparece en al menos dos fuentes (Google, Censo Económico 2024, RUES) y tiene una señal de actividad reciente.
- De Google solo se guarda el `place_id`. Calificaciones, reseñas, nombres y fotos se consultan en vivo y no se persisten.
- El estrato es solo el oficial y nunca se infiere.
- Los resultados de exploraciones van a `progress/`, no a `BRIEF.md`.

## 4. Subagentes

- El orquestador delega; los subagentes ejecutan una unidad acotada.
- Cada subagente escribe su resultado en `progress/<tipo>_<tema>.md` y
  responde solo `done -> progress/<archivo>` o `blocked -> <motivo>`.
- El estado de las tareas vive en `odd/tasks/`, no en `progress/`.

## 5. Cierre de sesión

1. `./init.sh` en verde.
2. Actualizar los checkboxes de `odd/tasks/` con evidencia (comando y resultado, hash de commit).
3. Añadir una línea a `progress/history.md`.
4. Commit por unidad de trabajo con Conventional Commits.
