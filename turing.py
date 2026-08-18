import numpy as np

class MaquinaTuringOscilador:
    def __init__(self, cinta_inicial, ruido_nivel=0.1):
        self.cinta = list(cinta_inicial)
        self.cabezal = 0
        self.estado_actual = "q0_buscando_f"
        self.memoria_frecuencia = ""
        self.ruido_nivel = ruido_nivel
        
    def paso(self):
        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0

        simbolo = self.cinta[self.cabezal]
        
        # Evitar usar str() en arrays de numpy
        if isinstance(simbolo, np.ndarray):
            simbolo_leido = "ARRAY"
        else:
            simbolo_leido = str(simbolo)
            
        escribir = simbolo
        movimiento = "DERECHA"
        nuevo_estado = self.estado_actual

        if self.estado_actual == "q0_buscando_f":
            if simbolo_leido == "f":
                nuevo_estado = "q1_leer_frecuencia"

        elif self.estado_actual == "q1_leer_frecuencia":
            if simbolo_leido == " ":
                if self.memoria_frecuencia != "":
                    nuevo_estado = "q2_procesar_datos"
            elif simbolo_leido.isdigit() or simbolo_leido == ".":
                self.memoria_frecuencia += simbolo_leido

        elif self.estado_actual == "q2_procesar_datos":
            if simbolo_leido == " ":
                pass 
            elif simbolo_leido in ["0", "1"]:
                frecuencia = float(self.memoria_frecuencia)
                tiempo = np.linspace(0, 1, 1000)
                onda = np.cos(2 * np.pi * frecuencia * tiempo)
                if simbolo_leido == "0":
                    onda = -onda
                ruido = np.random.normal(0, self.ruido_nivel, 1000)
                escribir = onda + ruido
            elif simbolo_leido == "_":
                nuevo_estado = "q_fin"
                movimiento = "CENTRO"

        self.cinta[self.cabezal] = escribir
        self.estado_actual = nuevo_estado
        
        if movimiento == "DERECHA":
            self.cabezal += 1
        elif movimiento == "IZQUIERDA":
            self.cabezal -= 1

    def ejecutar(self):
        while self.estado_actual != "q_fin":
            self.paso()
        return self.cinta
