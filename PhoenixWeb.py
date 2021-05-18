import dns.resolver
import requests
import time
import wget
from requests import get, exceptions
from os import path
from bs4 import BeautifulSoup
from progress.bar import Bar
from xml.etree.ElementTree import parse

def check_internet_connection():
    
    web1 = input("Introduzca el Sitio Web : ")

    try:
        get(web1, timeout = 4)
        print("Estado Activo")
    except exceptions.ConnectionError:
        print("Host Inactivo")
        
def verwordpress():
	url = input("Introduzca el Sitio Web : ")
	cabecera = {'User-Agent':'Firefox'}
	peticion = requests.get(url=url,headers=cabecera)
	soup = BeautifulSoup(peticion.text,'html5lib')
	for v in soup.find_all('meta'):
		if v.get('name') == 'generator':
			version = v.get('content')
	print(version)
    
def domserv():
	sitio = input("Introduzca el Dominio : ")
	agent = {'User-Agent':'Firefox'}
	a = requests.get("https://viewdns.info/reverseip/?host={}&t=1".format(sitio),headers=agent)
	b = BeautifulSoup(a.text,'html5lib')
	c = b.find(id="null")
	d = c.find(border="1")
	for l in d.find_all("tr"):
		print("Dominio alojado en el servidor: " + l.td.string)

def wp_plug():
	if path.exists("wp_plugins.txt"):
		w = open("wp_plugins.txt",'r')
		w = w.read().split('\n')
		lista = []
		url = input("Introduzca el Sitio Web : ")
		b = Bar("Espere...",max=len(w))

		for plugin in w:
			b.next()
			try:
				p = requests.get(url=url+"/"+plugin)
				if p.status_code == 200:
					final = url+"/"+plugin
					lista.append(final.split("/")[-2])
			except:
				pass
		b.finish()
		for plugin in lista:
			print("Plugin encontrado: {}".format(plugin))

	else:
		print("No se encuentra la lista")

def verjoomla():
    url = input("Introduzca el Sitio Web : ")
    download = wget.download(url + "/administrator/manifests/files/joomla.xml")
    archivo = parse("joomla.xml")
    for element in archivo.findall('version'):
	    ver = element.text

    print('\n\n'+ver)

def infodns():
    url = input("Introduzca el Dominio : ")
    informacion = ['A','AAAA','NS','SOA','MX','MF','MD','TXT']

    for x in informacion:
        try:
            a = dns.resolver.query(url, x)

            for q in a:
                print(q)
        except:
            print("No puede obtener la consulta")
        exit()

def temaswordp():
    url = input("Ingrese el Sitio Web : ")
    agent = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url,headers=agent)
    soup = BeautifulSoup(peticion.text,'html5lib')

    for enlace in soup.find_all('link'):
        if '/wp-content/themes/' in enlace.get('href'):
            the = enlace.get('href')
            the = the.split('/')
            if 'themes' in the:
                pos = the.index('themes')
                theme = the[pos+1]
                print("Tema Vulnerable: " + theme)
            exit

def subdomain():
    domain = input("Introduzca el Dominio : ")
    if path.exists('subdominios.txt'):
        wordlist = open('subdominios.txt','r')
        wordlist = wordlist.read().split('\n')
        lista = []
        for s in wordlist:
            try:
                a = dns.resolver.query("{}" + "." + url.format(s),'A')
                lista.append("{}" + "." + url.format(s))
            except:
                pass
        if len(lista) > 0:
            print('Numero de subdominios posibles: {}'.format(len(lista)))
            for e in lista:
                print(e)
        else:
            print("No se encontraron subdominios")
    else:
        print("No existe el archivo")
        exit()

def salir():
    print('\033[5;31m' "<<<<<<<<<<Saliendo de la Herrameinta>>>>>>>>>>")
    time.sleep(3)
    exit()


banner = """

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

@@@@@@@   @@@  @@@   @@@@@@   @@@@@@@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!@!@@@  @@!  @@!  !@@  @@!  @@!  @@!  @@!       @@!  @@@  
!@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!!@!@!  !@!  !@!  @!!  !@!  !@!  !@!  !@!       !@   @!@  
@!@@!@!   @!@!@!@!  @!@  !@!  @!!!:!    @!@ !!@!  !!@   !@@!@!   @!!  !!@  @!@  @!!!:!    @!@!@!@   
!!@!!!    !!!@!!!!  !@!  !!!  !!!!!:    !@!  !!!  !!!    @!!!    !@!  !!!  !@!  !!!!!:    !!!@!!!!  
!!:       !!:  !!!  !!:  !!!  !!:       !!:  !!!  !!:   !: :!!   !!:  !!:  !!:  !!:       !!:  !!!  
:!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!  :!:  :!:  !:!  :!:  :!:  :!:  :!:       :!:  !:!  
 ::       ::   :::  ::::: ::   :: ::::   ::   ::   ::   ::  :::   :::: :: :::    :: ::::   :: ::::  
 :         :   : :   : :  :   : :: ::   ::    :   :     :   ::     :: :  : :    : :: ::   :: : ::   
                                                                                                    
Canal Youtube: https://www.youtube.com/channel/UConS1Dk6zZAOFuaSwTtLbqA

Github: https://github.com/DarkPhoenix2020

PayPal: https://www.paypal.com/paypalme/DarkPhoenix87EH

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


"""

while True:
    def main():
        print('\033[0;33m' + banner + '\033[0;33m')
        menu = """
        
                            <<<<    MENU    >>>>

        (1) VERIFICAR EL ESTADO DE UN SITIO WEB (ACTIVO/INACTIVO)
        (2) OBTENER LA VERSION DE WORDPRESS QUE UTILIZA UN SITIO WEB
        (3) DETECTAR DOMINIOS ALOJADOS EN UN SERVIDOR
        (4) CONOCER LOS PLUGINS UTILIZADOS DE LA VERSION WORDPRESS DE UN SITIO WEB
        (5) OBTENER LA VERSION JOOMLA DE UN SITIO WEB
        (6) OBTENER INFORMACION DEL DNS DE UN DOMINIO
        (7) OBTENER TEMAS DE VERSIONES DE WORDPRESS DE UN SITIO WEB
        (8) OBTENER LOS SUBDOMINIOS DE UN DOMINIO
        (99) Salir
    
    """
        print('\033[1;36m' + menu + '\033[1;36m')

        opcion = input("Ingrese el Numero, que corresponda a la Opcion deseada : ")

        if opcion == "1":
            check_internet_connection()
        elif opcion == "2":
            verwordpress()
        elif opcion == "3":
            domserv()
        elif opcion == "4":
            wp_plug()
        elif opcion == "5":
            verjoomla()
        elif opcion == "6":
            infodns()
        elif opcion == "7":
            temaswordp()
        elif opcion == "8":
            subdomain()
        elif opcion == "99":
            salir()
        else:
            print("Opcion Incorrecta ")

    main()
