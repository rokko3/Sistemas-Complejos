# Descripcion de Maquina de turing para envio de informacion digital

## El transmisor tiene 3 Operaciones para enviar datos:
* Crear la funcion de datos D(t) en voltios +1 para 1 y -1 para 0, en un tiempo t
* Crear la frecuencia haciendo uso del oscilador
* Usar el oscilador para preparar los datos de transmision
* Enviar los datos

## El oscilador

* Debe recibir la frecuencia para preparar la funcion de oscilamiento
* Debe retornar la funcion de oscilamiento
* Debe ser capaz de demodular la informacion
* Debe multiplicar la funcion de datos por la funcion de oscilador

## El receptor

* Debe recibir la funcion de la señal recibida
* Usar el oscilador para demodular la frecuencia
* Mostrar los datos recibidos

