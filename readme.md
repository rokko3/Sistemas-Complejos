# Simulador de Transmision BPSK con Maquinas de Turing

Hecho por: William Alfonso, Cristian Bello, Daniel Oviedo
## Descripcion General

El simulador demuestra como un texto plano se convierte en bits, luego en ondas de radiofrecuencia (modulacion BPSK), sobrevive a un canal con ruido y finalmente es demodulado para recuperar el mensaje original. Lo hace mediante cuatro modulos principales que simulan maquinas de estado:

1.  **Emisor**: Traduce texto humano a una cadena binaria (ASCII) y formatea la "cinta" preparandola para la transmision.
2.  **Oscilador (Maquina de Turing)**: Lee la cinta formateada, extrae la frecuencia de trabajo y convierte los bits en arrays matematicos que representan ondas (Cosenos desfasados).
3.  **Canal**: Aplica ruido estocastico a la senal para simular las condiciones de propagacion reales.
4.  **Receptor y Demodulador**: Analiza la cinta recibida, recupera la frecuencia de transmision, emplea un Filtro Adaptado (multiplicacion e integracion) para discriminar el ruido y decodifica la senal nuevamente a texto plano.

## Funcionamiento de la Interfaz Grafica

La interfaz esta desarrollada con CustomTkinter y Matplotlib. Se divide en dos paneles principales:

### Panel de Controles (Izquierdo)
*   **Datos a enviar**: Cuadro de texto donde el usuario ingresa el mensaje a transmitir.
*   **Frecuencia Portadora**: Control deslizante que determina la frecuencia de la onda portadora. El valor se actualiza en tiempo real.
*   **Nivel de Ruido en el Aire**: Control deslizante que ajusta la amplitud del ruido blanco estocastico introducido en la senal.
*   **Modular y Transmitir**: Inicia el proceso de codificacion y modulacion, lanzando la senal al "aire".
*   **Recibir y Demodular**: Captura la senal ruidosa y realiza el procesamiento inverso para recuperar los datos.

### Panel de Visualizacion (Derecho)
Contiene tres lienzos de Matplotlib que se actualizan de forma reactiva:
*   **Senal Digital (Banda Base)**: Muestra la cadena de bits puros (ondas cuadradas) lista para ser inyectada al oscilador.
*   **Onda Transmitida (RF + Ruido)**: Visualiza la forma de la onda senoidal continua volando por el espacio con el nivel de ruido aplicado.
*   **Senal Digital Recuperada**: Grafica los bits que sobrevivieron al filtro adaptado del receptor, demostrando la fiabilidad del algoritmo ante la interferencia.

## Requerimientos e Instalacion

El proyecto fue desarrollado utilizando Python 3. Se requieren las siguientes librerias para su funcionamiento:

*   customtkinter
*   numpy
*   matplotlib

Para instalar las dependencias, ejecute en su terminal:
pip install customtkinter numpy matplotlib

## Uso

Para iniciar el simulador, simplemente ejecute el archivo principal de la interfaz desde la consola:
python grafica.py

Una vez abierta la interfaz, ingrese un texto, ajuste los parametros fisicos de transmision (frecuencia y ruido) y presione el boton de transmitir para observar las graficas generadas. Finalmente, utilice el boton del receptor para comprobar la recuperacion de datos.
