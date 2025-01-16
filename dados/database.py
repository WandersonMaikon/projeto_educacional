import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Substitua pelos dados do seu banco
        conexao = mysql.connector.connect(
            host="localhost",       # Host do banco de dados
            user="root",     # Usuário do banco
            password="maikon123",   # Senha do banco
            database="sistema_cursos"    # Nome do banco de dados
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        raise Exception(f"Erro ao conectar ao banco de dados: {e}")
