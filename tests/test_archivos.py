import pytest

from location_intelligence.archivos import ArchivoRechazado, TAMANO_MAXIMO_BYTES, validar_archivo

CSV_SEDES = b"sede,lat,lng\nCedritos,4.72,-74.04\nRosales,4.65,-74.05\nGalerias,4.64,-74.07\n"
PDF_MINIMO = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF"
SCRIPT_DISFRAZADO = b"#!/bin/bash\nrm -rf /tmp/x\necho hi\n"


def test_accepts_real_csv():
    assert validar_archivo(CSV_SEDES) == "csv"


def test_accepts_real_pdf():
    assert validar_archivo(PDF_MINIMO) == "pdf"


def test_rejects_script_named_like_an_image():
    # The name "foto.jpg" never reaches the validator: only content decides.
    with pytest.raises(ArchivoRechazado, match="tipo no permitido"):
        validar_archivo(SCRIPT_DISFRAZADO)


def test_rejects_empty_file():
    with pytest.raises(ArchivoRechazado, match="vacío"):
        validar_archivo(b"")


def test_rejects_oversized_file():
    with pytest.raises(ArchivoRechazado, match="grande"):
        validar_archivo(b"a" * (TAMANO_MAXIMO_BYTES + 1))
