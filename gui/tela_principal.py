import tkinter as tk

class TelaPrincipal:
    def __init__(self, root, login_root):
        self.root = root
        self.login_root = login_root
        self.root.title("Tela Principal")
        self.root.geometry("600x400")

        # Centralizar a nova janela
        width = 600
        height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Conteúdo da tela principal
        tk.Label(self.root, text="Bem-vindo à Tela Principal!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.root, text="Sair", font=("Arial", 14), command=self.sair).pack(pady=20)

    def sair(self):
        self.root.destroy()  # Fecha a tela principal
        self.login_root.deiconify()  # Traz de volta a janela de login
