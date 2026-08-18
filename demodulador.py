import numpy as np
class desmodulador():
    def __init__(self,cinta,frecuencia):
        self.frecuencia=frecuencia
        self.cinta=cinta
        self.estado_actual="q0_computando_datos"
        self.cabezal=0

    def paso(self):

        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0

        simbolo_leido=(self.cinta[self.cabezal])
        escribir = simbolo_leido
        movimiento = "DERECHA"
        nuevo_estado = self.estado_actual
        if self.estado_actual=="q0_computando_datos":
            onda_sucia=simbolo_leido
            if isinstance(simbolo_leido,np.ndarray):
                onda_sucia=simbolo_leido
                tiempo=np.linespace(0,1,1000)
                onda_local=np.cos(2*np.pi*self.frecuencia*tiempo)
                senal_mezclada=onda_sucia*onda_local
                valor_final=np.sum(senal_mezclada)
                if valor_final > 0:
                    bit_recuperado="1"
                else:
                    bit_recuperado="0"
                escribir=bit_recuperado
            else:
                nuevo_estado="q1_finalizado"
        if self.estado_actual=="q1_finalizado":
            escribir="qf_codificar"

        
        self.cinta[self.cabezal]=escribir
        self.estado_actual=nuevo_estado

        if movimiento=="DERECHA":
            self.cabezal+=1
        elif movimiento=="IZQUIERDA":
            self.cabezal-=1

    def ejecutar(self):
        while self.estado_actual!="qf_codificar":
            self.paso()

        return self.cinta()
