import PyPDF2
import logging

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class Metadata:

    def MetadataPDF(self):

        while True:
            try:
                pdf = open("Textos y actividades del Manual de la Cultura de la Legalidad.pdf", "rb")
                reader = PyPDF2.PdfReader(pdf)

                pagenumber = int(input("Ingresa un numero:"))
                page = reader.getPage(pagenumber)
                metad = reader.metadata
                if not pagenumber:
                    print("Numero de pagina no valida. Intente de nuevo")
                else:

                    print("Extrayendo texto del pdf..")
                    file = open('MetadataPDF.txt', 'a+', encoding="utf=8")

                    file.write("Texto extraido del pdf")
                    file.write('''
                        Texto del pdf: {}


                        '''.format(page.extractText()))
                    file.write("Metadata del pdf")
                    file.write('''
                        Fecha de creacion: {}
                        Creador: {}
                        ModDate: {}
                        Producer: {}
                        Autor: {}


                        '''.format(metad.creation_date, metad.creator, metad.modification_date, metad.producer,
                                   metad.author))
                    file.close()

                    print("Archivo txt guardado con exito")

                    break
            except Exception as error:
                logging.error(error, exc_info=True)
                print("Error")
