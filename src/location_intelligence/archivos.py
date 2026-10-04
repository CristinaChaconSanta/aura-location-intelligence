"""Single entry point to validate files uploaded by users.

The file type is decided by content with Magika, never by the extension or the
name the user sent. Magika detects the type only; it does not detect malware.
"""
from functools import lru_cache

from magika import Magika

TIPOS_PERMITIDOS = frozenset({"csv", "xlsx", "pdf"})
TAMANO_MAXIMO_BYTES = 10 * 1024 * 1024


class ArchivoRechazado(ValueError):
    """The upload is not an allowed type or is too large."""


@lru_cache(maxsize=1)
def _magika() -> Magika:
    return Magika()


def validar_archivo(contenido: bytes) -> str:
    """Return the detected type label, or raise ArchivoRechazado."""
    if not contenido:
        raise ArchivoRechazado("archivo vacío")
    if len(contenido) > TAMANO_MAXIMO_BYTES:
        raise ArchivoRechazado("archivo demasiado grande")
    tipo = _magika().identify_bytes(contenido).output.label
    if tipo not in TIPOS_PERMITIDOS:
        raise ArchivoRechazado(f"tipo no permitido: {tipo}")
    return tipo
