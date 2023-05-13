import logging
import os
import sys
from datetime import datetime
from pathlib import Path

class ConfigurarLogging:

    def FoldeLog():

        Programa = os.path.basename(sys.argv[0]).lower()
        Programa = os.path.splitext(Programa)[0]

        Folder = os.path.join(".config", Programa)
        Folder = os.path.join(Path.home(), Folder)
        Folder = os.path.join(Folder, "logs")

        return Folder


    def ConfigurarLogging(Nombre, NivelLog=logging.DEBUG):

        logger = logging.getLogger(Nombre)
        logger.setLevel(NivelLog)

        ArchivoLog = FoldeLog()

        if not os.path.isdir(ArchivoLog):
            os.makedirs(ArchivoLog)

        return logger
