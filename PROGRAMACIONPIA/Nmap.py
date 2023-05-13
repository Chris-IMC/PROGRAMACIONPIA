import nmap
import csv
import os
import logging

# 148.234.5.206
logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class Nmap:
    def DireccecionIp(self):
        print("Ingrese la direccion ip que desea escanear:")
        target = input("IP: ")

        while True:
            try:

                    print('Escaneando:')

                    scanner = nmap.PortScanner()
                    sc = scanner.scan(hosts=target, arguments='--open')
                    hosts_list = [(x, sc['scan'][x]['hostnames'][0]['name'], list(sc['scan'][x]['tcp'].keys())) for x in
                                  scanner.all_hosts()]

                    for item in hosts_list:
                        with open('scanHosts11.csv', 'a', newline='') as csvf:
                            writer = csv.writer(csvf)
                            writer.writerow(item)
                    print('Listo')
                    break
            except Exception as error:
                logging.error(error, exc_info=True)
                print("Error" )


