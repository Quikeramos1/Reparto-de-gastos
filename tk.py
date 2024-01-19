# Este archivo es independiete y ejecuta el programa con interface gráfica
from tkinter import *
import tkinter as tk
from tkinter import ttk

class InterfazTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title("Reparto de gastos")

        self.label1 = ttk.Label(self.master, text="Nombre de la persona 1:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre1 = ttk.Entry(self.master)
        self.entry_nombre1.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_sueldo1 = ttk.Label(self.master, text="Sueldo de la persona 1:")
        self.label_sueldo1.grid(row=1, column=0, padx=10, pady=10)

        self.entry_sueldo1 = ttk.Entry(self.master)
        self.entry_sueldo1.grid(row=1, column=1, padx=10, pady=10)

        self.label2 = ttk.Label(self.master, text="Nombre de la persona 2:")
        self.label2.grid(row=2, column=0, padx=10, pady=10)

        self.entry_nombre2 = ttk.Entry(self.master)
        self.entry_nombre2.grid(row=2, column=1, padx=10, pady=10)

        self.label_sueldo2 = ttk.Label(self.master, text="Sueldo de la persona 2:")
        self.label_sueldo2.grid(row=3, column=0, padx=10, pady=10)

        self.entry_sueldo2 = ttk.Entry(self.master)
        self.entry_sueldo2.grid(row=3, column=1, padx=10, pady=10)

        self.calcular_button = ttk.Button(self.master, text="Calcular", command=self.calcular_resultado, width=20)
        self.calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.textbox = tk.Text(self.master, height=10, width=60)
        self.textbox.grid(row=5, column=0, columnspan=2, pady=10)

        self.ventana_gastos = None  # Variable para almacenar la referencia a la ventana de gastos
        self.splash_root = None  # Variable para almacenar la referencia a la ventana splash

    def log(self, message):
        self.textbox.insert(tk.END, f"{message}\n")
        self.textbox.see(tk.END)  # Desplaza el cuadro de texto hasta la última línea

    def calcular_resultado(self):
        nombre_1 = self.entry_nombre1.get()
        nombre_2 = self.entry_nombre2.get()
        sueldo_1 = self.entry_sueldo1.get()
        sueldo_2 = self.entry_sueldo2.get()

        try:
            tasa_1, tasa_2 = self.calcular_aportacion(sueldo_1, sueldo_2)
            gastos = self.pedir_datos(nombre_1, nombre_2, sueldo_1, sueldo_2, tasa_1, tasa_2)
            self.cantidad_pagar(gastos, nombre_1, nombre_2, tasa_1, tasa_2)
            self.log(f" {nombre_1} aportará un {tasa_1}%")
            self.log(f" {nombre_2} aportará un {tasa_2}%")

        except Exception as e:
            self.log(f"Error: {e}")

    def pedir_datos(self, nombre_1, nombre_2, sueldo_1, sueldo_2, tasa_1, tasa_2):
        gastos = {}
                
        self.ventana_gastos = tk.Toplevel(self.master)
        self.ventana_gastos.title("Introducir Gastos")

        ttk.Label(self.ventana_gastos, text="Concepto del gasto:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.ventana_gastos, text="Importe del gasto:").grid(row=1, column=0, padx=10, pady=10)
        width = int(self.master.winfo_screenwidth() // 4.5)
        height = int(self.master.winfo_screenheight() // 3)
        pwidth = round(self.master.winfo_screenwidth() // 2 - width // 2)
        pheight = round(self.master.winfo_screenheight() // 2 - height // 2)
        self.ventana_gastos.geometry("{}x{}+{}+{}".format(width, height, pwidth, pheight))

        entry_concepto = ttk.Entry(self.ventana_gastos)
        entry_concepto.grid(row=0, column=1, padx=10, pady=10)

        entry_importe = ttk.Entry(self.ventana_gastos)
        entry_importe.grid(row=1, column=1, padx=10, pady=10)

        mensaje_label = ttk.Label(self.ventana_gastos, text="")
        mensaje_label.grid(row=2, column=0, columnspan=2, pady=10)

        def agregar_gasto():
            try:
                concepto = entry_concepto.get()
                importe = float(entry_importe.get())
                gastos[concepto] = importe
                mensaje_label.config(text=f"Gasto añadido: {concepto} - {importe}")
                self.log(f"Gasto añadido: {concepto} - {importe}")

            except ValueError:
                mensaje_label.config(text="Error: El importe debe ser un número")
                self.log("Error: El importe debe ser un número")
                

        def ejecutar_cantidad_pagar():
            self.ventana_gastos.destroy()  # Cierra la ventana de gastos
            resultados_text = self.cantidad_pagar(gastos, nombre_1, nombre_2, tasa_1, tasa_2)
                        
            ventana_resultados = tk.Toplevel(self.master)
            ventana_resultados.title("Resultados")
            
            ttk.Label(ventana_resultados, text=resultados_text).pack()
             # Centrar la ventana en la pantalla
            width = int(ventana_resultados.winfo_screenwidth() // 4.5)
            height = int(ventana_resultados.winfo_screenheight() // 2.5)
            pwidth = round(ventana_resultados.winfo_screenwidth() // 2 - width // 2)
            pheight = round(ventana_resultados.winfo_screenheight() // 2 - height // 2)
            ventana_resultados.geometry("{}x{}+{}+{}".format(width, height, pwidth, pheight))


            def on_closing():
                ventana_resultados.destroy()
                self.splash_root.destroy()
                self.master.destroy()

            ttk.Button(ventana_resultados, text="Salir", command=on_closing).pack()
            
        ttk.Button(self.ventana_gastos, text="Agregar Gasto", command=agregar_gasto).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.ventana_gastos, text="Calcular Pagos", command=ejecutar_cantidad_pagar).grid(row=4, column=0, columnspan=2, pady=10)
    
        return gastos

    def calcular_aportacion(self, sueldo_1, sueldo_2):
        sueldo_1 = float(sueldo_1)
        sueldo_2 = float(sueldo_2)
        total = sueldo_1 + sueldo_2
        tasa_1 = (sueldo_1 / total) * 100
        tasa_2 = (sueldo_2 / total) * 100
        
        return tasa_1, tasa_2
    
    

    def cantidad_pagar(self, gastos, nombre_1, nombre_2, tasa_1, tasa_2):
        resultados_text = ""
        
        total1 = []
        total2 = []
        for clave, valor in gastos.items():
            tasa_valor_1 = (int(valor) * int(tasa_1)) / 100
            tasa_valor_2 = (int(valor) * int(tasa_2)) / 100
            total1.append(float(tasa_valor_1))
            total2.append(float(tasa_valor_2))
            resultados_text += f"{nombre_1}, tiene que pagar de {clave}: {tasa_valor_1}\n"
            resultados_text += f"{nombre_2}, tiene que pagar de {clave}: {tasa_valor_2}\n"
            resultados_text += "\n"  # Agrega un espacio entre cada línea
            
        resultados_text += f"El total acumulado de {nombre_1} es de {sum(total1)}\n"
        resultados_text += f"El total acumulado de {nombre_2} es de {sum(total2)}\n"
        
        return resultados_text 



def mostrar_ventana_splash():
    splash_root = Tk()
    splash_root.geometry("400x400")
    splash_root.overrideredirect(True)
    width = int(splash_root.winfo_screenwidth() // 3)
    height = int(splash_root.winfo_screenheight() // 3)
    pwidth = round(splash_root.winfo_screenwidth() // 2 - width // 2)
    pheight = round(splash_root.winfo_screenheight() // 2 - height // 2)
    splash_root.geometry("{}x{}+{}+{}".format(width, height, pwidth, pheight))
    splash_root.after(3000, mostrar_ventana_principal, splash_root)

    splash_root.mainloop()


def mostrar_ventana_principal(splash_root):
    splash_root.withdraw()
    root = Tk()
    width = int(root.winfo_screenwidth() // 4.5)
    height = int(root.winfo_screenheight() // 2.5)
    pwidth = round(root.winfo_screenwidth() // 2 - width // 2)
    pheight = round(root.winfo_screenheight() // 2 - height // 2)
    root.geometry("{}x{}+{}+{}".format(width, height, pwidth, pheight))
    root.iconbitmap("/Users/quike/Desktop/calcular_aporte_economico/Reparto de gastos/dist/icon.ico")
    app = InterfazTkinter(root)
    app.splash_root = splash_root 
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, splash_root))
    
    root.mainloop()



def on_closing(root, splash_root):
    splash_root.destroy()
    root.destroy()


if __name__ == "__main__":
    mostrar_ventana_splash()
