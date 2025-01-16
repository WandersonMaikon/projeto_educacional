import tkinter as tk
from tkinter import messagebox
from tela_professor import TelaProfessor

class TelaPrincipal:
    def __init__(self, root, login_root, conexao_banco):
        self.root = root
        self.login_root = login_root
        self.conexao_banco = conexao_banco  # Conexão com o MySQL
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

        # Adiciona barra de navegação
        self.criar_menu()

        # Conteúdo da tela principal
        tk.Label(self.root, text="Bem-vindo à Tela Principal!", font=("Arial", 16)).pack(pady=20)

    def criar_menu(self):
        """Cria a barra de navegação superior."""
        menu_bar = tk.Menu(self.root)

        # Cadastrar
        menu_arquivo = tk.Menu(menu_bar, tearoff=0)
        menu_arquivo.add_command(label="Professor", command=self.abrir_tela_cadastro_professor)
        menu_arquivo.add_command(label="Sala", command=self.abrir_arquivo)
        menu_arquivo.add_command(label="Feriado", command=self.abrir_arquivo)
        menu_arquivo.add_command(label="Curso", command=self.abrir_arquivo)
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Sair", command=self.sair)
        menu_bar.add_cascade(label="Cadastrar", menu=menu_arquivo)

        # Menu Ajuda
        menu_ajuda = tk.Menu(menu_bar, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.exibir_sobre)
        menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

        # Configura a barra de menu
        self.root.config(menu=menu_bar)

    def abrir_tela_cadastro_professor(self):
        """Abre a tela de cadastro de professor."""
        TelaProfessor(self.root, self.conexao_banco)

    def abrir_arquivo(self):
        """Ação para abrir um arquivo."""
        messagebox.showinfo("Abrir Arquivo", "Funcionalidade de Abrir Arquivo não implementada ainda.")

    def exibir_sobre(self):
        """Exibe informações sobre o sistema."""
        messagebox.showinfo("Sobre", "Sistema de Navegação - Desenvolvido em Python e Tkinter.")

    def sair(self):
        """Fecha a tela principal e retorna à tela de login."""
        self.root.destroy()
        self.login_root.deiconify()
