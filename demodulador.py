import numpy as np

class desmodulador:
    def __init__(self, cinta, frecuencia):
        self.frecuencia = float(frecuencia)
        self.cinta = cinta
        self.estado_actual = "q0_computando_datos"
        self.cabezal = 0

    def paso(self):
        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0

        simbolo = self.cinta[self.cabezal]
        escribir = simbolo
        movimiento = "DERECHA"
        nuevo_estado = self.estado_actual

        if self.estado_actual == "q0_computando_datos":
            if isinstance(simbolo, np.ndarray):
                # Demodulacion física usando la frecuencia extraída
                tiempo = np.linspace(0, 1, 1000)
                onda_local = np.cos(2 * np.pi * self.frecuencia * tiempo)
                senal_mezclada = simbolo * onda_local
                valor_final = np.sum(senal_mezclada)
                
                if valor_final > 0:
                    escribir = "1"
                else:
                    escribir = "0"
            elif isinstance(simbolo, str) and simbolo == "_":
                nuevo_estado = "q1_finalizado"
                movimiento = "CENTRO"

        self.cinta[self.cabezal] = escribir
        self.estado_actual = nuevo_estado

        if movimiento == "DERECHA":
            self.cabezal += 1
        elif movimiento == "IZQUIERDA":
            self.cabezal -= 1

    def ejecutar(self):
        while self.estado_actual != "q1_finalizado":
            self.paso()
        return self.cinta
