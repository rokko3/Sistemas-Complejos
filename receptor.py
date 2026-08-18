from demodulador import desmodulador
from numpy import ndarray
class receptor():

    def __init__(self,cinta):
        self.cinta=cinta
        self.cabezal=0
        self.estado_actual="q0_recibiendo_frecuencia"
        self.memoria_frecuencia=""
        self.memoria_bits=""


    def paso(self):
        if self.cabezal >= len(self.cinta):
            self.cinta.append("_")
        elif self.cabezal < 0:
            self.cinta.insert(0, "_")
            self.cabezal = 0
            
        simbolo_leido=str(self.cinta[self.cabezal])
        escribir = simbolo_leido
        movimiento = "DERECHA"
        nuevo_estado = self.estado_actual
        
        if self.estado_actual=="q0_recibiendo_frecuencia":
            if simbolo_leido=="f":
                nuevo_estado="q1_leer_frecuencia"
                
        elif self.estado_actual == "q1_leer_frecuencia":
            if simbolo_leido == " ":
                # Si encuentra un espacio, verifica si ya leyó números antes
                if self.memoria_frecuencia != "":
                    nuevo_estado = "q2_procesar_datos"
            elif simbolo_leido.isdigit() or simbolo_leido == ".":
            # Si lee un número (int) o un punto (float), lo acumula en memoria
                self.memoria_frecuencia += simbolo_leido
        if isinstance(simbolo_leido,ndarray):
            self.estado_actual="q3_desmodulando"
            desmodulador1=desmodulador(self.cadena[self.cabezal::])
            nueva_cinta=desmodulador1.ejecutar()
            self.cinta=nueva_cinta
            


        if simbolo_leido=="qf_codificar":
            pass
        self.cinta[self.cabezal] = escribir
        self.estado_actual=nuevo_estado

        if movimiento == "DERECHA":
            self.cabezal += 1
        elif movimiento == "IZQUIERDA":
            self.cabezal -= 1
        
    def ejecutar(self):
    
        
        # El bucle se detiene cuando llega al estado q2
        while self.estado_actual != "q2_procesar_datos":
            self.paso()
            
        
        print(self.cinta)
        return self.memoria_frecuencia

if __name__ == "__main__":
    # Simulamos la cinta que nos enviaría el Emisor/Oscilador
    cinta_prueba = ['f', ' ', '2', '.', '4', ' ', '-cos(2.4t)', '+cos(2.4t)', '_']
    
    mi_receptor = receptor(cinta_prueba)
    mi_receptor.ejecutar()