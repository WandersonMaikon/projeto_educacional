import tkinter as tk
from tkinter import ttk, messagebox

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cursos")

        # Dimensões da janela
        width = 600
        height = 400

        # Calculando a posição central
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Definindo o tamanho e posição da janela
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Rótulo
        self.label = tk.Label(self.root, text="Bem-vindo ao Sistema de Cursos", font=("Arial", 14))
        self.label.pack(pady=20)

        # Botão para listar cursos
        self.listar_cursos_btn = tk.Button(self.root, text="Listar Cursos", command=self.listar_cursos)
        self.listar_cursos_btn.pack(pady=10)

        # Tabela para exibir dados
        self.tree = ttk.Treeview(self.root, columns=("Curso", "Horas"), show="headings")
        self.tree.heading("Curso", text="Curso")
        self.tree.heading("Horas", text="Horas")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def listar_cursos(self):
        """Exemplo de como exibir informações na interface"""
        # Limpa os dados antigos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Exemplo de cursos (isso deve vir do seu código real)
        cursos = [
            {"nome": "Técnico em Informática", "horas": 40},
            {"nome": "Técnico em Redes", "horas": 30},
        ]

        for curso in cursos:
            self.tree.insert("", tk.END, values=(curso["nome"], curso["horas"]))
        messagebox.showinfo("Informação", "Cursos listados com sucesso!")
