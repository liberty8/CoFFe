# CoFFe Man in the Middle 
Ataque Man in the Middle simple, utilizando [mitm6](https://github.com/fox-it/mitm6) y [netsniff-ng](https://github.com/netsniff-ng/netsniff-ng).
El script se debe complementar con ettercap para ejecutar mitm6 correctamente.

## Requisitos
- xterm
> apt install xterm
- python
> apt install python
- netsniff-ng
> apt install netsniff-ng
- mitm6 [(Desde github)](https://github.com/fox-it/mitm6) o desde pip
> pip install mitm6

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


## Ayuda en Ejecución
- Se debe ejecutar el script con privilegios root.
- Se utiliza el parametro de puerto(-p) para definir el puerto a trabajar  (Aún esta en beta)
- Se utiliza el parametro de gateway (-g) para definir la IP del router o gateway.
- Se utiliza el parametro de target (-t) para definir la IP objetivo.
- Se utiliza el parametro de interface (-i) para definir el adaptador de red.
- Se utiliza el parametro de localdomain (-l) para definir la IP local del sistema
