# CoFFe ☕️
CoFFe es un script en Python para realizar un ataque de tipo man-in-the-middle (MITM) con redirección de tráfico HTTP , es para propósitos educativos y de investigación, no para uso malintencionado.
Requisitos

    Python 2.x
    Librerías: argparse


Clona el repositorio:

    git clone https://github.com/tu_usuario/CoFFe.git
Navega al directorio del proyecto:
    
    cd CoFFe

Ejecuta el script como superusuario, proporcionando los parámetros necesarios:


    sudo python3 CoFFe.py -p [PUERTO] -g [GATEWAY] -t [TARGET] -l [IP_LOCAL] -i [INTERFAZ]

        -p [PUERTO]: Puerto a utilizar.
        -g [GATEWAY]: IP del gateway (router).
        -t [TARGET]: IP de la víctima.
        -l [IP_LOCAL]: IP local del sistema.
        -i [INTERFAZ]: Interfaz de red a utilizar.

## Funcionalidades

    Configura IP forward y tablas iptables.
    Redirige el tráfico HTTP/s visiblemente (con envenenamiento)
    Muestra información detallada del ataque.

🔒 Notas de Seguridad

    Este script debe utilizarse solo con permiso explícito en redes autorizadas.
    No se recomienda su uso en redes públicas o sin autorización, ya que puede ser ilegal y/o violar la privacidad de otros usuarios.

## Ejecución
##### En esta ocasión establecí el puerto 8080, la victima sera 192.168.0.6 , la ip de mi router 192.168.0.1 y la interfaz de red wlp1s0
    sudo python coFFe.py -p 8080 -t 192.168.0.6 -l 192.168.0.10 -g 192.168.0.1 -i wlp1s0
![imagen](https://github.com/mrx04programmer/CoFFe/assets/46001898/1b02a19c-398b-4e49-bfc6-743ccb2b9bc6)



##### Ejecutamos ettercap en modo de interfaz grafico (GUI) 
    etttercap -G
![imagen](https://github.com/mrx04programmer/CoFFe/assets/46001898/69c5b1a2-c7fc-44c0-99c5-2c59f0b3ddf7)

- Alistamos la lista de host (CTRL + H)
- Buscamos objetivos (CTRL + S)
- Agregamos la IP victima a **TARGET 1** y la IP del router (gateway) a **TARGET 2**
!Nos vamos al menú de MITM y nos vamos al apartado de ARP poisosing (así como se visualiza en la imagen)
![imagen](https://github.com/mrx04programmer/CoFFe/assets/46001898/0ad663a1-5b99-4d55-9786-ec06ba19440a)

- En este momento ya estaremos capturando y exportando el trafico, donde se pueden realizar cualquier otro tipo de sniffing y spoofing de tablas ARP. tales como wireshark, sslstrip, snort, etherape, etc.
- Para visualizar el trafico guardado como dump.pcap (por defecto) en wireshark, se ejecuta:
  > wireshark -r dump.pcap
  - Y ingresamos el filtro para visualizar solo el trafico de una sola IP (el objetivo)
  > ip.addr == <ip_objetivo>

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit de ellos (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Crea un nuevo Pull Request.


