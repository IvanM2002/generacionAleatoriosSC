import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import generador_uniforme
import generador_normal

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz Gráfica")
        self.geometry("400x350")
        
        # Creamos el panel de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        
        # Creamos los paneles de las pestañas
        self.panel_uniforme = ttk.Frame(self.notebook)
        self.panel_normal = ttk.Frame(self.notebook)
        
        # Agregamos los paneles a las pestañas
        self.notebook.add(self.panel_uniforme, text="Distribución Uniforme")
        self.notebook.add(self.panel_normal, text="Distribución Normal")
        
        # Creamos los widgets necesarios para el panel de distribución uniforme
        self.label_max_intervalo = ttk.Label(self.panel_uniforme, text="Máximo Intervalo:")
        self.entry_max_intervalo = ttk.Entry(self.panel_uniforme)
        self.label_min_intervalo = ttk.Label(self.panel_uniforme, text="Mínimo Intervalo:")
        self.entry_min_intervalo = ttk.Entry(self.panel_uniforme)
        self.label_semilla = ttk.Label(self.panel_uniforme, text="Semilla:")
        self.entry_semilla = ttk.Entry(self.panel_uniforme)
        self.label_total = ttk.Label(self.panel_uniforme, text="Total:")
        self.entry_total = ttk.Entry(self.panel_uniforme)
        self.label_num_intervalos = ttk.Label(self.panel_uniforme, text="Número de Intervalos:")
        self.entry_num_intervalos = ttk.Entry(self.panel_uniforme)
        self.btn_generar_distribucion = ttk.Button(self.panel_uniforme, text="Generar Distribución Uniforme", command=self.generar_distribucion_uniforme)
        self.btn_generar_grafica = ttk.Button(self.panel_uniforme, text="Generar Gráfica", command=self.generar_grafica, state="disabled")
        self.btn_generar_csv = ttk.Button(self.panel_uniforme, text="Generar CSV", command=self.generar_csv, state="disabled")
       # self.progressbar_uniforme = ttk.Progressbar(self.panel_uniforme, orient="horizontal", length=200, mode="indeterminate")
        
        
        # Alineamos los widgets en el panel de distribución uniforme
        self.label_max_intervalo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_max_intervalo.grid(row=0, column=1, padx=5, pady=5)
        self.label_min_intervalo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_min_intervalo.grid(row=1, column=1, padx=5, pady=5)
        self.label_semilla.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_semilla.grid(row=2, column=1, padx=5, pady=5)
        self.label_total.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_total.grid(row=3, column=1, padx=5, pady=5)
        self.label_num_intervalos.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_num_intervalos.grid(row=4, column=1, padx=5, pady=5)
        self.btn_generar_distribucion.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_grafica.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_csv.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
       # self.progressbar_uniforme.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
      #  self.progressbar_uniforme.grid_remove()  # Ocultar la barra de progreso inicialmente
        
        # Creamos los widgets necesarios para el panel de distribución normal
        self.label_semilla_normal = ttk.Label(self.panel_normal, text="Semilla:")
        self.entry_semilla_normal = ttk.Entry(self.panel_normal)
        self.label_total_normal = ttk.Label(self.panel_normal, text="Total:")
        self.entry_total_normal = ttk.Entry(self.panel_normal)
        self.btn_generar_distribucion_normal = ttk.Button(self.panel_normal, text="Generar Distribución Normal", command=self.generar_distribucion_normal)
        self.btn_generar_grafica_normal = ttk.Button(self.panel_normal, text="Generar Gráfica", command=self.generar_grafica_normal, state="disabled")
        self.btn_generar_csv_normal = ttk.Button(self.panel_normal, text="Generar CSV", command=self.generar_csv_normal, state="disabled")
       # self.progressbar_normal = ttk.Progressbar(self.panel_normal, orient="horizontal", length=200, mode="indeterminate")
        
        # Alineamos los widgets en el panel de distribución normal
        self.label_semilla_normal.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_semilla_normal.grid(row=0, column=1, padx=5, pady=5)
        self.label_total_normal.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_total_normal.grid(row=1, column=1, padx=5, pady=5)
        self.btn_generar_distribucion_normal.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_grafica_normal.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_csv_normal.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
      #  self.progressbar_normal.grid(row=3, column=0, columnspan=2, padx=5, pady=5)        
        
        # Inicializamos las barras de progreso
       # self.progressbar_uniforme.stop()
       # self.progressbar_normal.stop()
    
    def validar_campos_uniforme(self):
        if self.entry_max_intervalo.get() == "" or self.entry_min_intervalo.get() == "" or self.entry_total.get() == "" or self.entry_num_intervalos.get() == "":
            messagebox.showinfo("Advertencia", "Por favor, complete todos los campos en el panel de Distribución Uniforme.")
            return False
        return True
    
    def generar_distribucion_uniforme(self):
        if not self.validar_campos_uniforme():
            return
        self.max_intervalo = float(self.entry_max_intervalo.get())
        self.min_intervalo = float(self.entry_min_intervalo.get())
        semilla_texto = self.entry_semilla.get()
        if semilla_texto == "":
            semilla = None
        else:
            semilla = int(semilla_texto)
        total = int(self.entry_total.get())        
        
        # Iniciamos la barra de progreso
        #self.progressbar_uniforme.grid()
        #self.progressbar_uniforme.start()
        
        self.ni = generador_uniforme.generarDistrUniforme(self.max_intervalo, self.min_intervalo, semilla, total)
        
        # Detenemos la barra de progreso
        #self.progressbar_uniforme.stop()
        self.btn_generar_grafica.config(state="normal")  # Habilita el botón de generar gráfica
        self.btn_generar_csv.config(state="normal")  # Habilita el botón de generar CSV
        
    def generar_grafica(self):
        if not self.validar_campos_uniforme():
            return
        num_intervalos_texto = self.entry_num_intervalos.get()
        if num_intervalos_texto == "":
            return  # Si el campo de número de intervalos está vacío, no hagas nada
        num_intervalos = int(num_intervalos_texto)
        generador_uniforme.generar_histograma(num_intervalos,self.min_intervalo,self.max_intervalo)
    
    def generar_csv(self):
        if not self.validar_campos_uniforme():
            return
        generador_uniforme.guardar_en_csv()
    
    def validar_campos_normal(self):
        if self.entry_total_normal.get() == "":
            messagebox.showinfo("Advertencia", "Por favor, complete todos los campos en el panel de Distribución Normal.")
            return False
        return True
    
    def generar_distribucion_normal(self):
        if not self.validar_campos_normal():
            return
        semilla_texto = self.entry_semilla_normal.get()
        if semilla_texto == "":
            semilla = None
        else:
            semilla = int(semilla_texto)
        total = int(self.entry_total_normal.get())
        generador_normal.generarDistrNormal(semilla,total)
        self.btn_generar_grafica_normal.config(state="normal")
        self.btn_generar_csv_normal.config(state="normal")
    
    def generar_grafica_normal(self):
        if not self.validar_campos_normal():
            return
        generador_normal.generar_grafica()
    
    def generar_csv_normal(self):
        if not self.validar_campos_normal():
            return
        generador_normal.guardar_en_csv()
    
if __name__ == "__main__":
    app = InterfazGrafica()
    app.mainloop()
