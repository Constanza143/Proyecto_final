from pypdf import PdfWriter, PdfReader

def unir_pdfs(archivos, ruta_salida):
    escritor = PdfWriter()
    procesados = 0

    for ruta in archivos:
        try:
            lector = PdfReader(ruta)

            if lector.is_encrypted:
                print("PDF protegido:", ruta)
                continue

            for pagina in lector.pages:
                escritor.add_page(pagina)

            procesados += 1
            print("Agregado:", ruta)

        except Exception as error:
            print("Error al leer", ruta, ":", error)

    if procesados == 0:
        print("No se pudo procesar ningún PDF.")
        return False

    with open(ruta_salida, "wb") as salida:
        escritor.write(salida)

    print("PDF unificado creado:", ruta_salida)
    return True