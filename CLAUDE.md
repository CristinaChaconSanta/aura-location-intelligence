# aura-location-intelligence

## Identidad y propósito

Copiloto de expansión para negocios físicos en LATAM, de Aura Studio. Responde
dónde abrir, qué abrir y cómo venderle a la gente de una zona, combinando áreas
de tiempo de viaje (isócronas), competencia real y datos públicos del territorio.
Empieza en Bogotá. El producto todavía no tiene nombre.

Axioma: información verídica o nada. Cada número dice de dónde sale y de qué
fecha es; lo que no se puede verificar se marca como tal.

## Arranque obligatorio

1. `./init.sh` debe salir con código 0. Si falla, arréglalo antes de trabajar.
2. Lee `AGENTS.md`: mapa del repositorio y reglas duras.
3. Lee el documento activo en `odd/tasks/`. Una tarea a la vez.

## Principios

- Primero lo pequeño que alguien pagaría: un rubro, una ciudad, un informe.
  Lo demás queda como pendiente hasta que haya demanda.
- Ninguna fuente sola es verdad; se cruzan Google, DANE y RUES.
- Las pruebas nunca llaman a APIs reales; las exploraciones viven en `scripts/`.
- El `.env` lo edita solo la persona; el agente no lo lee.

## Punteros

- Producto, mercado y fuentes: `BRIEF.md`
- Resultados de exploraciones: `progress/exploracion_*.md`
- Verificación de cierre: `CHECKPOINTS.md`
