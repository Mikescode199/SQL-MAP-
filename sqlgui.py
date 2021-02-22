import tkinter as tk
import scannermike

class SQLGUI(tk.Frame):
    #SE DECLARAN LAS VARIABLES A USAR
    def __init__(self, __Padre__, *pargs):
        super(SQLGUI, self).__init__(__Padre__, *pargs)

        self._link = tk.StringVar()
        self._site_vulnerable = tk.StringVar()
        self._Dump_database = tk.StringVar()
        self.database_type = tk.StringVar()
        self.database_name = tk.StringVar() 
        self.tables_name = tk.StringVar() 

    def __main__(self):
        #ENTRADA DE N NUMEROS
        label_link_text = tk.Label(self, text="SQL GUI")
        label_link_text.pack() 
        label_link_text.config(font=("Times New Roman", 24))

        link_label = tk.Entry(self, textvariable=self._link) 
        link_label.pack()
        link_label.config(font=("Times New Roman", 14))

        self.Scan = tk.Button(self, text='Scan', fg="red",
                              command= lambda : scannermike._SCANBYMIKE_(str(self._link)))
        self.Scan.pack()
        self.Scan.config(font=("Times New Roman", 24))

        self.Dump = tk.Button(self, text='Dump', fg="red",
                              command= lambda : scannermike._Dump_(self, str(self._link)))
        self.Dump.pack()
        self.Dump.config(font=("Times New Roman", 24))

        self.Database_type = tk.Button(self, text='Database Type', fg="red",
                                       command= lambda : scannermike._get_database_type_(self, str(self._link)))
        self.Database_type.pack()
        self.Database_type.config(font=("Times New Roman", 24))





if __name__ == "__main__":
    root = tk.Tk() #OBJETO DE TKINTER EL CUAL SE LO PASAMOS A NUESTRO OBJETO
    root.geometry("1000x1000") #TAMANO DE VENTANA
    root.title("SQL BY MIKE")
    
    main = SQLGUI(root) #LLAMAMOS A NUESTRO OBJETO Y LE PASAMOS EL PARAMETRO TKINTER
    main.pack(fill="both", expand=False)
    main.__main__()
    root.mainloop()