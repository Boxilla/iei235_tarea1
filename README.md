# [IEI235] Tarea1

Tarea numero 1 de la asignatura IEI235-Pruebas de Software, donde se debe crear un programa que comprima una cadena de caracteres.

## Descripcion

El proposito de este programa es  realizar una compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena aabcccccaaa se convertiría en a2b1c5a3. Si la cadena "comprimida" no fuera más pequeña que la cadena original, su método debería devolver la cadena original, ademas crea un archivo llamado "log_tarea1_iei235.txt" donde se agrega una linea con la fecha de ejecución, los strings ingresados y el resultado de la comprension cada vez que el programa es ejecutado con exito.

## Ejecucion

Para ejecutar el programa y que cumplá totalmente su funcionaldiad se debe tener instalada la versión 3 de python.
Como el programa genera un documento se deben tener permisos suficientes para esto al ejecutar el programa.

El codigo fue escrito en python version 3.8.7

En ubuntu se ejecutaria de la siguiente forma estando en el directorio donde se encuentra el archivo "Tarea1.py"

```bash
python3 Tarea1.py
```

## Uso
Luego de ejecutar el programa este pedira primero un string donde se debe escribir la cadena que se desee comprimir y luego presionar enter, despues de esto retornará la cadena comprimida, si es que esta es más pequeña que la cadena ingresada inicialmente.

El programa solo recibe cadenas de largo mayor a 0, por lo que si no se ingresa ninguna cadena el programa pedira una hasta que se ingrese alguna.

Para finalizar el programa se debe escribir "x", como lo indica por pantalla el mismo programa.

```bash
'Ingrese cadena: 🐫🐿🐿🐿🐿🐿🐽🐽🐽🐽🐽🐽'
'🐫1🐿5🐽6'
'ENTER para repetir, o escriba X para salir.'
'Ingrese cadena: 🐫🐿🐿🐿🐿🐿🐽🐽🐽🐽🐽🐽🐫🐿🐿🐿🐿🐿🐽🐽🐽🐽🐽🐽'
'🐫1🐿5🐽6🐫1🐿5🐽6'
'ENTER para repetir, o escriba X para salir.x'

```

* Se suprimio el uso de tildes en este readme
