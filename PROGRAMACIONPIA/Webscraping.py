import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import logging

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")


class WEBscraping:

    def Webscrappingmenu(self):

        while True:
            try:

                # URL del sitio web para hacer web scraping
                url = input("URL de tu eleccion: ")  # Reemplaza con la URL de tu elección  https://www.freeimages.com/es/photo
                if not url:
                    print("Direccion URL no valida. Intentelo de nuevo")
                    break
                else:
                    # Carpeta de destino para guardar las imágenes descargadas
                    carpeta_destino = input("Ruta de tu carpeta de destino: ")  # Reemplaza con la ruta de tu carpeta de destino    C:\Python\PROGRAMACIONPIA\Imagenes
                if not carpeta_destino:
                    print("Carpeta de destino no encontrada. intentelo de nuevo")
                    break
                else:
                    # Realizar la solicitud GET al sitio web y obtener el contenido HTML
                    response = requests.get(url)
                    html_content = response.content

                    # Crear un objeto BeautifulSoup para analizar el contenido HTML
                    soup = BeautifulSoup(html_content, "html.parser")

                    # Encontrar todas las etiquetas <img> en el contenido HTML
                    etiquetas_img = soup.find_all("img")

                    # Descargar y guardar las imágenes en la carpeta de destino
                    for etiqueta_img in etiquetas_img:
                        # Obtener la URL de la imagen y convertirla en una URL absoluta
                        src = etiqueta_img["src"]
                        imagen_url = urllib.parse.urljoin(url, src)

                        # Obtener el nombre de archivo de la imagen
                        nombre_archivo = os.path.basename(imagen_url)

                        # Descargar la imagen y guardarla en la carpeta de destino
                        imagen_respuesta = requests.get(imagen_url)
                        ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
                        with open(ruta_archivo, "wb") as archivo:
                            archivo.write(imagen_respuesta.content)

                        print(f"Imagen descargada: {nombre_archivo}")

                    print("Descarga de imágenes completada.")
                    break

            except Exception as error:
                logging.error(error, exc_info=True)
                print("Error")
