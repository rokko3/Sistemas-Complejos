from demodulador import desmodulador
import numpy as np

class receptor:
    def __init__(self, cinta):
        self.cinta = cinta
        self.cabezal = 0
        self.estado_actual = "q0_recibiendo_frecuencia"
        self.memoria_frecuencia = ""

    def paso(self):
        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0
            
        simbolo = self.cinta[self.cabezal]
        
        # Evitar error de casting al pasar arrays de numpy a string
        if isinstance(simbolo, np.ndarray):
            simbolo_leido = "ARRAY"
        else:
            simbolo_leido = str(simbolo)
            
        nuevo_estado = self.estado_actual
        
        if self.estado_actual == "q0_recibiendo_frecuencia":
            if simbolo_leido == "f":
                nuevo_estado = "q1_leer_frecuencia"
                
        elif self.estado_actual == "q1_leer_frecuencia":
            if simbolo_leido == " ":
                if self.memoria_frecuencia != "":
                    nuevo_estado = "q2_procesar_datos"
            elif simbolo_leido.isdigit() or simbolo_leido == ".":
                self.memoria_frecuencia += simbolo_leido

        self.estado_actual = nuevo_estado
        self.cabezal += 1 # Siempre avanza en este modo

    def ejecutar(self):
        # 1. Buscar frecuencia
        while self.estado_actual != "q2_procesar_datos":
            self.paso()
            
        # 2. Delegar cinta al demodulador
        demod = desmodulador(self.cinta[self.cabezal:], self.memoria_frecuencia)
        cinta_bits = demod.ejecutar()
        
        # 3. Sobrescribir cinta
        self.cinta[self.cabezal:] = cinta_bits
        
        # 4. Traducir bits a string ASCII
        bits = [str(x) for x in cinta_bits if x in ["0", "1"]]
        cadena_completa = "".join(bits)
        mensaje_final = ""
        for i in range(0, len(cadena_completa), 8):
            byte = cadena_completa[i:i+8]
            if len(byte) == 8:
                mensaje_final += chr(int(byte, 2))
                
        return self.cinta, bits, mensaje_final