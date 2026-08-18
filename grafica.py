import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from emisor import Emisor
from receptor import receptor

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Simulador(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Simulador Transmisión")
        self.geometry("1400x850")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.cinta_en_el_aire = None

        self._crear_panel_controles()
        self._crear_panel_visualizacion()

    def _crear_panel_controles(self):
        self.panel_izquierdo = ctk.CTkFrame(self, corner_radius=0)
        self.panel_izquierdo.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Transmisor
        ctk.CTkLabel(self.panel_izquierdo, text="Transmisor", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))
        self.entry_datos = ctk.CTkEntry(self.panel_izquierdo, placeholder_text="Texto a enviar (ej: hola)")
        self.entry_datos.pack(pady=10, padx=20, fill="x")

        # Frecuencia
        self.lbl_freq_text = ctk.CTkLabel(self.panel_izquierdo, text="Frecuencia Portadora: 5.0 Hz")
        self.lbl_freq_text.pack(pady=(10, 0))
        self.slider_freq = ctk.CTkSlider(self.panel_izquierdo, from_=1, to=20, command=self.actualizar_labels)
        self.slider_freq.set(5)
        self.slider_freq.pack(pady=(0, 10), padx=20, fill="x")

        # Ruido
        self.lbl_ruido_text = ctk.CTkLabel(self.panel_izquierdo, text="Nivel de Ruido: 0.50")
        self.lbl_ruido_text.pack(pady=(10, 0))
        self.slider_ruido = ctk.CTkSlider(self.panel_izquierdo, from_=0, to=3, command=self.actualizar_labels)
        self.slider_ruido.set(0.5)
        self.slider_ruido.pack(pady=(0, 10), padx=20, fill="x")

        self.btn_transmitir = ctk.CTkButton(self.panel_izquierdo, text="Modular y Transmitir", command=self.transmitir)
        self.btn_transmitir.pack(pady=15, padx=20, fill="x")

        # Receptor
        ctk.CTkLabel(self.panel_izquierdo, text="Receptor", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(30, 10))
        self.btn_recibir = ctk.CTkButton(self.panel_izquierdo, text="Recibir y Demodular", fg_color="#27ae60", hover_color="#2ecc71", command=self.recibir)
        self.btn_recibir.pack(pady=15, padx=20, fill="x")
        
        self.lbl_mensaje_recibido = ctk.CTkLabel(self.panel_izquierdo, text="", font=ctk.CTkFont(size=22, weight="bold"), text_color="green")
        self.lbl_mensaje_recibido.pack(pady=20)

    def _crear_panel_visualizacion(self):
        self.panel_derecho = ctk.CTkFrame(self)
        self.panel_derecho.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.panel_derecho.grid_columnconfigure(0, weight=1)
        self.panel_derecho.grid_rowconfigure((0, 1, 2), weight=1)

        # Matplotlib integration
        self.fig1, self.ax1 = plt.subplots(figsize=(8, 2), facecolor='#2b2b2b')
        self.ax1.set_facecolor('#1e1e1e')
        self.ax1.tick_params(colors='white')
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.panel_derecho)
        self.canvas1.get_tk_widget().grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.fig2, self.ax2 = plt.subplots(figsize=(8, 2), facecolor='#2b2b2b')
        self.ax2.set_facecolor('#1e1e1e')
        self.ax2.tick_params(colors='white')
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.panel_derecho)
        self.canvas2.get_tk_widget().grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.fig3, self.ax3 = plt.subplots(figsize=(8, 2), facecolor='#2b2b2b')
        self.ax3.set_facecolor('#1e1e1e')
        self.ax3.tick_params(colors='white')
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.panel_derecho)
        self.canvas3.get_tk_widget().grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        # Draw empty placeholders
        for ax, title in [(self.ax1, "Señal Digital (Banda Base)"), (self.ax2, "Onda Transmitida (RF + Ruido)"), (self.ax3, "Señal Digital Recuperada")]:
            ax.set_title(title, color='white')
            ax.set_xticks([])
            ax.set_yticks([])
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()

    def actualizar_labels(self, _=None):
        freq = round(self.slider_freq.get(), 1)
        ruido = round(self.slider_ruido.get(), 2)
        self.lbl_freq_text.configure(text=f"Frecuencia Portadora: {freq} Hz")
        self.lbl_ruido_text.configure(text=f"Nivel de Ruido: {ruido}")

    def transmitir(self):
        mensaje = self.entry_datos.get()
        if not mensaje: return
        frecuencia = self.slider_freq.get()
        ruido = self.slider_ruido.get()

        # Usar la máquina de Turing Emisora
        emisor = Emisor(mensaje, frecuencia, ruido_nivel=ruido)
        self.cinta_en_el_aire, bits_puros = emisor.ejecutar()

        # Graficar Gráfica 1 (Bits de entrada)
        self.ax1.clear()
        onda_digital = []
        for b in bits_puros:
            onda_digital.extend([int(b)] * 100) # Cuadrar la onda para hacerla visible
        self.ax1.plot(onda_digital, color='cyan')
        self.ax1.set_title(f"Bits Transmitidos ({len(bits_puros)} bits)", color='white')
        self.ax1.set_ylim(-0.5, 1.5)
        self.canvas1.draw()

        # Graficar Gráfica 2 (Onda de numpy viajando por el aire)
        self.ax2.clear()
        onda_rf = []
        for celda in self.cinta_en_el_aire:
            if isinstance(celda, np.ndarray):
                onda_rf.extend(celda)
        # Mostrar solo los primeros caracteres (hasta 3000 puntos) para que no seature la RAM o se vea todo borroso
        self.ax2.plot(onda_rf[:8000], color='yellow', linewidth=0.5) 
        self.ax2.set_title("Onda de Radiofrecuencia volando (Física real simulada)", color='white')
        self.canvas2.draw()
        
        self.lbl_mensaje_recibido.configure(text=" Señal enviada", text_color="yellow")

    def recibir(self):
        if not self.cinta_en_el_aire: return
        
        # Pasar la cinta sucia al receptor
        rec = receptor(self.cinta_en_el_aire)
        cinta_final, bits_recuperados, mensaje_texto = rec.ejecutar()

        # Graficar Gráfica 3 (Bits recuperados por el filtro adaptado)
        self.ax3.clear()
        onda_recuperada = []
        for b in bits_recuperados:
            onda_recuperada.extend([int(b)] * 100)
        self.ax3.plot(onda_recuperada, color='lime')
        self.ax3.set_title(f"Bits Demodulados exitosamente", color='white')
        self.ax3.set_ylim(-0.5, 1.5)
        self.canvas3.draw()

        self.lbl_mensaje_recibido.configure(text=f"Recibido: '{mensaje_texto}'", text_color="lime")

if __name__ == "__main__":
    app = Simulador()
    app.mainloop()