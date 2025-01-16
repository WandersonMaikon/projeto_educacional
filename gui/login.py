import tkinter as tk
from dados.database import conectar
from gui.tela_principal import TelaPrincipal  # Importe a classe da tela principal


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.width = 300
        self.height = 200
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.x = (self.screen_width - self.width) // 2
        self.y = (self.screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        # Elementos da interface
        tk.Label(root, text="Login", font=("Arial", 32, "bold")).pack(pady=20)
        tk.Label(root, text="Nome de Usuário", font=("Arial", 14)).pack(pady=5)
        self.username_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=10)
        tk.Label(root, text="Senha", font=("Arial", 14)).pack(pady=5)
        self.password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=30)
        self.password_entry.pack(pady=20)
        self.mensagem_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.mensagem_label.pack(pady=5)
        tk.Button(root, text="Login", font=("Arial", 16, "bold"), command=self.fazer_login).pack(pady=20)

    def fazer_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            conexao = conectar()
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE username = %s AND password = %s", (username, password))
            usuario = cursor.fetchone()

            if usuario:
                self.abrir_tela_principal()
            else:
                self.mensagem_label.config(text="Credenciais inválidas. Tente novamente.", fg="red")
            cursor.close()
            conexao.close()
        except Exception:
            self.mensagem_label.config(text="Erro ao conectar ao banco de dados.", fg="red")

    def abrir_tela_principal(self):
        self.root.withdraw()  # Esconde a janela de login
        tela_principal = tk.Toplevel(self.root)
        TelaPrincipal(tela_principal, self.root)  # Chama a classe da tela principal
