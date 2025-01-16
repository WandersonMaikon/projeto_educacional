import tkinter as tk
from tkinter import messagebox
from dados.database import conectar

class ProfessorDAO:
    """Classe para lidar com operações relacionadas ao banco de dados."""
    @staticmethod
    def salvar_professor(nome, matricula, curso, telefone):
        """Salva os dados do professor no banco de dados."""
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            query = "INSERT INTO professores (nome, matricula, curso, telefone) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nome, matricula, curso, telefone))
            conexao.commit()
            cursor.close()
            conexao.close()
            return True, "Professor cadastrado com sucesso!"
        except Exception as e:
            return False, str(e)

class TelaProfessor:
    def __init__(self, root):
        self.root = root

        # Criar janela separada
        self.cadastro_window = tk.Toplevel(self.root)
        self.cadastro_window.title("Cadastrar Professor")
        self.cadastro_window.geometry("600x400")

        # Centralizar a nova janela
        width = 600
        height = 400
        screen_width = self.cadastro_window.winfo_screenwidth()
        screen_height = self.cadastro_window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.cadastro_window.geometry(f"{width}x{height}+{x}+{y}")

        # Estilizando a janela
        self.cadastro_window.config(bg="#f0f0f0")
        tk.Label(
            self.cadastro_window,
            text="Cadastro de Professor",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        ).pack(pady=20)

        # Labels e campos de entrada
        form_frame = tk.Frame(self.cadastro_window, bg="#f0f0f0")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nome:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.nome_entry = tk.Entry(form_frame, width=40)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Matrícula:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.matricula_entry = tk.Entry(form_frame, width=40)
        self.matricula_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Curso:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.curso_entry = tk.Entry(form_frame, width=40)
        self.curso_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Telefone:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.telefone_entry = tk.Entry(form_frame, width=40)
        self.telefone_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botão de salvar
        button_frame = tk.Frame(self.cadastro_window, bg="#f0f0f0")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Salvar",
            command=self.salvar_professor,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
            width=15
        ).pack(side="left", padx=10)

        tk.Button(
            button_frame,
            text="Cancelar",
            command=self.cadastro_window.destroy,
            bg="#f44336",
            fg="white",
            font=("Arial", 12),
            width=15
        ).pack(side="right", padx=10)

    def salvar_professor(self):
        """Coleta os dados e delega a lógica para salvar o professor."""
        nome = self.nome_entry.get().strip()
        matricula = self.matricula_entry.get().strip()
        curso = self.curso_entry.get().strip()
        telefone = self.telefone_entry.get().strip()

        if not nome or not matricula or not curso or not telefone:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        sucesso, mensagem = ProfessorDAO.salvar_professor(nome, matricula, curso, telefone)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.cadastro_window.destroy()
        else:
            messagebox.showerror("Erro", f"Erro ao salvar no banco de dados: {mensagem}")
