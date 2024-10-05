
from tkinter import Toplevel, ttk, messagebox
import tkinter as tk
from importador import Importador
from constantes import *

class VentanaUsuarios(Toplevel):
    def __init__(self):
        super().__init__()
        self.config(bg=COLOR_BARRA_IZQ)
        self.geometry("500x300")
        self.title("Administrador de Usuarios")
        btns = ["Agregar", "Actualizar", "Eliminar"]
        treeview = ttk.Treeview(self, columns=("admin","contrasena"))
        treeview.heading("#0", text="Usuario")
        treeview.heading("admin", text="Administrador")
        treeview.heading("contrasena", text="Contraseña")
        treeview.column("admin", width=90)
        treeview.column("contrasena", width=90)

        for usuario, permiso,contrasena in Importador.importar_usuarios():
            treeview.insert("", tk.END, text=usuario, values=[permiso, contrasena])
        
        treeview.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        frame = tk.Frame(self, bg=COLOR_BARRA_IZQ)
        
        btns = [tk.Button(frame,text=x, bg=COLOR_BUTTON, fg="white") for x in btns]
        for btn in btns: btn.pack(pady=10)
        
        btns[0].config(command=lambda : self.__agregar_actualizar_usuario())
        btns[1].config(command=lambda : self.__agregar_actualizar_usuario(
            treeview.item(treeview.focus())["text"],
            treeview.item(treeview.focus())["values"][0],
            treeview.item(treeview.focus())["values"][1]
        ))
        btns[-1].config(command=lambda: self.__eliminar_usuario(treeview))
        
        
        frame.pack(side="right", fill="y", ipadx=5)
    
    def __agregar_actualizar_usuario(self, nombre = "", admin=False, Contrasena = ""):
        var_admin = tk.BooleanVar()
        var_admin.set(admin)
        ventana = Toplevel(self, bg=COLOR_BARRA_IZQ, padx=20,pady=20)
        tk.Label(ventana, text="Nombre:", bg=COLOR_BARRA_IZQ, fg="white").pack()
        _usuario = tk.Entry(ventana)
        _usuario.insert(0,nombre)
        _usuario.pack()
        tk.Label(ventana, text="Contraseña:", bg=COLOR_BARRA_IZQ, fg="white").pack()
        _contrasena = tk.Entry(ventana, show="*")
        _contrasena.insert(0, Contrasena)
        _contrasena.pack()
        tk.Label(ventana, text="Administrador:", bg=COLOR_BARRA_IZQ, fg="white").pack()
        tk.Radiobutton(ventana, text="Si", value=True,
                        variable=var_admin, bg=COLOR_BARRA_IZQ, fg="white",
                selectcolor=COLOR_BARRA_IZQ, activebackground=COLOR_BARRA_IZQ, activeforeground="white", ).pack()
        tk.Radiobutton(ventana, text="No", value=False,
                        variable=var_admin, bg=COLOR_BARRA_IZQ, fg="white",
                selectcolor=COLOR_BARRA_IZQ, activebackground=COLOR_BARRA_IZQ, activeforeground="white",).pack()
        tk.Button(ventana, text="Cancelar").pack(side="left")
        tk.Button(ventana, text="Agregar" if not nombre else "Actualizar").pack(side="right")
    
    def __eliminar_usuario(self,treeview):
        id = treeview.focus()
        usuario = treeview.item(id)
        for user, permiso, contrasena in  Importador.importar_usuarios():
            if permiso == "True" and user != usuario["text"]:
                if messagebox.askokcancel("Eliminar", f"Decea eliminar al usuario {usuario['text']}", icon="warning"):
                    Importador.Eliminar_usuario(usuario["text"])
                    treeview.delete(id)
                    return None
                else: return None
        messagebox.showinfo("Cuidado", "Es el unico administrador no se puede eliminar")

if __name__ == "__main__":
    ventana = tk.Tk()
    sub_ventana = VentanaUsuarios()
    ventana.mainloop()