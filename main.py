import requests
from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana=None
    __dolar=None
    __pesos=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor Pulgadas a Centímetros')
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolar=StringVar()
        self.__pesos= StringVar()
        self.dolares = ttk.Entry(mainframe, width=7, textvariable=self.__dolar)
        self.dolares.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__pesos).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="dólares").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="pesos").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
    """__dolar=None
    
    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.geometry('290x150')
        self.__ventana.title('Conversor de moneda')
        salir=ttk.Button(self.__ventana, text='Salir',command=self.__ventana.destroy)
        text1 = ttk.Entry(self.__ventana, textvariable=self.__dolar,width=7)
        dolares = ttk.Label(self.__ventana, text="dólares")
        text1.grid(row=1, column=2)
        dolares.grid(row=1, column=3)"""
    def calcular(self):
        
        r=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        datos=r.json()
        index=0
        preciooficial=None
        while index < len(datos) and not preciooficial:
            casa = datos[index]
            if casa['casa']['nombre'] == 'Oficial':
                preciooficial = float(casa['casa']['venta'].replace(',', '.'))
            index += 1
            
        valor=float(self.dolares.get())
        self.__pesos.set(preciooficial*valor)
        
            
    def ejecutar(self):
        self.__ventana.mainloop()
if __name__ == '__main__':
    app=Aplicacion()
    app.ejecutar()
