import tkinter as tk
from dados.database import conectar


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")

        # Centralizar a janela
        self.width = 300
        self.height = 200
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.x = (self.screen_width - self.width) // 2
        self.y = (self.screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        # Testar conexão ao abrir
        if not self.testar_conexao():
            self.exibir_mensagem("Erro ao conectar ao banco de dados.")

        # Elementos da interface
        tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Nome de Usuário").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Senha").pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        self.mensagem_label = tk.Label(root, text="", fg="red")
        self.mensagem_label.pack(pady=5)

        tk.Button(root, text="Login", command=self.fazer_login).pack(pady=10)

    def testar_conexao(self):
        try:
            conexao = conectar()
            conexao.close()
            return True
        except Exception:
            return False

    def fazer_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)

            # Consulta ao banco de dados
            cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
            usuario = cursor.fetchone()

            if usuario:
                self.exibir_mensagem(f"Bem-vindo, {username}!", "green")
                self.abrir_tela_principal()
            else:
                self.exibir_mensagem("Credenciais inválidas. Tente novamente.", "red")

            cursor.close()
            conexao.close()
        except Exception:
            self.exibir_mensagem("Erro ao conectar ao banco de dados.", "red")

    def exibir_mensagem(self, mensagem, cor="red"):
        """Exibe uma mensagem no rótulo de mensagem."""
        self.mensagem_label.config(text=mensagem, fg=cor)

    def abrir_tela_principal(self):
        self.root.withdraw()  # Esconde a janela de login

        # Cria a nova janela
        tela_principal = tk.Toplevel(self.root)
        tela_principal.title("Tela Principal")
        tela_principal.geometry("400x300")

        # Centralizar a nova janela
        width = 400
        height = 300
        screen_width = tela_principal.winfo_screenwidth()
        screen_height = tela_principal.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        tela_principal.geometry(f"{width}x{height}+{x}+{y}")

        tk.Label(tela_principal, text="Bem-vindo à Tela Principal!", font=("Arial", 16)).pack(pady=20)

        # Botão para sair
        tk.Button(tela_principal, text="Sair", command=lambda: self.sair(tela_principal)).pack(pady=20)

    def sair(self, tela_principal):
        tela_principal.destroy()  # Fecha a tela principal
        self.root.deiconify()  # Traz de volta a janela de login
