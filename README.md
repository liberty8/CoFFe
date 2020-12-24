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

## Ejemplos
> python coFFe.py -p 8080 -t 192.168.0.6 -l 192.168.0.10 -g 192.168.0.1 -i wlp1s0

https://github.com/mrx04programmer/CoFFe/tree/main/assets/imagen1.png


## Ayuda en Ejecución
- Se debe ejecutar el script con privilegios root.
- Se utiliza el parametro de puerto(-p) para definir el puerto a trabajar  (Aún esta en beta)
- Se utiliza el parametro de gateway (-g) para definir la IP del router o gateway.
- Se utiliza el parametro de target (-t) para definir la IP victima.
- Se utiliza el parametro de interface (-i) para definir el adaptador de red.
- Se utiliza el parametro de localdomain (-l) para definir la IP local del sistema
