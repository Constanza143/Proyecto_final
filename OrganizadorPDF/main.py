import os
from archivos import buscar_pdfs
from unir import unir_pdfs

if __name__ == "__main__":
    carpeta = "pdfs"
    archivo_salida = "PDF_Final_Unido.pdf"

    if not os.path.isdir(carpeta):
        print("No se encontró la carpeta:", carpeta)

    else:
        archivos = buscar_pdfs(carpeta, archivo_salida)

        if not archivos:
            print("No se encontraron archivos PDF.")

        else:
            print("PDF encontrados:", len(archivos))

            unir_pdfs(
                archivos,
                os.path.join(carpeta, archivo_salida)
            )