import argparse
import os
import logging
from HASH import Hash
from Configloggin import ConfigurarLogging
from Nmap import Nmap
from PYPDF2 import Metadata
from Apishodan import APIshodan
from Webscraping import WEBscraping
from PowershellMeta import PowerShell

def main():


    parser = argparse.ArgumentParser(description='Tareas de Ciberseguridad')
    parser.add_argument('--Escaneo_de_puertos_nmap', '-E', help="Escáner de puertos que permite identificar puertos abiertos, cerrados o filtrados", action='store_true')
    parser.add_argument('--Api_de_shodan', '-S', help="Extrae informacion de diversos tipos de dispositivos en internet")
    parser.add_argument('--Webscraping', '-W', help="Obten y guarda imagenes de un url en una carpeta")
    parser.add_argument('--Metadatapdf', '-M', help="Extrae metadata de archivos pdf")
    parser.add_argument('--Hash', '-H', help="Extrae el valor hash de un archivo")
    parser.add_argument('--Powershell', '-P', help="Extrae metadata de imagenes guardas en el dispositivo")

    args = parser.parse_args()
    if args.Escaneo_de_puertos_nmap:
        nmap = Nmap()
        nmap.DireccecionIp()


    elif args.Api_de_shodan:
        apishodan = APIshodan()
        apishodan.shodanmenu()

    elif args.Webscraping:
        scraping = WEBscraping()
        scraping.Webscrappingmenu()

    elif args.Metadatapdf:
        metadata = Metadata()
        metadata.MetadataPDF()

    elif args.Hash:
        hash = Hash()
        hash.menu()

    elif args.Powershell:
        power = PowerShell()
        power.Powershell()

if __name__ == "__main__":
    main()
