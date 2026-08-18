from turing import MaquinaTuringOscilador

class Emisor:
    def __init__(self, mensaje, frecuencia, ruido_nivel=0.1):
        self.mensaje = str(mensaje)
        self.frecuencia = str(frecuencia)
        self.ruido_nivel = ruido_nivel
        self.cinta = []
        self.estado_actual = "q0_escribir_frecuencia"
        self.bits_puros = [] # Solo para graficar en la UI
        
    def paso(self):
        nuevo_estado = self.estado_actual

        if self.estado_actual == "q0_escribir_frecuencia":
            self.cinta.append("f")
            self.cinta.append(" ")
            for caracter in self.frecuencia:
                self.cinta.append(caracter)
            self.cinta.append(" ")
            nuevo_estado = "q1_codificar_mensaje"

        elif self.estado_actual == "q1_codificar_mensaje":
            for letra in self.mensaje:
                bits = format(ord(letra), '08b')
                for bit in bits:
                    self.cinta.append(bit)
                    self.bits_puros.append(bit)
            
            self.cinta.append("_")
            nuevo_estado = "q2_delegar_oscilador"

        elif self.estado_actual == "q2_delegar_oscilador":
            oscilador = MaquinaTuringOscilador(self.cinta, self.ruido_nivel)
            self.cinta = oscilador.ejecutar()
            nuevo_estado = "q_fin"

        self.estado_actual = nuevo_estado

    def ejecutar(self):
        while self.estado_actual != "q_fin":
            self.paso()
        return self.cinta, self.bits_puros