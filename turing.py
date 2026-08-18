import numpy as np
class MaquinaTuringOscilador:
    def __init__(self, cinta_inicial):
        self.cinta = list(cinta_inicial)
        self.cabezal = 0
        self.estado_actual = "q0_buscando_f"
        
        # En la teoría estricta, una Máquina de Turing usaría otra sección de la cinta 
        # para "recordar" esto. Para hacerlo programable sin crear infinitos estados,
        # le daremos una pequeña memoria interna al cabezal.
        self.memoria_frecuencia = ""
        
    def paso(self):
        """Ejecuta un solo paso del cabezal""" # Creacion de cinta inifinita, si sale por derecha se agrega, si es por izquierda se inserta
        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0

        simbolo_leido = str(self.cinta[self.cabezal]) #lee el dato en la posicion que se encuentra el cabezal
         
        # Valores por defecto: dejar la cinta igual y moverse a la derecha
        escribir = simbolo_leido
        movimiento = "DERECHA"
        nuevo_estado = self.estado_actual

        
        if self.estado_actual == "q0_buscando_f":
            if simbolo_leido == "f":
                nuevo_estado = "q1_leer_frecuencia"
            # Si es cualquier otra cosa, lo deja igual y avanza

        elif self.estado_actual == "q1_leer_frecuencia":
            if simbolo_leido == " ":
                # Si encuentra un espacio, verifica si ya leyó números antes
                if self.memoria_frecuencia != "":
                    nuevo_estado = "q2_procesar_datos"
            elif simbolo_leido.isdigit() or simbolo_leido == ".":
                # Si lee un número (int) o un punto (float), lo acumula en memoria
                self.memoria_frecuencia += simbolo_leido
            # Continúa en q1 leyendo caracteres numéricos hasta encontrar el próximo espacio

        elif self.estado_actual == "q2_procesar_datos":
            if simbolo_leido == " ":
                pass # Ignorar espacios entre datos
            elif simbolo_leido == "1":
                # Armamos la función con la frecuencia exacta leída (sea int o float)
                #escribir = f"+cos({self.memoria_frecuencia}t)"
                frecuencia=float(self.memoria_frecuencia)
                tiempo=np.linspace(0,1,1000)
                onda=+np.cos(2*np.pi*frecuencia*tiempo)
                ruido=np.random.normal(0,0.5,1000)
                escribir=onda+ruido
            elif simbolo_leido == "0":
                #escribir = f"-cos({self.memoria_frecuencia}t)"
                frecuencia=float(self.memoria_frecuencia)
                tiempo=np.linspace(0,1,1000)
                onda=-np.cos(2*np.pi*frecuencia*tiempo)
                ruido=np.random.normal(0,0.5,1000)
                escribir=onda+ruido
            elif simbolo_leido == "_":
                # Fin de la cinta
                nuevo_estado = "q_fin"
                movimiento = "CENTRO"

        # Aplicar acciones físicas
        self.cinta[self.cabezal] = escribir
        self.estado_actual = nuevo_estado
        
        if movimiento == "DERECHA":
            self.cabezal += 1
        elif movimiento == "IZQUIERDA":
            self.cabezal -= 1

    def ejecutar(self):
        #print(f"Cinta Inicial: {self.cinta}")
        pasos = 0
        while self.estado_actual != "q_fin":
            self.paso()
            pasos += 1
            if pasos > 50:
                #print("Seguridad: Bucle infinito detenido.")
                break
        #print(f"Cinta Final:   {self.cinta}")
        return self.cinta

if __name__ == "__main__":
    cinta_prueba = ["a", "f", "2", ".", "4", " ", "1", "0", "1"]
    print("Iniciando con frecuencia Float (2.4)...")
    maquina = MaquinaTuringOscilador(cinta_prueba)
    result=maquina.ejecutar()
    print(result)

    cinta_prueba_int = ["x", "y", "f", " ", "2", "4", "0", "0", " ", "0", "1", "0", "1", "_"]
    print("Iniciando con frecuencia Int (2400)...")
    maquina2 = MaquinaTuringOscilador(cinta_prueba_int)
    maquina2.ejecutar()
