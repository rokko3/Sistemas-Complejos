import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class simulador(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simulador Transmision")
        self.geometry("1100x750")
        self.minsize(900,600)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=3)
        self.grid_rowconfigure(0,weight=1)

        self._crear_panel_controles()
        self._crear_panel_visualizacion()

    def _crear_panel_controles(self):

        self.panel_izquierdo=ctk.CTkFrame(self,corner_radius=0)

        self.panel_izquierdo.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)


        # transmisor

        self.label_tx=ctk.CTkLabel(self.panel_izquierdo,text="Transmisor",font=ctk.CTkFont(size=20,weight="bold"))
        self.label_tx.pack(pady=(20,10))

        # Entrada de datois

        self.entry_datos=ctk.CTkEntry(self.panel_izquierdo,placeholder_text="Datos a enviar: ")
        self.entry_datos.pack(pady=10,padx=20,fill="x")

        self.opcion_modulacion=ctk.CTkOptionMenu(self.panel_izquierdo,values=["Modulacion BPSK"])
        self.opcion_modulacion.pack(pady=10,padx=20,fill="x")



        # Frecuencia oscilador

        self.label_freq=ctk.CTkLabel(self.panel_izquierdo,text="Frecuencia del oscilador")

        self.label_freq.pack(pady=(10,0))
        self.slider_freq=ctk.CTkSlider(self.panel_izquierdo,from_=1,to=100)
        self.slider_freq.pack(pady=(0,10),padx=20)

        # enviar 
        self.btn_transmitir = ctk.CTkButton(self.panel_izquierdo,text="Modualr y Transmitir")
        self.btn_transmitir.pack(pady=15,padx=20,fill="x")

        self.label_canal=ctk.CTkLabel(self.panel_izquierdo,text="Medio fisico (aire)",font=ctk.CTkFont(size=20,weight="bold"))
        self.label_canal.pack(pady=(30,10))

        # Ruido

        self.label_ruido=ctk.CTkLabel(self.panel_izquierdo,text="Porcentaje de ruido")
        self.label_ruido.pack(pady=(10,0))

        self.slider_ruido=ctk.CTkSlider(self.panel_izquierdo,from_=0,to=10)

        self.slider_ruido.set(0.1)
        self.slider_ruido.pack(pady=(0,10),padx=20,fill="x")

        # receptor

        self.label_rx=ctk.CTkLabel(self.panel_izquierdo,text="Receptor",font=ctk.CTkFont(size=20,weight="bold"))
        self.label_rx.pack(pady=(30,10))

        # recibir

        self.btn_recibir=ctk.CTkButton(self.panel_izquierdo,text="Recibir y demodular",fg_color="#27ae60",hover_color="#2ecc71")
        self.btn_recibir.pack(pady=15,padx=20,fill="x")

    def _crear_panel_visualizacion(self):
        self.panel_derecho=ctk.CTkFrame(self)
        self.panel_derecho.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

        self.panel_derecho.grid_columnconfigure(0,weight=1)
        self.panel_derecho.grid_rowconfigure((0,1,2),weight=1)



        # grafico 1, datos puros

        self.frame_grafico1=ctk.CTkFrame(self.panel_derecho,fg_color="#1e1e1e")

        self.frame_grafico1.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
        self.lbl_g1=ctk.CTkLabel(self.frame_grafico1,text="Grafica 1 (aca va la onda de datos)",font=ctk.CTkFont(slant="italic"))
        self.lbl_g1.place(relx=0.5,rely=0.5,anchor="center")



        # grafica 2

        self.frame_grafico2=ctk.CTkFrame(self.panel_derecho,fg_color="#1e1e1e")
        self.frame_grafico2.grid(row=1,column=0,sticky="nsew",padx=10,pady=10)

        self.lbl_g2=ctk.CTkLabel(self.frame_grafico2,text="Espacio grafica 2 (señal trasmitida modulado + ruido)",font=ctk.CTkFont(slant="italic"))
        self.lbl_g2.place(relx=0.5,rely=0.5,anchor="center")

        # grafica 3
        # 
        self.frame_grafica3=ctk.CTkFrame(self.panel_derecho,fg_color="#1e1e1e")

        self.frame_grafica3.grid(row=2,column=0,sticky="nsew",padx=10,pady=10)
        self.lbl_g3=ctk.CTkLabel(self.frame_grafica3,text="Grafica de señal demodulada en el receptor",font=ctk.CTkFont(slant="italic"))

        self.lbl_g3.place(relx=0.5,rely=0.5,anchor="center")
              
if __name__ == "__main__":
    app = simulador()
    app.mainloop()