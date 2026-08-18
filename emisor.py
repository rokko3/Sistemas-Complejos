from turing import MaquinaTuringOscilador

class Emisor:
    def __init__(self, mensaje, frecuencia):
        # En lugar de recibir una cinta sucia, el Emisor recibe los datos de alto nivel
        self.mensaje = str(mensaje)
        self.frecuencia = str(frecuencia)
        
        # Inicia con una cinta en blanco
        self.cinta = []
        self.estado_actual = "q0_escribir_frecuencia"
        
    def paso(self):
        """Ejecuta los estados lógicos del Emisor (Capa de Aplicación y Presentación)"""
        nuevo_estado = self.estado_actual

        if self.estado_actual == "q0_escribir_frecuencia":
            # 1. Prepara la cabecera de la cinta con el comando 'f' y la frecuencia
            self.cinta.append("f")
            self.cinta.append(" ")
            
            # Escribe dígito por dígito la frecuencia en la cinta
            for caracter in self.frecuencia:
                self.cinta.append(caracter)
                
            self.cinta.append(" ")
            nuevo_estado = "q1_codificar_mensaje"

        elif self.estado_actual == "q1_codificar_mensaje":
            for letra in self.mensaje:
                bits = format(ord(letra), '08b')
                # Escribe cada bit en la cinta
                for bit in bits:
                    self.cinta.append(bit)
            
            # Añade el marcador de fin de cinta
            self.cinta.append("_")
            nuevo_estado = "q2_delegar_oscilador"

        elif self.estado_actual == "q2_delegar_oscilador":
            # cinta para oscilador
            #print(f"[EMISOR] Cinta preparada con bits: {self.cinta}")
            #print("[EMISOR] Delegando trabajo a la Máquina de Turing del Oscilador\n")
            
            # creando el oscialdor
            oscilador = MaquinaTuringOscilador(self.cinta)
            
            # Ejecutamos el oscilador
            cinta_con_ondas = oscilador.ejecutar()
            
            # Sobrescribimos la cinta con el resultado
            self.cinta = cinta_con_ondas
            nuevo_estado = "q_fin"

        # Actualiza el estado
        self.estado_actual = nuevo_estado

    def ejecutar(self):
        print(f"Mensaje original: '{self.mensaje}'")
        print(f"Frecuencia (fc) : {self.frecuencia}\n")
        
        while self.estado_actual != "q_fin":
            self.paso()
        #print(type(self.cinta[2]))
        return self.cinta


if __name__ == "__main__":
    transmisor = Emisor(mensaje="hola", frecuencia=2.4)
    
    cinta_final_transmitida = transmisor.ejecutar()