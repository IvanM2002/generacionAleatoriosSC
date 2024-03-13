import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import generador_uniforme
import generador_normal
import congruenciaLineal as cl
import congruenciaMulti as cm
import cuadradosMedios as med


class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz Gráfica")
        self.geometry("500x350")

        # Creamos el panel de pestañas
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Creamos los paneles de las pestañas
        self.panel_uniforme = ttk.Frame(self.notebook)
        self.panel_normal = ttk.Frame(self.notebook)
        self.panel_congruenciaLineal = ttk.Frame(self.notebook)
        self.panel_congruenciaMulti = ttk.Frame(self.notebook)
        self.panel_cuadradosMedios = ttk.Frame(self.notebook)

        # Agregamos los paneles a las pestañas
        self.notebook.add(self.panel_uniforme, text="Distribución Uniforme")
        self.notebook.add(self.panel_normal, text="Distribución Normal")
        self.notebook.add(self.panel_congruenciaLineal, text="Congruencia Lineal")
        self.notebook.add(self.panel_congruenciaMulti, text="Congruencia Multiplicativa")
        self.notebook.add(self.panel_cuadradosMedios, text="Cuadrados Medios")

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

        # funcion para validar numeros
        def validate_int(value_if_allowed):
            if value_if_allowed.isdigit() or value_if_allowed == "":
                return True
            else:
                messagebox.showinfo("Error", "Solo se permiten números enteros.")
                return False

        # Registramos la función de validación
        validate_int_func = self.register(validate_int)

        # Creamos los widgets necesarios para congruencia lineal
        self.label_semilla_congLi = ttk.Label(self.panel_congruenciaLineal, text="Semilla:")
        self.entry_semilla_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_max_intervalo_congLi = ttk.Label(self.panel_congruenciaLineal, text="Max:")
        self.entry_max_intervalo_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_min_intervalo_congLi = ttk.Label(self.panel_congruenciaLineal, text="Min: ")
        self.entry_min_intervalo_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_k_congLi = ttk.Label(self.panel_congruenciaLineal, text="Pendiente (k): ")
        self.entry_k_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_c_congLi = ttk.Label(self.panel_congruenciaLineal, text="Intercepto (c): ")
        self.entry_c_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_g_congLi = ttk.Label(self.panel_congruenciaLineal, text="Campo numerico (g): ")
        self.entry_g_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_total_congLi = ttk.Label(self.panel_congruenciaLineal, text="Total ")
        self.entry_total_congLi = ttk.Entry(self.panel_congruenciaLineal, validate="key", validatecommand=(validate_int_func, "%P"))
        self.btn_generar_congLi = ttk.Button(self.panel_congruenciaLineal, text="Generar Congruencia Lineal", command=self.generar_congruencia_lineal)
        self.btn_generar_grafica_congLi = ttk.Button(self.panel_congruenciaLineal, text="Generar Gráfica", command=self.generar_grafica_congLi, state="disabled")
        self.btn_generar_csv_congLi = ttk.Button(self.panel_congruenciaLineal, text="Generar CSV", command=self.generar_csv_congLi, state="disabled")

        # Alineamos los widgets en el panel de congruencia lineal
        self.label_semilla_congLi.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_semilla_congLi.grid(row=0, column=1, padx=5, pady=5)
        self.label_max_intervalo_congLi.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_max_intervalo_congLi.grid(row=1, column=1, padx=5, pady=5)
        self.label_min_intervalo_congLi.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_min_intervalo_congLi.grid(row=2, column=1, padx=5, pady=5)
        self.label_k_congLi.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_k_congLi.grid(row=3, column=1, padx=5, pady=5)
        self.label_c_congLi.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_c_congLi.grid(row=4, column=1, padx=5, pady=5)
        self.label_g_congLi.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_g_congLi.grid(row=5, column=1, padx=5, pady=5)
        self.label_total_congLi.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.entry_total_congLi.grid(row=6, column=1, padx=5, pady=5)
        self.btn_generar_congLi.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_grafica_congLi.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_csv_congLi.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        # Creamos los widgets necesarios para congruencia multiplicativa
        self.label_semilla_congMu = ttk.Label(self.panel_congruenciaMulti, text="Semilla:")
        self.entry_semilla_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_max_intervalo_congMu = ttk.Label(self.panel_congruenciaMulti, text="Max:")
        self.entry_max_intervalo_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_min_intervalo_congMu = ttk.Label(self.panel_congruenciaMulti, text="Min: ")
        self.entry_min_intervalo_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_k_congMu = ttk.Label(self.panel_congruenciaMulti, text="Pendiente (k): ")
        self.entry_k_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_g_congMu = ttk.Label(self.panel_congruenciaMulti, text="Campo numerico (g): ")
        self.entry_g_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_total_congMu = ttk.Label(self.panel_congruenciaMulti, text="Total ")
        self.entry_total_congMu = ttk.Entry(self.panel_congruenciaMulti, validate="key", validatecommand=(validate_int_func, "%P"))
        self.btn_generar_congMu = ttk.Button(self.panel_congruenciaMulti, text="Generar Congruencia Multiplicativa", command=self.generar_congruencia_multi)
        self.btn_generar_grafica_congMu = ttk.Button(self.panel_congruenciaMulti, text="Generar Gráfica", command=self.generar_grafica_congMu, state="disabled")
        self.btn_generar_csv_congMu = ttk.Button(self.panel_congruenciaMulti, text="Generar CSV", command=self.generar_csv_congMu, state="disabled")

        # Alineamos los widgets en el panel de congruencia multiplicativa
        self.label_semilla_congMu.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_semilla_congMu.grid(row=0, column=1, padx=5, pady=5)
        self.label_max_intervalo_congMu.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_max_intervalo_congMu.grid(row=1, column=1, padx=5, pady=5)
        self.label_min_intervalo_congMu.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_min_intervalo_congMu.grid(row=2, column=1, padx=5, pady=5)
        self.label_k_congMu.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_k_congMu.grid(row=3, column=1, padx=5, pady=5)
        self.label_g_congMu.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_g_congMu.grid(row=4, column=1, padx=5, pady=5)
        self.label_total_congMu.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.entry_total_congMu.grid(row=5, column=1, padx=5, pady=5)
        self.btn_generar_congMu.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_grafica_congMu.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_csv_congMu.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        # Creamos los widgets necesarios para cuadrados medios
        self.label_semilla_cuaMed = ttk.Label(self.panel_cuadradosMedios, text="Semilla:")
        self.entry_semilla_cuaMed = ttk.Entry(self.panel_cuadradosMedios, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_max_intervalo_cuaMed = ttk.Label(self.panel_cuadradosMedios, text="Max:")
        self.entry_max_intervalo_cuaMed = ttk.Entry(self.panel_cuadradosMedios, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_min_intervalo_cuaMed = ttk.Label(self.panel_cuadradosMedios, text="Min: ")
        self.entry_min_intervalo_cuaMed = ttk.Entry(self.panel_cuadradosMedios, validate="key", validatecommand=(validate_int_func, "%P"))
        self.label_total_cuaMed = ttk.Label(self.panel_cuadradosMedios, text="Total ")
        self.entry_total_cuaMed = ttk.Entry(self.panel_cuadradosMedios, validate="key", validatecommand=(validate_int_func, "%P"))
        self.btn_generar_cuaMed = ttk.Button(self.panel_cuadradosMedios, text="Generar Cuadrados medios", command=self.generar_congruencia_cuaMed)
        self.btn_generar_grafica_cuaMed = ttk.Button(self.panel_cuadradosMedios, text="Generar Gráfica", command=self.generar_grafica_cuaMed, state="disabled")
        self.btn_generar_csv_cuaMed = ttk.Button(self.panel_cuadradosMedios, text="Generar CSV", command=self.generar_csv_cuaMed, state="disabled")

        # Alineamos los widgets en el panel de cuadrados medios
        self.label_semilla_cuaMed.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_semilla_cuaMed.grid(row=0, column=1, padx=5, pady=5)
        self.label_max_intervalo_cuaMed.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_max_intervalo_cuaMed.grid(row=1, column=1, padx=5, pady=5)
        self.label_min_intervalo_cuaMed.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_min_intervalo_cuaMed.grid(row=2, column=1, padx=5, pady=5)
        self.label_total_cuaMed.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_total_cuaMed.grid(row=3, column=1, padx=5, pady=5)
        self.btn_generar_cuaMed.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_grafica_cuaMed.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        self.btn_generar_csv_cuaMed.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    #  self.progressbar_normal.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    # Inicializamos las barras de progreso
    # self.progressbar_uniforme.stop()
    # self.progressbar_normal.stop()

    def validar_campos_uniforme(self):
        if self.entry_max_intervalo.get() == "" or self.entry_min_intervalo.get() == "" or self.entry_total.get() == "" or self.entry_num_intervalos.get() == "":
            messagebox.showinfo("Advertencia",
                                "Por favor, complete todos los campos en el panel de Distribución Uniforme.")
            return False
        return True

    def validar_campos_congLi(self):
        if self.entry_semilla_congLi.get() != "" or self.entry_k_congLi.get() != "" or self.entry_c_congLi.get() != "" or self.entry_g_congLi.get() != "" or self.entry_total_congLi.get() != "":
            if self.entry_max_intervalo_congLi.get() == "" and self.entry_min_intervalo_congLi.get() == "" :
                return True
            elif self.entry_max_intervalo_congLi.get() != "" and self.entry_min_intervalo_congLi.get() != "":
                return True
            else:
                messagebox.showinfo("Advertencia","Por favor, complete los rangos")
                return False
            return True
        messagebox.showinfo("Advertencia","Por favor, complete todos los campos en el panel de Congruencia Lineal.")
        return False

    def validar_campos_congMu(self):
        if self.entry_semilla_congMu.get() != "" or self.entry_k_congMu.get() != "" or self.entry_g_congMu.get() != "" or self.entry_total_congMu.get() != "":
            if self.entry_max_intervalo_congMu.get() == "" and self.entry_min_intervalo_congMu.get() == "" :
                return True
            elif self.entry_max_intervalo_congMu.get() != "" and self.entry_min_intervalo_congMu.get() != "":
                return True
            else:
                messagebox.showinfo("Advertencia","Por favor, complete los rangos")
                return False
            return True
        messagebox.showinfo("Advertencia","Por favor, complete todos los campos en el panel de Congruencia Multiplicativa.")
        return False

    def validar_campos_cuaMed(self):
        if self.entry_semilla_cuaMed.get()  != "" or self.entry_total_cuaMed.get() != "":
            if self.entry_max_intervalo_cuaMed.get() == "" and self.entry_min_intervalo_cuaMed.get() == "" :
                return True
            elif self.entry_max_intervalo_cuaMed.get() != "" and self.entry_min_intervalo_cuaMed.get() != "":
                return True
            else:
                messagebox.showinfo("Advertencia","Por favor, complete los rangos")
                return False
            return True
        messagebox.showinfo("Advertencia","Por favor, complete todos los campos en el panel de Cuadrados medios.")
        return False

    def generar_congruencia_lineal(self):
        if not self.validar_campos_congLi():
            return

        semilla_congLi =  int(self.entry_semilla_congLi.get())
        k_congLi = int(self.entry_k_congLi.get())
        c_congLi = int(self.entry_c_congLi.get())
        g_congLi = int(self.entry_g_congLi.get())
        total_congLi = int(self.entry_total_congLi.get())
        congruencia_lineal= []
        if self.entry_max_intervalo_congLi.get() != "" and self.entry_max_intervalo_congLi.get() != "":
            max_congLi = int(self.entry_max_intervalo_congLi.get())
            min_congLi = int(self.entry_min_intervalo_congLi.get())
            congruencia_lineal = cl.congruencia_lineal_range(semilla_congLi, k_congLi, c_congLi, g_congLi, total_congLi,min_congLi,max_congLi)
        else:
            congruencia_lineal = cl.congruencia_lineal(semilla_congLi, k_congLi, c_congLi, g_congLi, total_congLi)

        self.btn_generar_grafica_congLi.config(state="normal")  # Habilita el botón de generar gráfica
        self.btn_generar_csv_congLi.config(state="normal")  # Habilita el botón de generar CSV

    def generar_congruencia_multi(self):
        if not self.validar_campos_congMu():
            return

        semilla_congMu = int(self.entry_semilla_congMu.get())
        k_congMu = int(self.entry_k_congMu.get())
        g_congMu = int(self.entry_g_congMu.get())
        total_congMu = int(self.entry_total_congMu.get())
        congruencia_multi = []
        if self.entry_max_intervalo_congMu.get() != "" and self.entry_max_intervalo_congMu.get() != "":
            max_congMu = int(self.entry_max_intervalo_congMu.get())
            min_congMu = int(self.entry_min_intervalo_congMu.get())
            congruencia_multi = cm.congruencia_multiplicativo_range(semilla_congMu, k_congMu, g_congMu, total_congMu, min_congMu, max_congMu)
        else:
            congruencia_multi = cm.congruencia_multiplicativo(semilla_congMu, k_congMu, g_congMu, total_congMu)

        self.btn_generar_grafica_congMu.config(state="normal")  # Habilita el botón de generar gráfica
        self.btn_generar_csv_congMu.config(state="normal")  # Habilita el botón de generar CSV

    def generar_congruencia_cuaMed(self):
        if not self.validar_campos_cuaMed:
            return

        semilla_cuaMed = int(self.entry_semilla_cuaMed.get())
        total_cuaMed = int(self.entry_total_cuaMed.get())
        cuadrados_medios = []
        if self.entry_max_intervalo_cuaMed.get() != "" and self.entry_max_intervalo_cuaMed.get() != "":
            max_cuaMed = int(self.entry_max_intervalo_cuaMed.get())
            min_cuaMed = int(self.entry_min_intervalo_cuaMed.get())
            cuadrados_medios = med.cuadrados_medios_range(semilla_cuaMed, min_cuaMed, max_cuaMed, total_cuaMed)
        else:
            cuadrados_medios = med.cuadrados_medios(semilla_cuaMed, total_cuaMed)

        self.btn_generar_grafica_cuaMed.config(state="normal")  # Habilita el botón de generar gráfica
        self.btn_generar_csv_cuaMed.config(state="normal")  # Habilita el botón de generar CSV

    def generar_grafica_congLi(self):
        if not self.validar_campos_congLi:
            return
        cl.generar_grafica()

    def generar_grafica_cuaMed(self):
        if not self.validar_campos_cuaMed:
            return
        med.generar_grafica()
    def generar_grafica_congMu(self):
        if not self.validar_campos_congMu:
            return
        cm.generar_grafica()
    def generar_csv_congLi(self):
        if not self.validar_campos_congLi:
            return
        cl.guardar_en_csv()

    def generar_csv_congMu(self):
        if not self.validar_campos_congMu:
            return
        cm.guardar_en_csv()

    def generar_csv_cuaMed(self):
        if not self.validar_campos_cuaMed:
            return
        med.guardar_en_csv()

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
        # self.progressbar_uniforme.grid()
        # self.progressbar_uniforme.start()

        self.ni = generador_uniforme.generarDistrUniforme(self.max_intervalo, self.min_intervalo, semilla, total)

        # Detenemos la barra de progreso
        # self.progressbar_uniforme.stop()
        self.btn_generar_grafica.config(state="normal")  # Habilita el botón de generar gráfica
        self.btn_generar_csv.config(state="normal")  # Habilita el botón de generar CSV

    def generar_grafica(self):
        if not self.validar_campos_uniforme():
            return
        num_intervalos_texto = self.entry_num_intervalos.get()
        if num_intervalos_texto == "":
            return  # Si el campo de número de intervalos está vacío, no hagas nada
        num_intervalos = int(num_intervalos_texto)
        generador_uniforme.generar_histograma(num_intervalos, self.min_intervalo, self.max_intervalo)

    def generar_csv(self):
        if not self.validar_campos_uniforme():
            return
        generador_uniforme.guardar_en_csv()

    def validar_campos_normal(self):
        if self.entry_total_normal.get() == "":
            messagebox.showinfo("Advertencia",
                                "Por favor, complete todos los campos en el panel de Distribución Normal.")
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
        generador_normal.generarDistrNormal(semilla, total)
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
