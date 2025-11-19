import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("(˶˃ ᵕ ˂˶) .ᐟ.ᐟ","Ten un bonito día ⸜(｡˃ ᵕ ˂ )⸝♡")

ventana = tk.Tk()
ventana.title("Mi primera ventana")

label = tk.Label(ventana, text="'ira pícale aquí pa' q veas lo q pasa")
label.pack(pady=10)

boton = tk.Button(ventana, text="no hagas click aquí", command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()