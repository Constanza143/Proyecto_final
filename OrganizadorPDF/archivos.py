import os

def buscar_pdfs(carpeta, archivo_salida):
    ruta_salida = os.path.abspath(
        os.path.join(carpeta, archivo_salida)
    )

    archivos = []

    for nombre in os.listdir(carpeta):
        ruta = os.path.join(carpeta, nombre)

        if (nombre.lower().endswith(".pdf")
                and os.path.abspath(ruta) != ruta_salida):
            archivos.append(ruta)

    archivos.sort(key=lambda ruta: os.path.basename(ruta).lower())

    return archivos