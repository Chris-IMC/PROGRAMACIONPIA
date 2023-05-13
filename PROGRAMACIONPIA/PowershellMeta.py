import subprocess
import logging

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")

class PowerShell:

    def Powershell(self):

        while True:
            try:
                resultado = subprocess.run(["powershell.exe", "-File", "Powershellmetadatos.ps1"], capture_output=True)
                print(resultado.stdout.decode())
                break
            except Exception as error:
                logging.error(error, exc_info=True)
                print("Error")
