"""Editor de Texto versión 1.0
Editor de texto básico con Tkinter: abrir, guardar, limpiar y salir."""

import tkinter as tk
from tkinter import filedialog as fd

class EditorTextoBasico:

    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Editor de Texto 1.0")
        self.master.geometry("700x500")

        self.crear_menu()
        self.text_area = tk.Text(self.master, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.master.mainloop()

    def crear_menu(self):
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        edicion_menu = tk.Menu(self.menu_bar, tearoff=0)
        edicion_menu.add_command(label="Limpiar", command=self.limpiar_texto)
        self.menu_bar.add_cascade(label="Edición", menu=edicion_menu)

        ayuda_menu = tk.Menu(self.menu_bar, tearoff=0)
        ayuda_menu.add_command(label="Acerca de", command=self.mostrar_acerca_de)
        self.menu_bar.add_cascade(label="Ayuda", menu=ayuda_menu)

    def abrir_archivo(self):
        archivo = fd.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, contenido)

    def guardar_archivo(self):
        archivo = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo:
            with open(archivo, "w", encoding="utf-8") as f:
                contenido = self.text_area.get(1.0, tk.END)
                f.write(contenido)

    def limpiar_texto(self):
        self.text_area.delete(1.0, tk.END)

    def mostrar_acerca_de(self):
        acerca_de = tk.Toplevel(self.master)
        acerca_de.title("Acerca de")
        acerca_de.geometry("300x150")
        etiqueta = tk.Label(acerca_de, text="Editor de Texto 1.0\nDesarrollado con Tkinter", font=("Arial", 13))
        etiqueta.pack(pady=30)
        boton_cerrar = tk.Button(acerca_de, text="Cerrar", command=acerca_de.destroy)
        boton_cerrar.pack(pady=10)

if __name__ == "__main__":
    EditorTextoBasico()