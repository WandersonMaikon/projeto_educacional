import mysql.connector
from mysql.connector import Error
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="maikon123",
            database="sistema_cursos"
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        raise Exception(f"Erro ao conectar ao banco de dados: {e}")
