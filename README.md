## Resumen

El ransomware es un tipo de malware bastante común hoy en día; sin embargo, muchos usuarios aún no son conscientes de los daños que puede ocasionar. En el presente informe, se explica qué es un ransomware, sus tipos y se nombra algunos ejemplos de este malware con el objetivo de mostrar los potenciales daños, conocer su funcionamiento y evitar ser víctima de uno. Además, se desarrolla un prototipo de ransomware con el lenguaje python para una mejor explicación de su funcionamiento.

Antes de la ejecución del código, se debe ejecutar el archivo server.py con el objetivo de levantar un servidor local. Luego, tunelizamos dicho servidor con la herramienta ngrok. Por último, se debe modificar el código dependiendo del servidor y puerto generado por ngrok.

El código ProyectoConPassword encripta una sola carpeta, pero se puede cambiar fácilmente por todo el disco C:// en el caso de windows, o todo el directorio root en linux. 

## Ejecución

Primero se habilita el ssh, se ejecuta el programa server.py y por último se ejecuta ngrok.

https://user-images.githubusercontent.com/67574216/184583853-0ffc9517-1eeb-415b-9b12-00e24dc95ad8.mp4


